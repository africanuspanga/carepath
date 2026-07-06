#!/usr/bin/env python3
"""
Process the 11 stock images provided for CarePath and wire them into the site.
"""
import os
import shutil
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "new-images"
SITE_DIR = ROOT / "vicodin"
TARGET_DIR = SITE_DIR / "img" / "carepath"

# Ensure target dir exists
TARGET_DIR.mkdir(parents=True, exist_ok=True)

# Clean mapping from source filename -> (dest_name, max_width, max_height, crop_to_fill)
# crop_to_fill=True means crop to exact (max_width x max_height) from center.
# crop_to_fill=False means fit within box preserving aspect ratio.
IMAGE_PLAN = {
    "Modern hospital operating room Africa.jpg":      ("hero-1.jpg", 1920, 900, True),
    "Diagnostic medical devices laboratory.jpg":      ("hero-2.jpg", 1920, 900, True),
    "Healthcare worker using medical equipment.jpg":  ("about.jpg", 600, 800, False),
    "Medical equipment supply warehouse.jpg":         ("services.jpg", 800, 1031, False),
    "African hospital clinic medical supplies.jpg":   ("banner-1.jpg", 740, 882, True),
    "Medical equipment supply.jpg":                   ("banner-2.jpg", 540, 688, True),
    "Hospital bed emergency trolley furniture.jpg":   ("banner-3.jpg", 740, 882, True),
    "Hospital ICU ventilator monitor equipment.jpg":  ("product-1.jpg", 600, 700, True),
    "Medical laboratory microscope analyser.jpg":     ("product-2.jpg", 600, 700, True),
    "Ultrasound machine medical imaging.jpg":         ("product-3.jpg", 600, 700, True),
    "Orthopaedic surgery implant instruments.jpg":    ("product-4.jpg", 600, 700, True),
}

PRODUCT_CARDS = [
    ("img/carepath/product-1.jpg", "ICU & Critical Care", "Ventilators, patient monitors, infusion pumps and critical-care solutions."),
    ("img/carepath/product-2.jpg", "Laboratory Diagnostics", "Microscopes, analysers, reagents and complete lab setups."),
    ("img/carepath/product-3.jpg", "Medical Imaging", "Ultrasound, X-ray accessories and imaging consumables."),
    ("img/carepath/product-4.jpg", "Orthopaedic & Surgical", "Implants, surgical instruments and theatre supplies."),
    ("img/carepath/banner-3.jpg", "Hospital Furniture", "Beds, trolleys, emergency furniture and patient-care equipment."),
    ("img/carepath/banner-1.jpg", "General Medical Supplies", "Everyday clinical consumables and hospital essentials."),
    ("img/carepath/hero-2.jpg", "Diagnostic Devices", "Point-of-care devices and laboratory diagnostics."),
    ("img/carepath/about.jpg", "Healthcare Equipment", "Reliable equipment for hospitals, clinics and pharmacies."),
]


def process_image(src_path: Path, dest_name: str, max_w: int, max_h: int, crop: bool):
    img = Image.open(src_path)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    if crop:
        # Resize so it covers the box, then crop center
        src_w, src_h = img.size
        ratio = max(max_w / src_w, max_h / src_h)
        new_w = int(src_w * ratio)
        new_h = int(src_h * ratio)
        img = img.resize((new_w, new_h), Image.LANCZOS)
        left = (new_w - max_w) // 2
        top = (new_h - max_h) // 2
        img = img.crop((left, top, left + max_w, top + max_h))
    else:
        img.thumbnail((max_w, max_h), Image.LANCZOS)

    dest_path = TARGET_DIR / dest_name
    img.save(dest_path, "JPEG", quality=85, optimize=True)
    print(f"Saved {dest_path} ({img.size[0]}x{img.size[1]})")


def process_all_images():
    for src_name, (dest_name, w, h, crop) in IMAGE_PLAN.items():
        src_path = SOURCE_DIR / src_name
        if not src_path.exists():
            raise FileNotFoundError(f"Missing source image: {src_path}")
        process_image(src_path, dest_name, w, h, crop)


def update_generator():
    gen_path = SITE_DIR / "generate_carepath.py"
    text = gen_path.read_text()

    # Slider backgrounds
    text = text.replace('data-bs-bg="img/slider/13.jpg"', 'data-bs-bg="img/carepath/hero-1.jpg"')
    text = text.replace('data-bs-bg="img/slider/11.jpg"', 'data-bs-bg="img/carepath/hero-2.jpg"')

    # About / services images
    text = text.replace('src="img/others/9.png" alt="Medical Equipment"', 'src="img/carepath/about.jpg" alt="Medical Equipment"')
    text = text.replace('src="img/others/9.png" alt="About CarePath"', 'src="img/carepath/about.jpg" alt="About CarePath"')
    text = text.replace('src="img/service/11.jpg" alt="Our Services"', 'src="img/carepath/services.jpg" alt="Our Services"')

    # Home banners (5 slots)
    text = text.replace('src="img/banner/1.jpg" alt="Banner Image"', 'src="img/carepath/banner-1.jpg" alt="Banner Image"')
    text = text.replace('src="img/banner/2.jpg" alt="Banner Image"', 'src="img/carepath/banner-2.jpg" alt="Banner Image"')
    text = text.replace('src="img/banner/3.jpg" alt="Banner Image"', 'src="img/carepath/banner-3.jpg" alt="Banner Image"')
    text = text.replace('src="img/banner/11.jpg" alt="Banner Image"', 'src="img/carepath/banner-2.jpg" alt="Banner Image"')
    text = text.replace('src="img/banner/12.jpg" alt="Banner Image"', 'src="img/carepath/banner-1.jpg" alt="Banner Image"')

    # Home featured products (8 cards) - replace images, alt text and titles
    HOME_FEATURED = PRODUCT_CARDS[:8]
    old_template_titles = [
        "Antiseptic Spray",
        "Digital Stethoscope",
        "Cosmetic Containers",
        "Thermometer Gun",
        "Blue Hand Gloves",
        "Medical Mask",
        "Hand Sanitizer",
        "First Aid Kit",
    ]
    for old_title, (img_path, new_title, desc) in zip(old_template_titles, HOME_FEATURED):
        text = text.replace(f'alt="{old_title}"', f'alt="{new_title}"')
        text = text.replace(f'">{old_title}</a>', f'">{new_title}</a>')
        # Also catch the img src if still on a template path
        text = text.replace(f'alt="{new_title}"></a>', f'alt="{new_title}"></a>')  # no-op marker
        # Replace the preceding product image src in the same card by finding the template img/product/X.png right before the old alt
        # We do this via a targeted regex replacement for the home section only.

    # Use regex to replace the src path inside the home featured-product cards only (between the opening of the home grid and the closing </div> of the section)
    import re
    home_section_start = '<div class="row ltn__tab-product-slider-one-active--- slick-arrow-1">'
    home_section_end = '<div class="col-lg-12 text-center mt-30">'
    hs = text.find(home_section_start)
    he = text.find(home_section_end, hs)
    if hs != -1 and he != -1:
        home_section = text[hs:he]
        for i, (img_path, title, desc) in enumerate(HOME_FEATURED, start=1):
            home_section = home_section.replace(f'img/product/{i}.png', img_path)
        text = text[:hs] + home_section + text[he:]

    # Products page: replace entire product grid with 8 real cards
    start_marker = 'PRODUCTS_BODY = """<!-- PRODUCT AREA START -->'
    end_marker = '<!-- PRODUCT AREA END -->\n"""'
    start = text.find(start_marker)
    end = text.find(end_marker)
    if start == -1 or end == -1:
        print(f"WARNING: Could not locate PRODUCTS_BODY block (start={start}, end={end})")
    else:
        end += len(end_marker)
        product_cards_html = ""
        for img_path, title, desc in PRODUCT_CARDS:
            product_cards_html += f'''            <div class="col-lg-3 col-md-4 col-sm-6 col-6">
                <div class="ltn__product-item ltn__product-item-2 text-left">
                    <div class="product-img"><a href="contact.html"><img src="{img_path}" alt="{title}"></a></div>
                    <div class="product-info">
                        <h2 class="product-title"><a href="contact.html">{title}</a></h2>
                        <p style="font-size:0.85rem;color:#666;margin-top:6px;">{desc}</p>
                    </div>
                </div>
            </div>
'''

        new_body = f'''{start_marker}
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
{product_cards_html}        </div>
    </div>
</div>
{end_marker}'''
        text = text[:start] + new_body + text[end:]

    gen_path.write_text(text)
    print(f"Updated {gen_path}")


def regenerate_site():
    import subprocess
    result = subprocess.run(
        ["python3", "generate_carepath.py"],
        cwd=SITE_DIR,
        capture_output=True,
        text=True,
    )
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError("Site regeneration failed")


def main():
    print("Processing stock images...")
    process_all_images()
    print("\nUpdating generator...")
    update_generator()
    print("\nRegenerating HTML pages...")
    regenerate_site()
    print("\nDone.")


if __name__ == "__main__":
    main()
