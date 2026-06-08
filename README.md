# 🎮 Dofus Stuff Builder

**Outil de création de build pour Dofus 3** — application web single-page, sans dépendances, vanilla JS.

> Projet portfolio développé à destination d'Ankama Games.

---

## ✨ Fonctionnalités

### Personnage
- Sélection de classe parmi les **18 classes Dofus** avec portrait officiel
- Couleurs de thème dynamiques par classe
- Portrait en fallback avatar si image indisponible

### Équipement
- **Paperdoll complet** : Chapeau, Amulette, Cape, Ceinture, 2 Anneaux, Bottes, Arme, Arme 2, Bouclier, Familier
- **6 slots Dofus / Trophée / Objet vivant**
- Slot Monture dédié
- **Drag & drop** des items de la grille vers les slots
- Animations de slot (flash doré à l'équipement, shake si incompatible)

### Grille d'items
- Données en temps réel depuis l'**API DofusDude** (dofus3/v1/fr)
- Recherche textuelle instantanée
- Filtres par type d'item, par classe, par niveau (min/max)
- Tri par niveau ↓, niveau ↑, ou A–Z
- Mini-stats affichées directement sur la carte

### Stats & Analyse
- **Panneau stats cumulées** : toutes les caractéristiques additionnées
- **Points de Vie** = 55 base + Vitalité × 5 avec barre visuelle
- **PA / PM totaux** = base (6/3) + bonus équipés
- **Résistances visuelles** : 5 barres colorées par élément (Feu, Eau, Terre, Air, Neutre)
- **Bonus de panoplie** : détection automatique des sets équipés, affichage des bonus par palier
- **Kamas tracker** : estimation du coût total du build (saisie manuelle par item)

### Modales & UX
- **Modal détail item** : stats complètes, niveau, type, bouton équiper/retirer
- **Comparaison d'items** : Shift+clic sur 2 cartes → tableau côte à côte avec diff colorée
- **Tooltip au survol** des slots équipés (stats principales sans ouvrir la modal)

### Builds
- **Sauvegarde locale** (localStorage) du build actif
- **Gestionnaire de builds** : jusqu'à 6 builds nommés, chargement en 1 clic
- **Export URL** : lien partageable encodé en base64 (hash URL)
- **Import URL** : reconstruction automatique du build depuis un lien partagé
- **Renommage** du build (double-clic sur le nom)
- **Reset** complet du build
- **Export PNG** : capture du layout complet en haute résolution (×2)

---

## 🚀 Lancement

Aucune dépendance, aucun build step requis :

```bash
# Ouvrir directement dans le navigateur
open index.html

# Ou via serveur local (recommandé pour CORS)
npx serve .
python -m http.server 8080
```

---

## 🔌 API

- **Items & équipements** : `https://api.dofusdu.de/dofus3/v1/fr/items/equipment`
- **Montures** : `https://api.dofusdu.de/dofus3/v1/fr/mounts`
- **Sets / Panoplies** : `https://api.dofusdu.de/dofus3/v1/fr/sets`
- **Portraits de classes** : `https://barbofus.com/storage/images/icons/classes/faces/unity/{id*10}_1.png`

---

## 🗂 Structure

```
dofus-stuff-builder/
├── index.html              # Application complète (HTML + CSS + JS)
├── images/
│   └── classes/            # Portraits des 18 classes (PNG 128×128)
├── telecharger_classes.py  # Script de téléchargement des portraits
└── README.md
```

---

## 🛠 Stack technique

- **Vanilla JS** (ES2022) — aucun framework
- **CSS custom properties** — thème dynamique par classe
- **HTML5 Drag & Drop API** — glisser-déposer natif
- **LocalStorage** — persistance des builds
- **html2canvas** — export image (CDN)
- **Google Fonts** — Cinzel (titres), Lato (texte)

---

## 📸 Aperçu

![Dofus Stuff Builder](preview.png)

---

## 👤 Auteur

**Bilal** — Portfolio Ankama Games  
`bilal123saaoud@gmail.com`
