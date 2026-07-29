# startup-due-diligence

**English** | [简体中文](README.zh-CN.md)

> Due diligence for engineers.
> Last updated: 2026-07-29.

An open research repository that gives engineers sourced evidence for evaluating
technology startups before joining them.

## Why this project

Choosing a startup to join is difficult.

Traditional startup databases focus on:

- Funding
- Valuation
- Investors
- Market size

But engineers often care about different questions:

- What problem is the company solving?
- What systems would an engineer actually work on?
- What does the public record show about the engineering environment?
- What evidence is available about the company's traction and financing?
- What should engineers know before joining?

This project collects the underlying facts needed to assess those questions. It
does not score companies, recommend whether to join, or replace your own
interviews and due diligence.

## Research standard

The repository is evidence-first:

1. Prefer primary sources such as product documentation, company releases,
   corporate registries, and first-party job postings.
2. Attach a specific source and date to every figure.
3. Label conclusions inferred from job postings or other indirect evidence.
4. Record conflicting claims instead of silently choosing one.
5. Treat missing public information as a scoped search result, not proof that
   the information or practice does not exist.

The complete page structure, source hierarchy, and publishing checklist are in
[GUIDE.md](GUIDE.md).

## Early-stage companies and founder social media

For very early-stage companies, a founder's public professional social-media
account may be one of the few current first-party sources. Public posts can be
used to:

- find product launches, hiring plans, customer announcements, and links to
  longer-form sources;
- record what the founder publicly stated, with the account, post URL, and date;
- identify leads that can be checked against company pages, registries, job
  postings, or later announcements.

Social posts require stricter attribution than formal company materials. A
founder's statement is evidence that the statement was made; it is not
independent confirmation that the claim is true. Aspirations, estimates, and
personal opinions must be labelled as such. Research must not use private or
access-controlled content, collect unrelated personal information, or infer
character, culture, or business quality from personal activity.

## Contributing

Before adding or updating a company:

1. Read [GUIDE.md](GUIDE.md).
2. Copy its company-page skeleton.
3. Link every number and time-sensitive statement to a dated source.
4. Separate verified facts, company claims, and researcher inference.
5. Run through the guide's publishing checklist and set `Last updated`.

Verify bilingual consistency before publishing:

```bash
python3 scripts/verify_translations.py
```

Corrections with a more direct or more recent source are welcome. When sources
disagree, preserve the disagreement in the company page rather than overwriting
one claim without explanation.

## Disclaimer

This repository contains independent research notes based on publicly available
information. It is not affiliated with the companies covered. Sources can be
incomplete, claims can change, and information may become outdated. Verify
important information directly with the company and other authoritative sources
before making employment, investment, or commercial decisions.

## License

[MIT](LICENSE)
