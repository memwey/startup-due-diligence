#!/usr/bin/env python3
"""Verify structural consistency between English and Simplified Chinese Markdown."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


EN_UPDATED_RE = re.compile(r"Last updated:\s*(\d{4}-\d{2}-\d{2})")
ZH_UPDATED_RE = re.compile(r"最后更新[：:]\s*(\d{4}-\d{2}-\d{2})")
ZH_SYNC_RE = re.compile(r"同步至[：:]\s*(\d{4}-\d{2}-\d{2})")
HEADING_RE = re.compile(r"^(#{1,6})\s+")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*]\(([^)]+)\)")
EXTERNAL_LINK_RE = re.compile(r"\[[^\]]*]\((https?://[^)\s]+)\)")


@dataclass(frozen=True)
class Pair:
    english: Path
    chinese: Path


def lines_outside_fences(text: str) -> list[str]:
    """Return Markdown lines excluding fenced code blocks."""
    result: list[str] = []
    in_fence = False
    fence_marker = ""

    for line in text.splitlines():
        stripped = line.lstrip()
        if not in_fence and (stripped.startswith("```") or stripped.startswith("~~~")):
            in_fence = True
            fence_marker = stripped[:3]
            continue
        if in_fence and stripped.startswith(fence_marker):
            in_fence = False
            fence_marker = ""
            continue
        if not in_fence:
            result.append(line)

    return result


def find_pairs(root: Path) -> tuple[list[Pair], list[str]]:
    """Discover canonical English pages and their expected Chinese translations."""
    english_pages = sorted(root.rglob("README.md"))
    guide = root / "GUIDE.md"
    if guide.exists():
        english_pages.append(guide)

    pairs: list[Pair] = []
    errors: list[str] = []

    for english in sorted(set(english_pages)):
        chinese = english.with_name(
            "GUIDE.zh-CN.md" if english.name == "GUIDE.md" else "README.zh-CN.md"
        )
        if not chinese.exists():
            errors.append(f"missing Chinese translation: {chinese.relative_to(root)}")
            continue
        pairs.append(Pair(english=english, chinese=chinese))

    expected_english = {pair.english.resolve() for pair in pairs}
    chinese_pages = list(root.rglob("README.zh-CN.md"))
    guide_chinese = root / "GUIDE.zh-CN.md"
    if guide_chinese.exists():
        chinese_pages.append(guide_chinese)

    for chinese in chinese_pages:
        english = chinese.with_name(
            "GUIDE.md" if chinese.name == "GUIDE.zh-CN.md" else "README.md"
        )
        if english.resolve() not in expected_english:
            errors.append(f"orphan Chinese translation: {chinese.relative_to(root)}")

    return pairs, errors


def one_date(pattern: re.Pattern[str], text: str, label: str, path: Path) -> tuple[str | None, list[str]]:
    matches = pattern.findall("\n".join(lines_outside_fences(text)))
    if len(matches) == 1:
        return matches[0], []
    if not matches:
        return None, [f"{path}: missing {label} date"]
    return None, [f"{path}: expected one {label} date, found {len(matches)}"]


def heading_levels(text: str) -> list[int]:
    return [
        len(match.group(1))
        for line in lines_outside_fences(text)
        if (match := HEADING_RE.match(line))
    ]


def table_row_count(text: str) -> int:
    return sum(line.lstrip().startswith("|") for line in lines_outside_fences(text))


def section_external_links(text: str, title: str) -> set[str] | None:
    """Return unique external links in a level-two section, or None if absent."""
    section_lines: list[str] = []
    in_section = False

    for line in lines_outside_fences(text):
        if line.startswith("## "):
            current_title = line[3:].strip()
            if in_section:
                break
            in_section = current_title == title
            continue
        if in_section:
            section_lines.append(line)

    if not in_section and not section_lines:
        return None
    return set(EXTERNAL_LINK_RE.findall("\n".join(section_lines)))


def check_pair(pair: Pair, root: Path) -> tuple[list[str], str]:
    english_text = pair.english.read_text(encoding="utf-8")
    chinese_text = pair.chinese.read_text(encoding="utf-8")
    english_name = pair.english.relative_to(root)
    chinese_name = pair.chinese.relative_to(root)
    errors: list[str] = []

    en_updated, date_errors = one_date(
        EN_UPDATED_RE, english_text, "Last updated", english_name
    )
    errors.extend(date_errors)
    zh_updated, date_errors = one_date(
        ZH_UPDATED_RE, chinese_text, "最后更新", chinese_name
    )
    errors.extend(date_errors)
    zh_synced, date_errors = one_date(
        ZH_SYNC_RE, chinese_text, "同步至", chinese_name
    )
    errors.extend(date_errors)

    if en_updated and zh_updated and en_updated != zh_updated:
        errors.append(
            f"{english_name} / {chinese_name}: Last updated mismatch "
            f"({en_updated} != {zh_updated})"
        )
    if en_updated and zh_synced and en_updated != zh_synced:
        errors.append(
            f"{chinese_name}: translation is stale "
            f"(English {en_updated}, synchronized through {zh_synced})"
        )

    en_headings = heading_levels(english_text)
    zh_headings = heading_levels(chinese_text)
    if en_headings != zh_headings:
        errors.append(
            f"{english_name} / {chinese_name}: heading structure differs "
            f"({en_headings} != {zh_headings})"
        )

    en_rows = table_row_count(english_text)
    zh_rows = table_row_count(chinese_text)
    if en_rows != zh_rows:
        errors.append(
            f"{english_name} / {chinese_name}: table row count differs "
            f"({en_rows} != {zh_rows})"
        )

    en_sources = section_external_links(english_text, "Resources")
    zh_sources = section_external_links(chinese_text, "资料来源")
    if (en_sources is None) != (zh_sources is None):
        errors.append(
            f"{english_name} / {chinese_name}: Resources section exists in only one language"
        )
    elif en_sources is not None and zh_sources is not None and en_sources != zh_sources:
        missing_zh = sorted(en_sources - zh_sources)
        extra_zh = sorted(zh_sources - en_sources)
        if missing_zh:
            errors.append(
                f"{chinese_name}: source links missing from translation: "
                + ", ".join(missing_zh)
            )
        if extra_zh:
            errors.append(
                f"{chinese_name}: source links not present in English: "
                + ", ".join(extra_zh)
            )

    source_count = len(en_sources) if en_sources is not None else 0
    summary = (
        f"{english_name} <-> {chinese_name}: "
        f"synced {en_updated or 'unknown'}, {source_count} source links"
    )
    return errors, summary


def check_local_links(root: Path) -> list[str]:
    errors: list[str] = []

    for markdown in sorted(root.rglob("*.md")):
        text = "\n".join(lines_outside_fences(markdown.read_text(encoding="utf-8")))
        for target in MARKDOWN_LINK_RE.findall(text):
            target = target.strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.removeprefix("<").removesuffix(">")
            relative_target = target.split("#", 1)[0]
            if not relative_target:
                continue
            resolved = (markdown.parent / relative_target).resolve()
            if not resolved.exists():
                errors.append(
                    f"{markdown.relative_to(root)}: broken local link: {target}"
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify English/Simplified Chinese Markdown synchronization."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the parent of scripts/)",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    pairs, errors = find_pairs(root)
    summaries: list[str] = []

    for pair in pairs:
        pair_errors, summary = check_pair(pair, root)
        errors.extend(pair_errors)
        summaries.append(summary)

    errors.extend(check_local_links(root))

    if errors:
        print(f"FAIL: {len(errors)} problem(s)")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"OK: {len(pairs)} translation pair(s)")
    for summary in summaries:
        print(f"  - {summary}")
    print("  - all local Markdown links resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
