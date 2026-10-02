#!/usr/bin/env python3
"""Replace visible copy in the copied Ecomuz template. Structure stays."""
from pathlib import Path
import re
import subprocess

ROOT = Path("/Users/humbertoalonso/Website Exports/symart")

# Longest strings first.
LONG = [
    ("Furniture that turns a house into a calm, modern home you’ll love coming back to every single day",
     "Diseñamos, fabricamos e instalamos mobiliario corporativo en Aguascalientes, a tu medida."),
    ("Furniture that turns a house into a calm, modern home you'll love coming back to every single day",
     "Diseñamos, fabricamos e instalamos mobiliario corporativo en Aguascalientes, a tu medida."),
    ("Explore Ecomuz's curated collections of modern furniture designed to bring warmth and comfort to every room.",
     "Symart diseña, fabrica e instala muebles de oficina a tu medida en Aguascalientes."),
    ("Explore Ecomuz’s curated collections of modern furniture designed to bring warmth and comfort to every room.",
     "Symart diseña, fabrica e instala muebles de oficina a tu medida en Aguascalientes."),
    ("Stylish, functional furniture created to bring warmth and comfort to your home.",
     "Mobiliario de oficina fabricado en Aguascalientes, con garantía de 5 años."),
    ("Stylish, Functional Furniture for Your Home",
     "Muebles de oficina a tu medida"),
    ("Modern Furniture for Warm, Functional Living",
     "Muebles de oficina a tu medida"),
    ("A refined living space where timeless minimalism meets contemporary craftsmanship. Maison Madeleine celebrates warm natural tones, sculptural forms, and carefully balanced proportions to create an inviting atmosphere of understated luxury.",
     "Escritorios, estaciones y archivo fabricados en casa para oficinas que reciben clientes. Un solo equipo diseña, fabrica e instala."),
    ("Designed around simplicity and function, Élan Dining transforms the dining experience through clean architectural lines, premium materials, and a calming neutral palette that encourages effortless everyday living.",
     "Estaciones de trabajo que ordenan el puesto, ocultan cables y aguantan el uso diario. Módulos individuales o para cuatro personas."),
    ("A sophisticated wall cabinet collection that blends seamless storage with modern aesthetics. Atelier Wall showcases precision detailing, floating forms, and elegant finishes that elevate contemporary interiors without overwhelming the space.",
     "Archiveros, credenzas, libreros y flippers en los mismos acabados del escritorio. El color del catálogo no cambia el precio."),
    ("Fast and free shipping on every order that you make today.",
     "Cinco años contra defectos de fabricación, en sillas y en muebles."),
    ("We stock only the finest items that you will always trust.",
     "Fabricamos en Aguascalientes y controlamos calidad, tiempos y acabados."),
    ("Our friendly team is always here to help you, at any time.",
     "Cotizamos en menos de 24 horas, con planos o con una visita."),
    ("Track every order in real time, from checkout to delivery.",
     "En Aguascalientes la entrega y la instalación van incluidas."),
    ("Discover nearby furniture stores with real-time location access.",
     "Hablas directo con el taller. Teléfono y WhatsApp +52 449 915 0678."),
    ("Explore our best collections for smart shopping",
     "Líneas de oficina fabricadas para el uso diario"),
    ("Explore more products crafted just for your needs",
     "Cuéntanos el proyecto y te respondemos en menos de 24 horas"),
    ("Available mobile app", "Garantía de 5 años"),
    ("Picky brands look book", "Proyectos que ya entregamos"),
    ("One & only trusted point", "Un solo proveedor"),
    ("Hand-picked items", "Lo más pedido"),
    ("Trendy collection", "Líneas de catálogo"),
    ("Why choose us?", "Por qué Symart"),
    ("Free shipping", "Garantía 5 años"),
    ("Best quality items", "Fabricación propia"),
    ("24/7 support", "Respuesta en 24 h"),
    ("Order tracking", "Instalación incluida"),
    ("main store location", "Taller en Aguascalientes"),
    ("Get in touch", "Contacto"),
    ("Instagram feed", "Proyectos"),
    ("Maison Madeleine", "Corporativos"),
    ("Élan Dining", "Estaciones"),
    ("Atelier Wall", "Almacenamiento"),
    ("Designed for", "Muebles de"),
    ("modern living", "oficina a medida"),
    ("Shop now", "Ver catálogo"),
    ("Shop Now", "Ver catálogo"),
    ("View All", "Ver todo"),
    ("All Products", "Ver todo"),
    ("Rubber lounge armchair", "Silla Acusta 30"),
    ("Nova Edge Sofa", "Escritorio recto OG"),
    ("Lumen Arc Coffee Table", "Escritorio en L OGL"),
    ("Woodpeak Dining Set", "Estación 4 personas"),
    ("Woodaxis Office Chair", "Silla Lake 20"),
    ("Heritage Craft Dresser", "Credenza"),
    ("Urban Oak Side Chair", "Silla Arezzo"),
    ("Oaklyn Dining Chair", "Silla Staff"),
    ("Maplewood Armchair", "Silla Acusta 10"),
    ("Woodspan Bookshelf", "Librero"),
    ("Woodspire King Bed", "Escritorio OCE"),
    ("Forge Square Stool", "Archivero metálico"),
    ("Forestline Wardrobe", "Flipper"),
    ("Forestcraft Rocking Chair", "Silla Sling Negro"),
    ("Ironleaf Sideboard", "Archivero"),
    ("Rustwood Corner Shelf", "Estación individual"),
    ("Rustline Bed Frame", "Mesa de juntas"),
    ("Rustline Chair Frame", "Mesa de juntas"),
    ("Timberlux Nightstand", "Estación con cajones"),
    ("Vista Sliding Door", "Recepción"),
    ("Ridge Dining Table", "Escritorio OCG"),
    ("Crestwood Dining Chair", "Silla operativa"),
    ("info@ecomuz.com", "ventas@symart.com.mx"),
    ("+123 455 677 99-4", "+52 449 915 0678"),
    ("+31 (0)38 - 760 1750", "+52 449 915 0678"),
    ("+31 (0)20 - 354 0259", "+52 449 915 0678"),
    ("1/A, Booston Tower, NYC", "Aguascalientes, México"),
    ("Hanzelaan 351 8017", "Área de servicio"),
    ("JM Zwolle Netherlands", "Sin showroom público"),
    ("Moermanskkade 313 1013 BC Amsterdam", "Cotización en menos de 24 horas"),
    ("Fontes Pereira de Melo  14/Lisboa Portugal", "Fabricación e instalación"),
    ("Fontes Pereira de Melo 14/Lisboa Portugal", "Fabricación e instalación"),
    ("Ecomuz Zwolle", "Symart ventas"),
    ("Ecomuz Amsterdam", "Symart taller"),
    ("Ecomuz Lisbon", "Symart obra"),
    ("@Ecomuz", "@symartmuebles"),
    ("Copyright & design by @symartmuebles - 2026", "© 2026 Symart. Muebles de oficina a tu medida."),
    ("Business email", "Correo de trabajo"),
    ("Subscribe", "Enviar"),
    ("Shipping & Returns", "Envíos"),
    ("Terms & Conditions", "Términos"),
    ("Privacy Policy", "Privacidad"),
    ("About us", "El taller"),
    ("Our Mission", "Lo que hacemos"),
    ("Our Vision", "Cómo trabajamos"),
    ("Need Help?", "¿Hablamos?"),
    ("We're Here to Help", "Cotiza tu espacio"),
    ("Get In Touch", "Escríbenos"),
    ("Frequently Asked Question", "Preguntas frecuentes"),
    ("How do I track my order?", "¿Cuánto tarda un proyecto?"),
    ("How long does delivery take?", "¿Cotizan sin planos?"),
    ("Can I return or exchange a product?", "¿El color cambia el precio?"),
    ("What payment methods do you accept?", "¿Los muebles tienen garantía?"),
    ("Search by product", "Busca por código"),
    ("Related product", "Complementos"),
    ("Select Quantity", "Cantidad"),
    ("Add to cart", "Agregar"),
    ("Add To Cart", "Agregar"),
    ("Buy Now", "Cotizar"),
    ("Featured products", "Destacados"),
    ("Shop favorites", "Lo más pedido"),
    ("Customer favorites", "Clientes"),
    ("Trending now", "En existencia"),
    ("Exclusive deals", "Sobre pedido"),
    ("New, Seating", "Sillas"),
    ("Picky, Seating", "Ejecutivas"),
    ("Bedroom, New", "Escritorios"),
    ("Storage, Trendy", "Archivo"),
    ("Featured, Storage", "Archivo"),
    ("Lighting, Picky", "Estaciones"),
    ("Lighting, Trendy", "Estaciones"),
    ("Lighting, New, Trendy", "Estaciones"),
    ("Decor, Featured, New", "Recepción"),
    ("New, Picky, Seating", "Sillas"),
    ("Bedroom, Trendy", "Escritorios"),
    ("Featured, Lighting", "Mesas"),
    ("50 Oxford Street", "Aguascalientes"),
    ("221B Baker Street", "México"),
    ("1421 Union Avenue", "Taller Symart"),
    ("London NW1 6XE, UK", "Aguascalientes, México"),
    ("Coppell, Virginia", "Aguascalientes"),
    ("Frankfurt, Germany", "México"),
    ("How to Choose the Perfect Sofa for Your Living Room", "Cómo elegir una silla con respaldo"),
    ("Ergonomic Home Office Setups for Remote Workers", "Cómo equipar un puesto de trabajo"),
    ("10 Small-Space Furniture Ideas That Actually Work", "Cómo aprovechar cada metro de oficina"),
    ("Bedroom Storage Solutions for a Clutter-Free Space", "Archivo que mantiene la oficina en orden"),
    ("How Lighting Transforms the Feel of a Room", "Qué exige la Ley Silla"),
    ("Mixing Modern and Vintage Furniture Like a Pro", "Color de catálogo, mismo precio"),
    ("Sustainable Furniture: What to Look For When Buying", "Qué revisar antes de equipar una oficina"),
    ("The Ultimate Guide to Caring for Leather Furniture", "Cuidado de sillas y cubiertas de melamina"),
    ("Understanding Wood Types: Oak, Walnut and Beyond", "Melamina, estructura y acabados Symart"),
    ("Browse the full Ecomuz catalog of modern, handcrafted furniture for living, dining, and workspaces.",
     "Escritorios, sillas, estaciones, archivo, mesas y recepciones fabricados por Symart."),
    ("Questions? Concerns? Let’s make your shopping experience seamless and enjoyable.",
     "¿Tienes un proyecto? Cotización en menos de 24 horas. +52 449 915 0678."),
    ("Questions? Concerns? Let's make your shopping experience seamless and enjoyable.",
     "¿Tienes un proyecto? Cotización en menos de 24 horas. +52 449 915 0678."),
    ("Discover handpicked products made just for you.",
     "Mobiliario de oficina fabricado a tu medida."),
    ("Stories, updates, and inspirations from our shop to you.",
     "Guías para equipar oficinas, aulas y espacios de atención."),
    ("Shop Furniture — Ecomuz", "Catálogo — Symart"),
    ("Shop Furniture \u2014 Ecomuz", "Catálogo — Symart"),
]
SHORT = {
    "Home": "Inicio",
    "Shop": "Productos",
    "About": "Conócenos",
    "Support": "Contacto",
    "Blog": "Blog",
    "Ecomuz": "Symart",
}

def apply(text: str) -> str:
    for old, new in LONG:
        text = text.replace(old, new)
    for old, new in SHORT.items():
        text = text.replace(f">{old}<", f">{new}<")
        text = text.replace(f'children:"{old}"', f'children:"{new}"')
        text = text.replace(f'uXUSpLfOL:"{old}"', f'uXUSpLfOL:"{new}"')
        text = text.replace(f'alt:"{old} emblem"', f'alt:"{new} emblem"')
        text = text.replace(f'displayName:"{old}"', f'displayName:"{new}"')
    # leftover brand inside sentences already partly rewritten
    text = text.replace("Ecomuz", "Symart")
    text = text.replace("ecomuz.com", "symart.com.mx")
    return text

def main():
    files = list(ROOT.glob("*.html")) + [ROOT/"assets/site.js"]
    for path in files:
        raw = path.read_text(encoding="utf-8", errors="ignore")
        updated = apply(raw)
        if updated != raw:
            path.write_text(updated, encoding="utf-8")
            print("text", path.name)
    swap_images()

def dims(path: Path):
    out = subprocess.check_output(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)], text=True)
    w = int(re.search(r"pixelWidth: (\d+)", out).group(1))
    h = int(re.search(r"pixelHeight: (\d+)", out).group(1))
    return w, h

def swap_images():
    src_dir = Path("/Users/humbertoalonso/Website Exports/ecomuz.framer.ai/images/symart")
    sources = [
        "hero.webp", "og.webp", "ogl.webp", "ocg.webp", "oce.webp",
        "estacion-2.webp", "estacion-4.webp", "almacen.webp", "sillas-2.webp",
        "variedad.webp", "calidad.webp", "oficina.webp", "espacio-2.png",
        "espacio-1.png", "espacio-3.png", "espacio-4.png", "proceso.png",
        "sillas.webp", "operativas.webp", "resistentes.webp", "estacion-1.webp",
        "estacion-3.webp", "almacen-2.webp", "mantenimiento.webp",
    ]
    sources = [src_dir/name for name in sources if (src_dir/name).exists()]
    groups = {}
    for path in (ROOT/"images").iterdir():
        if path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
            continue
        if path.stat().st_size < 30000:
            continue
        base = re.sub(r"-[0-9a-f]{6,}(?=\.(png|jpe?g|webp)$)", "", path.name, flags=re.I)
        groups.setdefault(base, []).append(path)
    ordered = sorted(groups.items(), key=lambda kv: max(p.stat().st_size for p in kv[1]), reverse=True)
    done = 0
    for i, (base, paths) in enumerate(ordered):
        source = sources[i % len(sources)]
        for path in paths:
            try:
                w, h = dims(path)
            except Exception:
                continue
            fmt = "jpeg" if path.suffix.lower() in {".jpg", ".jpeg"} else "png"
            subprocess.run(
                ["sips", "-s", "format", fmt, "-z", str(h), str(w), str(source), "--out", str(path)],
                check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            done += 1
    # favicon
    icon = ROOT/"images/DzlQrsbVn6Eqmyo37bxYOKx0cg.png"
    logo = src_dir/"logo.webp"
    if icon.exists() and logo.exists():
        w, h = dims(icon)
        subprocess.run(
            ["sips", "-s", "format", "png", "-z", str(max(h, 32)), str(max(w, 32)), str(logo), "--out", str(icon)],
            check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    print("images rewritten", done, "groups", len(ordered))

if __name__ == "__main__":
    main()
