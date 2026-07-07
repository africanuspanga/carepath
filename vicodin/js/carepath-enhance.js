/* CarePath — progressive UI enhancements + enquiry cart.
   Pure vanilla JS; no dependencies. Degrades gracefully. */
(function () {
  'use strict';

  var STORAGE_KEY = 'carepath-cart';
  var reduce = window.matchMedia &&
    window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------------------------------------------------------- Helpers */
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  function setYear() {
    var els = document.querySelectorAll('.current-year');
    for (var i = 0; i < els.length; i++) {
      if (!els[i].textContent.trim()) {
        els[i].textContent = new Date().getFullYear();
      }
    }
  }

  function showToast(message) {
    var toast = document.querySelector('.cp-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.className = 'cp-toast';
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(function () { toast.classList.remove('show'); }, 2800);
  }

  /* ---------------------------------------------------------------- Cart */
  function getCart() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : [];
    } catch (e) { return []; }
  }

  function saveCart(cart) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(cart)); }
    catch (e) {}
    updateCartBadge();
    renderCartDrawer();
  }

  function addToCart(item) {
    var cart = getCart();
    var existing = cart.find(function (c) { return c.id === item.id; });
    if (existing) {
      existing.qty = (existing.qty || 1) + 1;
    } else {
      cart.push({
        id: item.id,
        name: item.name,
        category: item.category || '',
        image: item.image || '',
        qty: 1
      });
    }
    saveCart(cart);
    showToast(item.name + ' added to cart');
    openCartDrawer();
  }

  function removeFromCart(id) {
    var cart = getCart().filter(function (c) { return c.id !== id; });
    saveCart(cart);
  }

  function updateQty(id, delta) {
    var cart = getCart();
    var item = cart.find(function (c) { return c.id === id; });
    if (!item) return;
    item.qty = (item.qty || 1) + delta;
    if (item.qty < 1) item.qty = 1;
    saveCart(cart);
  }

  function clearCart() {
    saveCart([]);
  }

  function cartCount() {
    return getCart().reduce(function (sum, item) { return sum + (item.qty || 1); }, 0);
  }

  function updateCartBadge() {
    var badges = document.querySelectorAll('.cp-cart-count');
    var count = cartCount();
    badges.forEach(function (badge) {
      badge.textContent = count;
      badge.style.display = count ? 'inline-block' : 'none';
    });
  }

  function buildEnquiryBody() {
    var cart = getCart();
    if (!cart.length) return '';
    var lines = ['Hello CarePath,', '', 'I would like to enquire about the following items:', ''];
    cart.forEach(function (item, idx) {
      lines.push((idx + 1) + '. ' + item.name + (item.category ? ' (' + item.category + ')' : '') + ' — Qty: ' + (item.qty || 1));
    });
    lines.push('', 'Please send me a quotation.', '', 'Best regards,');
    return lines.join('%0D%0A');
  }

  function submitEnquiry() {
    var cart = getCart();
    if (!cart.length) {
      showToast('Your cart is empty');
      return;
    }
    var subject = 'Enquiry from CarePath Website (' + cart.length + ' item' + (cart.length > 1 ? 's' : '') + ')';
    var body = buildEnquiryBody();
    window.location.href = 'mailto:info@carepath.co.tz?subject=' + encodeURIComponent(subject) + '&body=' + body;
  }

  /* ---------------------------------------------------------------- Drawer */
  function ensureDrawer() {
    if (document.getElementById('cp-cart-drawer')) return;

    var overlay = document.createElement('div');
    overlay.id = 'cp-cart-overlay';
    overlay.className = 'cp-cart-overlay';
    overlay.addEventListener('click', closeCartDrawer);

    var drawer = document.createElement('div');
    drawer.id = 'cp-cart-drawer';
    drawer.className = 'cp-cart-drawer';
    drawer.innerHTML =
      '<div class="cp-cart-header">' +
        '<h4>Your Enquiry</h4>' +
        '<button class="cp-cart-close" aria-label="Close">&times;</button>' +
      '</div>' +
      '<div class="cp-cart-body" id="cp-cart-body"></div>' +
      '<div class="cp-cart-footer">' +
        '<p>Add items you need and send us one enquiry. We\'ll respond with a quote.</p>' +
        '<div class="cp-cart-actions">' +
          '<button class="btn theme-btn-1 btn-effect-1" id="cp-submit-enquiry">Request Quote</button>' +
          '<button class="btn theme-btn-2 btn-effect-2" id="cp-clear-cart">Clear Cart</button>' +
        '</div>' +
      '</div>';

    drawer.querySelector('.cp-cart-close').addEventListener('click', closeCartDrawer);
    drawer.querySelector('#cp-submit-enquiry').addEventListener('click', submitEnquiry);
    drawer.querySelector('#cp-clear-cart').addEventListener('click', function () {
      clearCart();
      showToast('Enquiry list cleared');
    });

    document.body.appendChild(overlay);
    document.body.appendChild(drawer);
  }

  function openCartDrawer() {
    ensureDrawer();
    document.getElementById('cp-cart-overlay').classList.add('open');
    document.getElementById('cp-cart-drawer').classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeCartDrawer() {
    var overlay = document.getElementById('cp-cart-overlay');
    var drawer = document.getElementById('cp-cart-drawer');
    if (overlay) overlay.classList.remove('open');
    if (drawer) drawer.classList.remove('open');
    document.body.style.overflow = '';
  }

  function renderCartDrawer() {
    var body = document.getElementById('cp-cart-body');
    if (!body) return;
    var cart = getCart();
    if (!cart.length) {
      body.innerHTML =
        '<div class="cp-cart-empty">' +
          '<i class="fas fa-shopping-cart"></i>' +
          '<p>Your cart is empty.</p>' +
          '<p style="font-size:.85rem;margin-top:8px;">Add services or products to request a quote.</p>' +
        '</div>';
      return;
    }
    var html = '';
    cart.forEach(function (item) {
      html +=
        '<div class="cp-cart-item" data-id="' + item.id + '">' +
          (item.image ? '<img src="' + item.image + '" alt="" class="cp-cart-item-img">' : '') +
          '<div class="cp-cart-item-info">' +
            '<h5>' + item.name + '</h5>' +
            (item.category ? '<small>' + item.category + '</small>' : '') +
            '<div class="cp-cart-qty">' +
              '<button class="cp-qty-minus" aria-label="Decrease">-</button>' +
              '<span>' + (item.qty || 1) + '</span>' +
              '<button class="cp-qty-plus" aria-label="Increase">+</button>' +
            '</div>' +
            '<button class="cp-cart-remove">Remove</button>' +
          '</div>' +
        '</div>';
    });
    body.innerHTML = html;

    body.querySelectorAll('.cp-qty-minus').forEach(function (btn) {
      btn.addEventListener('click', function () {
        updateQty(this.closest('.cp-cart-item').dataset.id, -1);
      });
    });
    body.querySelectorAll('.cp-qty-plus').forEach(function (btn) {
      btn.addEventListener('click', function () {
        updateQty(this.closest('.cp-cart-item').dataset.id, 1);
      });
    });
    body.querySelectorAll('.cp-cart-remove').forEach(function (btn) {
      btn.addEventListener('click', function () {
        removeFromCart(this.closest('.cp-cart-item').dataset.id);
      });
    });
  }

  function initCartIcons() {
    document.querySelectorAll('.cp-cart-wrap').forEach(function (wrap) {
      wrap.addEventListener('click', openCartDrawer);
    });
  }

  function initAddButtons() {
    document.querySelectorAll('[data-cp-add]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var id = this.dataset.cpAdd;
        var name = this.dataset.cpName;
        var category = this.dataset.cpCategory;
        var image = this.dataset.cpImage;
        if (!id || !name) return;
        addToCart({ id: id, name: name, category: category, image: image });
        this.classList.add('added');
        this.innerHTML = '<i class="fas fa-check"></i> Added';
        setTimeout(function (b) {
          b.classList.remove('added');
          b.innerHTML = '<i class="fas fa-shopping-cart"></i> Add to Cart';
        }, 1800, this);
      });
    });
  }

  /* ---------------------------------------------------------------- Scroll reveal */
  function initReveal() {
    var selector = [
      '.ltn__feature-item',
      '.ltn__product-item',
      '.cp-service-card',
      '.cp-product-card',
      '.product-category-card',
      '.carepath-roadmap-item',
      '.ltn__contact-address-item',
      '.ltn__form-box',
      '.about-us-img-wrap',
      '.about-us-info-wrap',
      '.section-title-area',
      '.ltn__banner-item',
      '.cp-stat-card',
      '.cp-client-card',
      '.cp-testimonial-card'
    ].join(',');

    var nodes = Array.prototype.slice.call(document.querySelectorAll(selector));
    if (!nodes.length) return;

    if (reduce || !('IntersectionObserver' in window)) return;

    nodes.forEach(function (el) { el.classList.add('cp-reveal'); });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var el = entry.target;
          var siblings = el.parentNode ? el.parentNode.children : [el];
          var idx = Array.prototype.indexOf.call(siblings, el);
          el.style.transitionDelay = Math.min(idx, 4) * 60 + 'ms';
          el.classList.add('cp-in');
          io.unobserve(el);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });

    nodes.forEach(function (el) { io.observe(el); });
  }

  /* ---------------------------------------------------------------- Init */
  ready(function () {
    setYear();
    initReveal();
    ensureDrawer();
    updateCartBadge();
    renderCartDrawer();
    initCartIcons();
    initAddButtons();
  });
})();
