// Table-of-contents scroll spy. Progressive enhancement only.
(function () {
  var toc = document.querySelector(".toc");
  if (!toc || !("IntersectionObserver" in window)) return;

  var links = {};
  toc.querySelectorAll("a[href^='#']").forEach(function (a) {
    links[decodeURIComponent(a.hash.slice(1))] = a;
  });
  var headings = Object.keys(links)
    .map(function (id) { return document.getElementById(id); })
    .filter(Boolean);
  if (!headings.length) return;

  var setActive = function (id) {
    toc.querySelectorAll("a.active").forEach(function (a) {
      a.classList.remove("active");
    });
    if (links[id]) links[id].classList.add("active");
  };

  var visible = new Set();
  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) visible.add(e.target.id);
        else visible.delete(e.target.id);
      });
      // highlight the first visible heading, or the last one scrolled past
      var current = null;
      for (var i = 0; i < headings.length; i++) {
        if (visible.has(headings[i].id)) { current = headings[i].id; break; }
        if (headings[i].getBoundingClientRect().top < 100) current = headings[i].id;
      }
      if (current) setActive(current);
    },
    { rootMargin: "-10% 0px -70% 0px" }
  );
  headings.forEach(function (h) { observer.observe(h); });
})();
