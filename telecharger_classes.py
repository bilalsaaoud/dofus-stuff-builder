"""
Script pour télécharger les images des classes Dofus.
Lance ce fichier UNE SEULE FOIS via lancer_download.bat, puis recharge l'app.
Les images sont sauvegardées dans images/classes/{id}.png
"""

import urllib.request
import urllib.error
import os
import time

CLASSES = [
    (1,  'feca',       'Féca'),
    (2,  'osamodas',   'Osamodas'),
    (3,  'enutrof',    'Enutrof'),
    (4,  'sram',       'Sram'),
    (5,  'xelor',      'Xélor'),
    (6,  'ecaflip',    'Ecaflip'),
    (7,  'eniripsa',   'Éniripsa'),
    (8,  'iop',        'Iop'),
    (9,  'cra',        'Crâ'),
    (10, 'sadida',     'Sadida'),
    (11, 'sacrieur',   'Sacrieur'),
    (12, 'pandawa',    'Pandawa'),
    (13, 'roublard',   'Roublard'),
    (14, 'zobal',      'Zobal'),
    (15, 'steamer',    'Steamer'),
    (16, 'eliotrope',  'Éliotrope'),
    (17, 'huppermage', 'Huppermage'),
    (18, 'ouginak',    'Ouginak'),
    (20, 'forgelance', 'Forgelance'),
]

def get_urls(cls_id, slug):
    """URLs à tester dans l'ordre — du plus fiable au moins fiable."""
    return [
        # ① Barbofus Unity — portraits HD (tête + buste, style 3D Dofus)
        f"https://barbofus.com/storage/images/icons/classes/faces/unity/{cls_id*10}_1.png",
        f"https://barbofus.com/storage/images/icons/classes/faces/unity/{cls_id*10}_0.png",
        # ② Barbofus ghost — silhouette full-body
        f"https://barbofus.com/storage/images/icons/classes/ghost/{cls_id}.png",
        # ③ Ankama CDN (peut ne pas répondre)
        f"https://static.ankama.com/dofus/www/game/classes/thumbnails/{cls_id}/male.png",
        f"https://static.ankama.com/dofus/www/game/classes/faces/200/{cls_id}.png",
        f"https://static.ankama.com/dofus/ankama/dofus/artworks/classes/{cls_id}_male.png",
        f"https://static.ankama.com/dofus/www/game/classes/{cls_id}_male.png",
    ]

folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "classes")
os.makedirs(folder, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
    'Referer': 'https://barbofus.com/',
}

ok = 0
fail = []

print("=" * 50)
print("  Téléchargement images personnages Dofus")
print("=" * 50)

for cls_id, slug, name in CLASSES:
    dest = os.path.join(folder, f"{cls_id}.png")
    if os.path.exists(dest) and os.path.getsize(dest) > 2000:
        print(f"  ✓ {name} déjà téléchargé ({os.path.getsize(dest)//1024} Ko)")
        ok += 1
        continue

    downloaded = False
    for url in get_urls(cls_id, slug):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                if len(data) > 2000:  # vraie image (pas une erreur 404 HTML)
                    with open(dest, 'wb') as f:
                        f.write(data)
                    source = url.split('/')[2]  # domaine
                    print(f"  ✓ {name} ({len(data)//1024} Ko) ← {source}")
                    downloaded = True
                    ok += 1
                    break
        except urllib.error.HTTPError as e:
            continue
        except Exception:
            continue

    if not downloaded:
        print(f"  ✗ {name} → aucune URL disponible (fallback SVG dans l'app)")
        fail.append(name)

    time.sleep(0.15)  # respecter les serveurs

print()
print(f"{'='*50}")
print(f"  ✓ {ok}/{len(CLASSES)} classes téléchargées")
if fail:
    print(f"  ✗ Manquantes : {', '.join(fail)}")
    print("    → Ces classes utiliseront l'avatar SVG coloré")
print(f"{'='*50}")
print()
print("➜  Recharge l'app dans le navigateur (F5) !")
print()
