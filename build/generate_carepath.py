#!/usr/bin/env python3
"""Generate CarePath static HTML pages from shared template parts."""
from pathlib import Path

BASE = Path(__file__).parent

NAV = """
<li><a href="index.html">Home</a></li>
<li class="menu-icon"><a href="about.html">About</a>
    <ul class="sub-menu">
        <li><a href="about.html">Company Profile</a></li>
        <li><a href="about.html#roadmap">Roadmap</a></li>
        <li><a href="about.html#mission">Mission & Vision</a></li>
    </ul>
</li>
<li><a href="services.html">Services</a></li>
<li><a href="products.html">Products</a></li>
<li><a href="partners.html">Partners</a></li>
<li><a href="clients.html">Clients</a></li>
<li><a href="contact.html">Contact</a></li>
"""

MOBILE_NAV = """
<li><a href="index.html">Home</a></li>
<li><a href="about.html">About</a></li>
<li><a href="services.html">Services</a></li>
<li><a href="products.html">Products</a></li>
<li><a href="partners.html">Partners</a></li>
<li><a href="clients.html">Clients</a></li>
<li><a href="contact.html">Contact</a></li>
"""


def head(title: str) -> str:
    return f"""<!doctype html>
<html class="no-js" lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>{title} | CarePath Company Limited</title>
    <meta name="robots" content="index, follow" />
    <meta name="description" content="CarePath Company Limited - Transforming access to quality medical equipment across Tanzania. Distribution, importation, installation, training and after-sales support.">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="shortcut icon" href="img/favicon.png" type="image/x-icon" />
    <link rel="stylesheet" href="css/font-icons.css">
    <link rel="stylesheet" href="css/plugins.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/responsive.css">
    <link rel="stylesheet" href="css/carepath-custom.css">
</head>
<body>
<!--[if lte IE 9]>
    <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="https://browsehappy.com/">upgrade your browser</a> to improve your experience and security.</p>
<![endif]-->
<div class="body-wrapper">
"""


def header(active: str = "") -> str:
    return f"""<!-- HEADER AREA START -->
<header class="ltn__header-area ltn__header-3">
    <div class="ltn__header-top-area border-bottom">
        <div class="container">
            <div class="row">
                <div class="col-md-7">
                    <div class="ltn__top-bar-menu">
                        <ul>
                            <li><a href="mailto:info@carepath.co.tz"><i class="icon-mail"></i> info@carepath.co.tz</a></li>
                            <li><a href="contact.html"><i class="icon-placeholder"></i> Wikicha Tower, Mikocheni, Dar es Salaam, Tanzania</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-md-5">
                    <div class="top-bar-right text-end">
                        <div class="ltn__top-bar-menu">
                            <ul>
                                <li>
                                    <div class="ltn__social-media">
                                        <ul>
                                            <li><a href="#" title="Facebook"><i class="fab fa-facebook-f"></i></a></li>
                                            <li><a href="#" title="Linkedin"><i class="fab fa-linkedin"></i></a></li>
                                            <li><a href="#" title="Instagram"><i class="fab fa-instagram"></i></a></li>
                                        </ul>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="ltn__header-middle-area">
        <div class="container">
            <div class="row">
                <div class="col">
                    <div class="site-logo">
                        <a href="index.html"><img src="img/carepath-logo.png" alt="CarePath Logo"></a>
                    </div>
                </div>
                <div class="col header-contact-serarch-column d-none d-lg-block">
                    <div class="header-contact-search">
                        <div class="header-feature-item">
                            <div class="header-feature-icon"><i class="icon-call"></i></div>
                            <div class="header-feature-info">
                                <h6>Phone</h6>
                                <p><a href="tel:+255719902445">+255 719 902 445</a></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="header-bottom-area ltn__border-top ltn__header-sticky ltn__sticky-bg-secondary ltn__secondary-bg section-bg-1 menu-color-white d-none d-lg-block">
        <div class="container">
            <div class="row">
                <div class="col header-menu-column justify-content-center">
                    <div class="sticky-logo">
                        <div class="site-logo">
                            <a href="index.html"><img src="img/carepath-logo.png" alt="CarePath Logo"></a>
                        </div>
                    </div>
                    <div class="header-menu header-menu-2">
                        <nav>
                            <div class="ltn__main-menu">
                                <ul>
                                    {NAV}
                                </ul>
                            </div>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    </div>
</header>
<!-- HEADER AREA END -->

<!-- MOBILE MENU START -->
<div class="mobile-header-menu-fullwidth mb-30 d-block d-lg-none">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="mobile-menu-toggle d-lg-none">
                    <span>MENU</span>
                    <a href="#ltn__utilize-mobile-menu" class="ltn__utilize-toggle">
                        <svg viewBox="0 0 800 600">
                            <path d="M300,220 C300,220 520,220 540,220 C740,220 640,540 520,420 C440,340 300,200 300,200" id="top"></path>
                            <path d="M300,320 L540,320" id="middle"></path>
                            <path d="M300,210 C300,210 520,210 540,210 C740,210 640,530 520,410 C440,330 300,190 300,190" id="bottom" transform="translate(480, 320) scale(1, -1) translate(-480, -318)"></path>
                        </svg>
                    </a>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- MOBILE MENU END -->

<!-- Utilize Mobile Menu Start -->
<div id="ltn__utilize-mobile-menu" class="ltn__utilize ltn__utilize-mobile-menu">
    <div class="ltn__utilize-menu-inner ltn__scrollbar">
        <div class="ltn__utilize-menu-head">
            <div class="site-logo">
                <a href="index.html"><img src="img/carepath-logo.png" alt="CarePath Logo"></a>
            </div>
            <button class="ltn__utilize-close">×</button>
        </div>
        <div class="ltn__utilize-menu">
            <ul>
                {MOBILE_NAV}
            </ul>
        </div>
        <div class="ltn__social-media-2">
            <ul>
                <li><a href="#" title="Facebook"><i class="fab fa-facebook-f"></i></a></li>
                <li><a href="#" title="Linkedin"><i class="fab fa-linkedin"></i></a></li>
                <li><a href="#" title="Instagram"><i class="fab fa-instagram"></i></a></li>
            </ul>
        </div>
    </div>
</div>
<!-- Utilize Mobile Menu End -->
<div class="ltn__utilize-overlay"></div>
"""


def breadcrumb(title: str) -> str:
    return f"""<!-- BREADCRUMB AREA START -->
<div class="ltn__breadcrumb-area text-left bg-overlay-white-30 bg-image" data-bs-bg="img/bg/14.jpg">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="ltn__breadcrumb-inner">
                    <h1 class="page-title">{title}</h1>
                    <div class="ltn__breadcrumb-list">
                        <ul>
                            <li><a href="index.html"><span class="ltn__secondary-color"><i class="fas fa-home"></i></span> Home</a></li>
                            <li>{title}</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- BREADCRUMB AREA END -->
"""


def footer() -> str:
    return """<!-- FOOTER AREA START -->
<footer class="ltn__footer-area">
    <div class="footer-top-area section-bg-1 plr--5">
        <div class="container-fluid">
            <div class="row">
                <div class="col-xl-4 col-md-6 col-sm-6 col-12">
                    <div class="footer-widget footer-about-widget">
                        <div class="footer-logo">
                            <div class="site-logo">
                                <img src="img/carepath-logo.png" alt="CarePath Logo">
                            </div>
                        </div>
                        <p>CarePath Company Limited is transforming access to quality medical equipment across Tanzania through reliable distribution, regulatory-compliant importation, installation, training and after-sales support.</p>
                        <div class="footer-address">
                            <ul>
                                <li>
                                    <div class="footer-address-icon"><i class="icon-placeholder"></i></div>
                                    <div class="footer-address-info"><p>Wikicha Tower, Mikocheni, Mwai Kibaki Road, Dar es Salaam, Tanzania</p></div>
                                </li>
                                <li>
                                    <div class="footer-address-icon"><i class="icon-call"></i></div>
                                    <div class="footer-address-info"><p><a href="tel:+255719902445">+255 719 902 445</a></p></div>
                                </li>
                                <li>
                                    <div class="footer-address-icon"><i class="icon-mail"></i></div>
                                    <div class="footer-address-info"><p><a href="mailto:info@carepath.co.tz">info@carepath.co.tz</a></p></div>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="col-xl-2 col-md-6 col-sm-6 col-12">
                    <div class="footer-widget footer-menu-widget clearfix">
                        <h4 class="footer-title">Company</h4>
                        <div class="footer-menu">
                            <ul>
                                <li><a href="index.html">Home</a></li>
                                <li><a href="about.html">About Us</a></li>
                                <li><a href="services.html">Services</a></li>
                                <li><a href="products.html">Products</a></li>
                                <li><a href="contact.html">Contact</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="col-xl-3 col-md-6 col-sm-6 col-12">
                    <div class="footer-widget footer-menu-widget clearfix">
                        <h4 class="footer-title">Solutions</h4>
                        <div class="footer-menu">
                            <ul>
                                <li><a href="services.html">Equipment Distribution</a></li>
                                <li><a href="services.html">Importation & Compliance</a></li>
                                <li><a href="services.html">Installation & Support</a></li>
                                <li><a href="services.html">Training & Consultation</a></li>
                                <li><a href="services.html">After-Sales Service</a></li>
                            </ul>
                        </div>
                    </div>
                </div>
                <div class="col-xl-3 col-md-6 col-sm-12 col-12">
                    <div class="footer-widget footer-newsletter-widget">
                        <h4 class="footer-title">Get in Touch</h4>
                        <p>Need medical equipment or support? Send us a message and our team will respond promptly.</p>
                        <div class="btn-wrapper">
                            <a href="contact.html" class="theme-btn-1 btn btn-effect-1">Contact Us</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="ltn__copyright-area ltn__copyright-2 section-bg-7 plr--5">
        <div class="container-fluid ltn__border-top-2">
            <div class="row">
                <div class="col-md-6 col-12">
                    <div class="ltn__copyright-design clearfix">
                        <p>&copy; <span class="current-year"></span> CarePath Company Limited. All Rights Reserved.</p>
                    </div>
                </div>
                <div class="col-md-6 col-12 align-self-center">
                    <div class="ltn__copyright-menu text-end">
                        <ul>
                            <li><a href="about.html">Company Profile</a></li>
                            <li><a href="contact.html">Contact</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</footer>
<!-- FOOTER AREA END -->

</div>
<!-- Body main wrapper end -->

<div class="preloader d-none" id="preloader">
    <div class="preloader-inner">
        <div class="spinner">
            <div class="dot1"></div>
            <div class="dot2"></div>
        </div>
    </div>
</div>

<script src="js/plugins.js"></script>
<script src="js/main.js"></script>
</body>
</html>
"""


def wrap_page(title: str, body: str, include_breadcrumb: bool = True, breadcrumb_title: str = "") -> str:
    bc = breadcrumb(breadcrumb_title or title) if include_breadcrumb else ""
    return head(title) + header() + bc + body + footer()


# -----------------------------------------------------------------------------
# PAGE CONTENTS
# -----------------------------------------------------------------------------

INDEX_BODY = """<!-- SLIDER AREA START -->
<div class="ltn__slider-area ltn__slider-3 section-bg-1">
    <div class="ltn__slide-one-active slick-slide-arrow-1 slick-slide-dots-1">
        <div class="ltn__slide-item ltn__slide-item-2 ltn__slide-item-3 bg-image bg-overlay-theme-black-60" data-bs-bg="img/carepath/hero-1.jpg">
            <div class="ltn__slide-item-inner text-left">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-12 align-self-center">
                            <div class="slide-item-info">
                                <div class="slide-item-info-inner ltn__slide-animation">
                                    <h6 class="slide-sub-title white-color--- animated"><span><i class="fas fa-heartbeat"></i></span> Medical Equipment Solutions</h6>
                                    <h1 class="slide-title animated">Transforming Access to<br>Quality Medical Equipment</h1>
                                    <div class="slide-brief animated">
                                        <p>CarePath Company Limited delivers reliable, innovative and high-quality medical equipment across Tanzania, empowering healthcare providers to improve patient outcomes.</p>
                                    </div>
                                    <div class="btn-wrapper animated">
                                        <a href="services.html" class="theme-btn-1 btn btn-effect-1">Our Solutions</a>
                                        <a href="contact.html" class="btn btn-effect-3 btn-white">Contact Us <i class="icon-next"></i></a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="ltn__slide-item ltn__slide-item-2 ltn__slide-item-3 bg-image bg-overlay-theme-black-60" data-bs-bg="img/carepath/hero-2.jpg">
            <div class="ltn__slide-item-inner text-left">
                <div class="container">
                    <div class="row">
                        <div class="col-lg-12 align-self-center">
                            <div class="slide-item-info">
                                <div class="slide-item-info-inner ltn__slide-animation">
                                    <h6 class="slide-sub-title white-color--- animated"><span><i class="fas fa-shipping-fast"></i></span> Nationwide Distribution</h6>
                                    <h1 class="slide-title animated">End-to-End Healthcare<br>Equipment Support</h1>
                                    <div class="slide-brief animated">
                                        <p>From sourcing and importation to installation, training and after-sales service, we support healthcare institutions at every stage.</p>
                                    </div>
                                    <div class="btn-wrapper animated">
                                        <a href="products.html" class="theme-btn-1 btn btn-effect-1">Explore Products</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- SLIDER AREA END -->

<!-- ABOUT US AREA START -->
<div class="ltn__about-us-area pt-80 pb-90">
    <div class="container">
        <div class="row">
            <div class="col-lg-6 align-self-center">
                <div class="about-us-img-wrap about-img-left">
                    <img src="img/carepath/about.jpg" alt="Medical Equipment">
                </div>
            </div>
            <div class="col-lg-6 align-self-center">
                <div class="about-us-info-wrap">
                    <div class="section-title-area ltn__section-title-2--- mb-30">
                        <h6 class="section-subtitle section-subtitle-2 ltn__secondary-color">About CarePath</h6>
                        <h1 class="section-title">Your Trusted Partner in Medical Equipment</h1>
                        <p>Founded in 2023, CarePath Company Limited is on a mission to transform access to quality medical equipment across Tanzania. We supply hospitals, clinics, diagnostic centres, laboratories and research institutions with certified devices and integrated healthcare solutions.</p>
                    </div>
                    <ul class="ltn__list-item-1 ltn__list-item-1-before--- clearfix">
                        <li><i class="fas fa-check-square"></i> Nationwide distribution of certified medical devices.</li>
                        <li><i class="fas fa-check-square"></i> Regulatory-compliant importation and sourcing.</li>
                        <li><i class="fas fa-check-square"></i> Professional installation, training and after-sales support.</li>
                    </ul>
                    <div class="btn-wrapper mt-30">
                        <a href="about.html" class="theme-btn-1 btn btn-effect-1">Learn More</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- ABOUT US AREA END -->

<!-- SERVICES AREA START -->
<div class="ltn__service-area section-bg-1 pt-115 pb-70">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section-title-area ltn__section-title-2--- text-center">
                    <h6 class="section-subtitle section-subtitle-2 ltn__secondary-color">What We Do</h6>
                    <h1 class="section-title">Our Integrated Solutions</h1>
                </div>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-lg-4 col-sm-6 col-12 mb-50">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-truck-medical"></i></span></div>
                    <div class="ltn__feature-info">
                        <h3><a href="services.html">Medical Equipment Distribution</a></h3>
                        <p>Reliable nationwide distribution of certified medical devices and supplies.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-12 mb-50">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-globe"></i></span></div>
                    <div class="ltn__feature-info">
                        <h3><a href="services.html">Global Importation & Compliance</a></h3>
                        <p>Sourcing from recognized manufacturers with full Tanzanian regulatory compliance.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-12 mb-50">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-tools"></i></span></div>
                    <div class="ltn__feature-info">
                        <h3><a href="services.html">Installation & Technical Support</a></h3>
                        <p>Professional installation, commissioning and maintenance services.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-12 mb-50">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-user-md"></i></span></div>
                    <div class="ltn__feature-info">
                        <h3><a href="services.html">Training & Consultation</a></h3>
                        <p>Hands-on product training and ongoing technical consultation.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-12 mb-50">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-headset"></i></span></div>
                    <div class="ltn__feature-info">
                        <h3><a href="services.html">After-Sales Service</a></h3>
                        <p>Ensuring long-term functionality and performance of supplied equipment.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- SERVICES AREA END -->

<!-- BANNER AREA START -->
<div class="ltn__banner-area mt-120---">
    <div class="container">
        <div class="row ltn__custom-gutter--- justify-content-center">
            <div class="col-lg-4 col-sm-6">
                <div class="ltn__banner-item">
                    <div class="ltn__banner-img">
                        <a href="products.html"><img src="img/carepath/banner-1.jpg" alt="Banner Image"></a>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6">
                <div class="ltn__banner-item">
                    <div class="ltn__banner-img">
                        <a href="products.html"><img src="img/carepath/banner-2.jpg" alt="Banner Image"></a>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6">
                <div class="ltn__banner-item">
                    <div class="ltn__banner-img">
                        <a href="products.html"><img src="img/carepath/banner-3.jpg" alt="Banner Image"></a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- BANNER AREA END -->

<!-- PRODUCT AREA START (product-item-3) -->
<div class="ltn__product-area ltn__product-gutter no-product-ratting pt-85 pb-70">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section-title-area ltn__section-title-2 text-center">
                    <h6 class="section-subtitle section-subtitle-2 ltn__secondary-color">Our Catalogue</h6>
                    <h1 class="section-title">Featured Products</h1>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-3">
                <div class="row">
                    <div class="col-lg-12 col-sm-6">
                        <div class="ltn__banner-item">
                            <div class="ltn__banner-img">
                                <a href="products.html"><img src="img/carepath/banner-2.jpg" alt="Banner Image"></a>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-12 col-sm-6">
                        <div class="ltn__banner-item">
                            <div class="ltn__banner-img">
                                <a href="products.html"><img src="img/carepath/banner-1.jpg" alt="Banner Image"></a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-9">
                <div class="row ltn__tab-product-slider-one-active--- slick-arrow-1">
                    <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                        <div class="ltn__product-item ltn__product-item-2 text-left">
                            <div class="product-img">
                                <a href="products.html"><img src="img/carepath/product-1.jpg" alt="ICU & Critical Care"></a>
                                <div class="product-badge"><ul><li class="sale-badge">New</li></ul></div>
                            </div>
                            <div class="product-info">
                                <h2 class="product-title"><a href="products.html">ICU & Critical Care</a></h2>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                        <div class="ltn__product-item ltn__product-item-2 text-left">
                            <div class="product-img">
                                <a href="products.html"><img src="img/carepath/product-2.jpg" alt="Laboratory Diagnostics"></a>
                            </div>
                            <div class="product-info">
                                <h2 class="product-title"><a href="products.html">Laboratory Diagnostics</a></h2>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                        <div class="ltn__product-item ltn__product-item-2 text-left">
                            <div class="product-img">
                                <a href="products.html"><img src="img/carepath/product-3.jpg" alt="Medical Imaging"></a>
                                <div class="product-badge"><ul><li class="sale-badge">New</li></ul></div>
                            </div>
                            <div class="product-info">
                                <h2 class="product-title"><a href="products.html">Medical Imaging</a></h2>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                        <div class="ltn__product-item ltn__product-item-2 text-left">
                            <div class="product-img">
                                <a href="products.html"><img src="img/carepath/product-4.jpg" alt="Orthopaedic & Surgical"></a>
                            </div>
                            <div class="product-info">
                                <h2 class="product-title"><a href="products.html">Orthopaedic & Surgical</a></h2>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                        <div class="ltn__product-item ltn__product-item-2 text-left">
                            <div class="product-img">
                                <a href="products.html"><img src="img/carepath/banner-3.jpg" alt="Hospital Furniture"></a>
                                <div class="product-badge"><ul><li class="sale-badge">New</li></ul></div>
                            </div>
                            <div class="product-info">
                                <h2 class="product-title"><a href="products.html">Hospital Furniture</a></h2>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                        <div class="ltn__product-item ltn__product-item-2 text-left">
                            <div class="product-img">
                                <a href="products.html"><img src="img/carepath/banner-1.jpg" alt="General Medical Supplies"></a>
                            </div>
                            <div class="product-info">
                                <h2 class="product-title"><a href="products.html">General Medical Supplies</a></h2>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                        <div class="ltn__product-item ltn__product-item-2 text-left">
                            <div class="product-img">
                                <a href="products.html"><img src="img/carepath/hero-2.jpg" alt="Diagnostic Devices"></a>
                                <div class="product-badge"><ul><li class="sale-badge">New</li></ul></div>
                            </div>
                            <div class="product-info">
                                <h2 class="product-title"><a href="products.html">Diagnostic Devices</a></h2>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                        <div class="ltn__product-item ltn__product-item-2 text-left">
                            <div class="product-img">
                                <a href="products.html"><img src="img/carepath/about.jpg" alt="Healthcare Equipment"></a>
                            </div>
                            <div class="product-info">
                                <h2 class="product-title"><a href="products.html">Healthcare Equipment</a></h2>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-12 text-center mt-30">
                <a href="products.html" class="theme-btn-1 btn btn-effect-1">View All Products</a>
            </div>
        </div>
    </div>
</div>
<!-- PRODUCT AREA END -->

<!-- STRATEGIC PARTNERS AREA START -->
<div class="ltn__brand-logo-area section-bg-1 pt-80 pb-60">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section-title-area ltn__section-title-2--- text-center mb-40">
                    <h6 class="section-subtitle section-subtitle-2 ltn__secondary-color">Trusted Manufacturers</h6>
                    <h1 class="section-title">Our Strategic Partners</h1>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-12">
                <div class="carepath-logo-marquee">
                    <div class="carepath-logo-track">
                        <div class="carepath-logo-item"><h4>BIOBASE</h4></div>
                        <div class="carepath-logo-item"><h4>MEDIGlobal</h4></div>
                        <div class="carepath-logo-item"><h4>Makula</h4></div>
                        <div class="carepath-logo-item"><h4>Seamaty</h4></div>
                        <div class="carepath-logo-item"><h4>Macura</h4></div>
                        <div class="carepath-logo-item"><h4>Mindray</h4></div>
                        <!-- Duplicate for seamless loop -->
                        <div class="carepath-logo-item"><h4>BIOBASE</h4></div>
                        <div class="carepath-logo-item"><h4>MEDIGlobal</h4></div>
                        <div class="carepath-logo-item"><h4>Makula</h4></div>
                        <div class="carepath-logo-item"><h4>Seamaty</h4></div>
                        <div class="carepath-logo-item"><h4>Macura</h4></div>
                        <div class="carepath-logo-item"><h4>Mindray</h4></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-12 text-center mt-30">
                <a href="partners.html" class="theme-btn-1 btn btn-effect-1">View All Partners</a>
            </div>
        </div>
    </div>
</div>
<!-- STRATEGIC PARTNERS AREA END -->

<!-- KEY CLIENTS AREA START -->
<div class="ltn__brand-logo-area section-bg-1 pt-60 pb-90">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section-title-area ltn__section-title-2--- text-center mb-40">
                    <h6 class="section-subtitle section-subtitle-2 ltn__secondary-color">Healthcare & Research Institutions</h6>
                    <h1 class="section-title">Our Key Clients</h1>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-12">
                <div class="carepath-logo-marquee">
                    <div class="carepath-logo-track" style="animation-direction: reverse;">
                        <div class="carepath-logo-item"><h4>NIMR</h4><small>National Institute for Medical Research</small></div>
                        <div class="carepath-logo-item"><h4>UDOM</h4><small>University of Dodoma</small></div>
                        <div class="carepath-logo-item"><h4>NCAA</h4><small>Ngorongoro Conservation Area Authority</small></div>
                        <div class="carepath-logo-item"><h4>Hach</h4></div>
                        <div class="carepath-logo-item"><h4>TANESCO</h4></div>
                        <div class="carepath-logo-item"><h4>UNDP</h4></div>
                        <!-- Duplicate for seamless loop -->
                        <div class="carepath-logo-item"><h4>NIMR</h4><small>National Institute for Medical Research</small></div>
                        <div class="carepath-logo-item"><h4>UDOM</h4><small>University of Dodoma</small></div>
                        <div class="carepath-logo-item"><h4>NCAA</h4><small>Ngorongoro Conservation Area Authority</small></div>
                        <div class="carepath-logo-item"><h4>Hach</h4></div>
                        <div class="carepath-logo-item"><h4>TANESCO</h4></div>
                        <div class="carepath-logo-item"><h4>UNDP</h4></div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-lg-12 text-center mt-30">
                <a href="clients.html" class="theme-btn-2 btn btn-effect-2">View All Clients</a>
            </div>
        </div>
    </div>
</div>
<!-- KEY CLIENTS AREA END -->

<!-- CALL TO ACTION START -->
<div class="ltn__call-to-action-area call-to-action-6 before-bg-bottom">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="call-to-action-inner call-to-action-inner-6 ltn__secondary-bg position-relative text-center---">
                    <div class="coll-to-info text-color-white">
                        <h1>Ready to equip your healthcare facility?</h1>
                    </div>
                    <div class="btn-wrapper">
                        <a class="btn btn-effect-3 btn-white" href="contact.html">Get in Touch <i class="icon-next"></i></a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- CALL TO ACTION END -->
"""


ABOUT_BODY = """<!-- ABOUT US AREA START -->
<div class="ltn__about-us-area pt-115 pb-90">
    <div class="container">
        <div class="row">
            <div class="col-lg-6 align-self-center">
                <div class="about-us-img-wrap about-img-left">
                    <img src="img/carepath/about.jpg" alt="About CarePath">
                </div>
            </div>
            <div class="col-lg-6 align-self-center">
                <div class="about-us-info-wrap">
                    <div class="section-title-area ltn__section-title-2--- mb-30">
                        <h6 class="section-subtitle section-subtitle-2 ltn__secondary-color">Who We Are</h6>
                        <h1 class="section-title">CarePath Company Limited</h1>
                        <p>CarePath was founded in 2023 with a clear mission: <strong>to transform access to quality medical equipment across Tanzania.</strong></p>
                        <p>We operate across the healthcare technology value chain — from sourcing and importation to installation, training and after-sales support — serving government hospitals, regional referral hospitals, private healthcare institutions, diagnostic laboratories, NGOs, universities and research institutions.</p>
                    </div>
                    <ul class="ltn__list-item-1 ltn__list-item-1-before--- clearfix">
                        <li><i class="fas fa-check-square"></i> Founded in 2023 in Dar es Salaam, Tanzania.</li>
                        <li><i class="fas fa-check-square"></i> Trusted supplier of diagnostic, laboratory, ICU, imaging and general medical equipment.</li>
                        <li><i class="fas fa-check-square"></i> Partnerships with internationally recognized manufacturers.</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- ABOUT US AREA END -->

<!-- ROADMAP AREA START -->
<div id="roadmap" class="ltn__about-us-area section-bg-1 pt-115 pb-90">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section-title-area ltn__section-title-2--- text-center mb-50">
                    <h6 class="section-subtitle section-subtitle-2 ltn__secondary-color">Our Journey</h6>
                    <h1 class="section-title">Roadmap to the Future</h1>
                </div>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="carepath-roadmap">
                    <div class="carepath-roadmap-item">
                        <div class="carepath-roadmap-year">2023 — Company Establishment</div>
                        <p>CarePath was established and entered the healthcare equipment market in Tanzania, focusing on building reliable supplier relationships, developing importation channels and establishing a strong distribution foundation.</p>
                    </div>
                    <div class="carepath-roadmap-item">
                        <div class="carepath-roadmap-year">2024 — Product & Distribution Expansion</div>
                        <p>We expanded our product portfolio to include diagnostic, laboratory and general medical equipment, strengthening our distribution network and serving hospitals, clinics and diagnostic centres across different regions.</p>
                    </div>
                    <div class="carepath-roadmap-item">
                        <div class="carepath-roadmap-year">2025 — Operational & Technical-Support Growth</div>
                        <p>Operations scaled through improved warehousing and stronger quality-assurance protocols. We enhanced technical-support services including installation, application training and after-sales assistance.</p>
                    </div>
                    <div class="carepath-roadmap-item">
                        <div class="carepath-roadmap-year">2026 — Strategic Partnerships & Market Positioning</div>
                        <p>CarePath is strengthening partnerships with global manufacturers while expanding its presence within Tanzania’s healthcare sector, positioning itself as a trusted provider of integrated medical equipment and healthcare solutions.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- ROADMAP AREA END -->

<!-- MISSION VISION VALUES AREA START -->
<div id="mission" class="ltn__feature-area pt-115 pb-90">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section-title-area ltn__section-title-2--- text-center mb-50">
                    <h6 class="section-subtitle section-subtitle-2 ltn__secondary-color">Our Foundation</h6>
                    <h1 class="section-title">Mission, Vision & Values</h1>
                </div>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-lg-4 col-sm-6 col-12 mb-50">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-bullseye"></i></span></div>
                    <div class="ltn__feature-info">
                        <h3>Our Mission</h3>
                        <p>To deliver reliable, innovative and high-quality medical equipment that empowers healthcare providers to improve patient outcomes.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-12 mb-50">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-eye"></i></span></div>
                    <div class="ltn__feature-info">
                        <h3>Our Vision</h3>
                        <p>To become Tanzania’s leading provider of integrated medical equipment and healthcare solutions.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-12 mb-50">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-heart"></i></span></div>
                    <div class="ltn__feature-info">
                        <h3>Our Values</h3>
                        <ul class="text-start ps-4">
                            <li>Integrity in every transaction</li>
                            <li>Excellence in service delivery</li>
                            <li>Innovation in healthcare solutions</li>
                            <li>Commitment to patient-centred impact</li>
                            <li>Partnership-driven growth</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- MISSION VISION VALUES AREA END -->
"""


SERVICES_BODY = """<!-- ABOUT SERVICE AREA START -->
<div class="ltn__about-us-area pt-115 pb-90">
    <div class="container">
        <div class="row">
            <div class="col-lg-5 align-self-center">
                <div class="about-us-img-wrap ltn__img-shape-left about-img-left">
                    <img src="img/carepath/services.jpg" alt="Our Services">
                </div>
            </div>
            <div class="col-lg-7 align-self-center">
                <div class="about-us-info-wrap">
                    <div class="section-title-area ltn__section-title-2--- mb-20">
                        <h6 class="section-subtitle section-subtitle-2 ltn__secondary-color">What We Do</h6>
                        <h1 class="section-title">Our Integrated Solutions</h1>
                        <p>CarePath provides end-to-end medical equipment solutions designed to support healthcare providers at every stage — from procurement to long-term performance.</p>
                    </div>
                    <div class="btn-wrapper animated">
                        <a href="contact.html" class="theme-btn-1 btn btn-effect-1 text-uppercase">Get in Touch</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- ABOUT SERVICE AREA END -->

<!-- SERVICES DETAIL AREA START -->
<div class="ltn__service-area section-bg-1 pt-115 pb-70">
    <div class="container">
        <div class="row justify-content-center">
            <div class="col-lg-4 col-sm-6 col-12 mb-50">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-truck-medical"></i></span></div>
                    <div class="ltn__feature-info">
                        <h3>Medical Equipment Distribution</h3>
                        <p>Reliable nationwide distribution of certified medical devices and supplies to healthcare institutions across Tanzania.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-12 mb-50">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-globe"></i></span></div>
                    <div class="ltn__feature-info">
                        <h3>Global Importation & Regulatory Compliance</h3>
                        <p>Sourcing from internationally recognized manufacturers while ensuring full compliance with Tanzanian health authorities.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-12 mb-50">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-tools"></i></span></div>
                    <div class="ltn__feature-info">
                        <h3>Equipment Installation & Technical Support</h3>
                        <p>Professional installation, commissioning, technical setup and maintenance services.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-12 mb-50">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-user-md"></i></span></div>
                    <div class="ltn__feature-info">
                        <h3>Application Training & Consultation</h3>
                        <p>Hands-on product training and ongoing technical consultation for healthcare professionals.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-4 col-sm-6 col-12 mb-50">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-headset"></i></span></div>
                    <div class="ltn__feature-info">
                        <h3>After-Sales Service & Maintenance</h3>
                        <p>Ensuring long-term functionality and performance of supplied equipment through maintenance and technical follow-up.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- SERVICES DETAIL AREA END -->
"""


PRODUCTS_BODY = """<!-- PRODUCT AREA START -->
<div class="ltn__product-area ltn__product-gutter pt-115 pb-70">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section-title-area ltn__section-title-2 text-center mb-50">
                    <h6 class="section-subtitle section-subtitle-2 ltn__secondary-color">Comprehensive Range</h6>
                    <h1 class="section-title">Our Products</h1>
                    <p>CarePath supplies a comprehensive range of medical equipment, devices and healthcare supplies.</p>
                </div>
            </div>
        </div>
        <div class="row ltn__tab-product-slider-one-active--- slick-arrow-1">
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                <div class="ltn__product-item ltn__product-item-2 text-left">
                    <div class="product-img"><a href="contact.html"><img src="img/carepath/product-1.jpg" alt="ICU & Critical Care"></a></div>
                    <div class="product-info">
                        <h2 class="product-title"><a href="contact.html">ICU & Critical Care</a></h2>
                        <p style="font-size:0.85rem;color:#666;margin-top:6px;">Ventilators, patient monitors, infusion pumps and critical-care solutions.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                <div class="ltn__product-item ltn__product-item-2 text-left">
                    <div class="product-img"><a href="contact.html"><img src="img/carepath/product-2.jpg" alt="Laboratory Diagnostics"></a></div>
                    <div class="product-info">
                        <h2 class="product-title"><a href="contact.html">Laboratory Diagnostics</a></h2>
                        <p style="font-size:0.85rem;color:#666;margin-top:6px;">Microscopes, analysers, reagents and complete lab setups.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                <div class="ltn__product-item ltn__product-item-2 text-left">
                    <div class="product-img"><a href="contact.html"><img src="img/carepath/product-3.jpg" alt="Medical Imaging"></a></div>
                    <div class="product-info">
                        <h2 class="product-title"><a href="contact.html">Medical Imaging</a></h2>
                        <p style="font-size:0.85rem;color:#666;margin-top:6px;">Ultrasound, X-ray accessories and imaging consumables.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                <div class="ltn__product-item ltn__product-item-2 text-left">
                    <div class="product-img"><a href="contact.html"><img src="img/carepath/product-4.jpg" alt="Orthopaedic & Surgical"></a></div>
                    <div class="product-info">
                        <h2 class="product-title"><a href="contact.html">Orthopaedic & Surgical</a></h2>
                        <p style="font-size:0.85rem;color:#666;margin-top:6px;">Implants, surgical instruments and theatre supplies.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                <div class="ltn__product-item ltn__product-item-2 text-left">
                    <div class="product-img"><a href="contact.html"><img src="img/carepath/banner-3.jpg" alt="Hospital Furniture"></a></div>
                    <div class="product-info">
                        <h2 class="product-title"><a href="contact.html">Hospital Furniture</a></h2>
                        <p style="font-size:0.85rem;color:#666;margin-top:6px;">Beds, trolleys, emergency furniture and patient-care equipment.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                <div class="ltn__product-item ltn__product-item-2 text-left">
                    <div class="product-img"><a href="contact.html"><img src="img/carepath/banner-1.jpg" alt="General Medical Supplies"></a></div>
                    <div class="product-info">
                        <h2 class="product-title"><a href="contact.html">General Medical Supplies</a></h2>
                        <p style="font-size:0.85rem;color:#666;margin-top:6px;">Everyday clinical consumables and hospital essentials.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                <div class="ltn__product-item ltn__product-item-2 text-left">
                    <div class="product-img"><a href="contact.html"><img src="img/carepath/hero-2.jpg" alt="Diagnostic Devices"></a></div>
                    <div class="product-info">
                        <h2 class="product-title"><a href="contact.html">Diagnostic Devices</a></h2>
                        <p style="font-size:0.85rem;color:#666;margin-top:6px;">Point-of-care devices and laboratory diagnostics.</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                <div class="ltn__product-item ltn__product-item-2 text-left">
                    <div class="product-img"><a href="contact.html"><img src="img/carepath/about.jpg" alt="Healthcare Equipment"></a></div>
                    <div class="product-info">
                        <h2 class="product-title"><a href="contact.html">Healthcare Equipment</a></h2>
                        <p style="font-size:0.85rem;color:#666;margin-top:6px;">Reliable equipment for hospitals, clinics and pharmacies.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- PRODUCT AREA END -->
"""


PARTNERS_BODY = """<!-- PARTNERS INTRO AREA START -->
<div class="ltn__about-us-area pt-115 pb-90">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section-title-area ltn__section-title-2--- text-center mb-50">
                    <h6 class="section-subtitle section-subtitle-2 ltn__secondary-color">Global Manufacturers</h6>
                    <h1 class="section-title">Our Strategic Partners</h1>
                    <p>CarePath collaborates with internationally recognized manufacturers and suppliers to ensure:</p>
                </div>
            </div>
        </div>
        <div class="row justify-content-center mb-50">
            <div class="col-lg-3 col-md-6 col-12 mb-30">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-award"></i></span></div>
                    <div class="ltn__feature-info"><h4>Advanced Medical Technologies</h4></div>
                </div>
            </div>
            <div class="col-lg-3 col-md-6 col-12 mb-30">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-clipboard-check"></i></span></div>
                    <div class="ltn__feature-info"><h4>Regulatory-Compliant Equipment</h4></div>
                </div>
            </div>
            <div class="col-lg-3 col-md-6 col-12 mb-30">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-lightbulb"></i></span></div>
                    <div class="ltn__feature-info"><h4>Continuous Product Innovation</h4></div>
                </div>
            </div>
            <div class="col-lg-3 col-md-6 col-12 mb-30">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-link"></i></span></div>
                    <div class="ltn__feature-info"><h4>Reliable Supply Chains</h4></div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- PARTNERS INTRO AREA END -->

<!-- PARTNERS LOGOS AREA START -->
<div class="ltn__brand-logo-area section-bg-1 pt-115 pb-90">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section-title-area ltn__section-title-2--- text-center mb-50">
                    <h1 class="section-title">Partner Brands</h1>
                </div>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-lg-4 col-md-4 col-sm-6 col-12 mb-30"><div class="partner-logo-card"><h4>BIOBASE</h4></div></div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-12 mb-30"><div class="partner-logo-card"><h4>MEDIGlobal</h4></div></div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-12 mb-30"><div class="partner-logo-card"><h4>Makula</h4></div></div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-12 mb-30"><div class="partner-logo-card"><h4>Seamaty</h4></div></div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-12 mb-30"><div class="partner-logo-card"><h4>Macura</h4></div></div>
            <div class="col-lg-4 col-md-4 col-sm-6 col-12 mb-30"><div class="partner-logo-card"><h4>Mindray</h4></div></div>
        </div>
    </div>
</div>
<!-- PARTNERS LOGOS AREA END -->
"""


CLIENTS_BODY = """<!-- CLIENTS INTRO AREA START -->
<div class="ltn__about-us-area pt-115 pb-90">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section-title-area ltn__section-title-2--- text-center mb-50">
                    <h6 class="section-subtitle section-subtitle-2 ltn__secondary-color">Delivering Precision. Empowering Healthcare. Transforming Lives.</h6>
                    <h1 class="section-title">Our Clients</h1>
                    <p>CarePath proudly serves a diverse range of healthcare and research institutions across Tanzania.</p>
                </div>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-hospital"></i></span></div>
                    <div class="ltn__feature-info"><h4>Government Hospitals</h4></div>
                </div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-hospital-alt"></i></span></div>
                    <div class="ltn__feature-info"><h4>Regional Referral Hospitals</h4></div>
                </div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-clinic-medical"></i></span></div>
                    <div class="ltn__feature-info"><h4>Private Healthcare Institutions</h4></div>
                </div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-vial"></i></span></div>
                    <div class="ltn__feature-info"><h4>Diagnostic Laboratories</h4></div>
                </div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-hands-helping"></i></span></div>
                    <div class="ltn__feature-info"><h4>NGOs & Medical Projects</h4></div>
                </div>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30">
                <div class="ltn__feature-item ltn__feature-item-6 text-center bg-white box-shadow-1">
                    <div class="ltn__feature-icon"><span><i class="fas fa-university"></i></span></div>
                    <div class="ltn__feature-info"><h4>Universities & Research Institutions</h4></div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- CLIENTS INTRO AREA END -->

<!-- CLIENTS LOGOS AREA START -->
<div class="ltn__brand-logo-area section-bg-1 pt-115 pb-90">
    <div class="container">
        <div class="row">
            <div class="col-lg-12">
                <div class="section-title-area ltn__section-title-2--- text-center mb-50">
                    <h1 class="section-title">Client Institutions</h1>
                </div>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30"><div class="client-logo-card"><h4>NIMR</h4><small>National Institute for Medical Research</small></div></div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30"><div class="client-logo-card"><h4>UDOM</h4><small>The University of Dodoma</small></div></div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30"><div class="client-logo-card"><h4>NCAA</h4><small>Ngorongoro Conservation Area Authority</small></div></div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30"><div class="client-logo-card"><h4>Hach</h4><small>Be Right</small></div></div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30"><div class="client-logo-card"><h4>TANESCO</h4></div></div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30"><div class="client-logo-card"><h4>UNDP</h4><small>United Nations Development Programme</small></div></div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30"><div class="client-logo-card"><h4>Mantra Tanzania Limited</h4></div></div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30"><div class="client-logo-card"><h4>Eppendorf</h4></div></div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30"><div class="client-logo-card"><h4>Plan International</h4></div></div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30"><div class="client-logo-card"><h4>GE Whatman</h4></div></div>
            <div class="col-lg-3 col-md-4 col-sm-6 col-12 mb-30"><div class="client-logo-card"><h4>HJFMRI</h4></div></div>
        </div>
    </div>
</div>
<!-- CLIENTS LOGOS AREA END -->
"""


CONTACT_BODY = """<!-- CONTACT ADDRESS AREA START -->
<div class="ltn__contact-address-area mb-90 mt-90">
    <div class="container">
        <div class="row">
            <div class="col-lg-4">
                <div class="ltn__contact-address-item ltn__contact-address-item-3 box-shadow">
                    <div class="ltn__contact-address-icon"><i class="icon-mail" style="font-size:2rem;color:var(--carepath-turquoise)"></i></div>
                    <h3>Email Address</h3>
                    <p><a href="mailto:info@carepath.co.tz">info@carepath.co.tz</a></p>
                </div>
            </div>
            <div class="col-lg-4">
                <div class="ltn__contact-address-item ltn__contact-address-item-3 box-shadow">
                    <div class="ltn__contact-address-icon"><i class="icon-call" style="font-size:2rem;color:var(--carepath-turquoise)"></i></div>
                    <h3>Phone Number</h3>
                    <p><a href="tel:+255719902445">+255 719 902 445</a><br><a href="tel:0719902445">0719 902 445</a></p>
                </div>
            </div>
            <div class="col-lg-4">
                <div class="ltn__contact-address-item ltn__contact-address-item-3 box-shadow">
                    <div class="ltn__contact-address-icon"><i class="icon-placeholder" style="font-size:2rem;color:var(--carepath-turquoise)"></i></div>
                    <h3>Office Address</h3>
                    <p>Wikicha Tower, Mikocheni<br>Mwai Kibaki Road, Dar es Salaam, Tanzania</p>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- CONTACT ADDRESS AREA END -->

<!-- CONTACT MESSAGE AREA START -->
<div class="ltn__contact-message-area mb-120 mb--100">
    <div class="container">
        <div class="row">
            <div class="col-lg-8">
                <div class="ltn__form-box contact-form-box box-shadow white-bg">
                    <h4 class="title-2">Send Us a Message</h4>
                    <form id="contact-form" action="mail.php" method="post">
                        <div class="row">
                            <div class="col-md-6">
                                <div class="input-item input-item-name ltn__custom-icon">
                                    <input type="text" name="name" placeholder="Your Name" required>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="input-item input-item-email ltn__custom-icon">
                                    <input type="email" name="email" placeholder="Your Email" required>
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="input-item input-item-phone ltn__custom-icon">
                                    <input type="text" name="phone" placeholder="Phone Number">
                                </div>
                            </div>
                            <div class="col-md-6">
                                <div class="input-item input-item-subject ltn__custom-icon">
                                    <input type="text" name="subject" placeholder="Subject">
                                </div>
                            </div>
                        </div>
                        <div class="input-item input-item-textarea ltn__custom-icon">
                            <textarea name="message" placeholder="Your message" rows="6" required></textarea>
                        </div>
                        <div class="btn-wrapper mt-0">
                            <button class="btn theme-btn-1 btn-effect-1" type="submit">Send Message</button>
                        </div>
                    </form>
                </div>
            </div>
            <div class="col-lg-4">
                <div class="ltn__contact-address-item ltn__contact-address-item-3 box-shadow white-bg p-30">
                    <h3 class="mb-20">Banking Details</h3>
                    <table class="table table-borderless">
                        <tr><td><strong>Bank</strong></td><td>NMB Bank</td></tr>
                        <tr><td><strong>Branch</strong></td><td>Mlimani City</td></tr>
                        <tr><td><strong>Account Name</strong></td><td>CAREPATH COMPANY LIMITED</td></tr>
                        <tr><td><strong>Account Number</strong></td><td>22510130502</td></tr>
                    </table>
                    <hr>
                    <h3 class="mb-20 mt-30">Website</h3>
                    <p><a href="http://carepath.co.tz/" target="_blank">carepath.co.tz</a></p>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- CONTACT MESSAGE AREA END -->
"""


PAGES = [
    ("index.html", "Home", INDEX_BODY, False, ""),
    ("about.html", "About Us", ABOUT_BODY, True, "About Us"),
    ("services.html", "Our Services", SERVICES_BODY, True, "Our Services"),
    ("products.html", "Products", PRODUCTS_BODY, True, "Products"),
    ("partners.html", "Strategic Partners", PARTNERS_BODY, True, "Strategic Partners"),
    ("clients.html", "Our Clients", CLIENTS_BODY, True, "Our Clients"),
    ("contact.html", "Contact Us", CONTACT_BODY, True, "Contact Us"),
]


if __name__ == "__main__":
    for filename, title, body, use_bc, bc_title in PAGES:
        html = wrap_page(title, body, include_breadcrumb=use_bc, breadcrumb_title=bc_title)
        (BASE / filename).write_text(html, encoding="utf-8")
        print(f"Generated {filename}")
