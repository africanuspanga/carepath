/* CarePath — progressive UI enhancements (scroll reveal + year).
   Purely additive; no dependency on jQuery. Degrades gracefully. */
(function () {
  'use strict';

  var reduce = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Fill copyright year in case the template's jQuery hook doesn't run.
  function setYear() {
    var els = document.querySelectorAll('.current-year');
    for (var i = 0; i < els.length; i++) {
      if (!els[i].textContent.trim()) {
        els[i].textContent = new Date().getFullYear();
      }
    }
  }

  function initReveal() {
    var selector = [
      '.ltn__feature-item',
      '.ltn__product-item',
      '.product-category-card',
      '.carepath-roadmap-item',
      '.ltn__contact-address-item',
      '.ltn__form-box',
      '.about-us-img-wrap',
      '.about-us-info-wrap',
      '.section-title-area',
      '.ltn__banner-item'
    ].join(',');

    var nodes = Array.prototype.slice.call(document.querySelectorAll(selector));
    if (!nodes.length) return;

    // No IntersectionObserver or reduced motion → show everything immediately.
    if (reduce || !('IntersectionObserver' in window)) return;

    nodes.forEach(function (el) { el.classList.add('cp-reveal'); });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var el = entry.target;
          // Stagger siblings within the same row for a polished cascade.
          var siblings = el.parentNode ? el.parentNode.children : [el];
          var idx = Array.prototype.indexOf.call(siblings, el);
          el.style.transitionDelay = Math.min(idx, 5) * 80 + 'ms';
          el.classList.add('cp-in');
          io.unobserve(el);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    nodes.forEach(function (el) { io.observe(el); });
  }

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  ready(function () { setYear(); initReveal(); });
})();
