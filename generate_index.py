#!/usr/bin/env python3
"""
Génère automatiquement index.md pour MkDocs Material
avec le nombre de fichiers Markdown dans chaque sous-dossier.
"""

import os

ROOT = "./docs"  # dossier docs
OUTPUT = os.path.join(ROOT, "index.md")

# Sections et sous-dossiers
SECTIONS = {
    "DevOps": ["python", "c", "web", "git", "docker"],
    "Réseaux & Interfaces": ["reseaux", "interfaces"],
    "Systèmes exploitation": ["windows", "gnu_linux"]
}

# Labels Material pour chaque sous-dossier
LABELS = {
    "python": ":material-language-python: [Guide Python]",
    "c": ":material-language-cpp: [Guide C]",
    "web": ":material-web: [HTML/CSS/JS]",
    "git": ":material-github: [Git & GitHub]",
    "docker": ":material-docker: [Docker]",
    "reseaux": ":material-network: [Réseaux TCP/IP]",
    "interfaces": ":material-connection: [Interfaces et Protocoles de Communication]",
    "windows": ":material-microsoft-windows: [Windows]",
    "gnu_linux": ":material-linux: [GNU/Linux]"
}

def count_md_files(path):
    if not os.path.isdir(path):
        return 0
    return len([f for f in os.listdir(path) if f.endswith(".md")])

lines = ["---", "hide:", "  - navigation", "  - toc", "---", "", "# Accueil", ""]

for section, subfolders in SECTIONS.items():
    lines.append(f"## {section}")
    for folder in subfolders:
        # Calculer le chemin complet selon la hiérarchie
        if section == "DevOps":
            full_path = os.path.join(ROOT, "devops", folder)
        elif section == "Systèmes exploitation":
            full_path = os.path.join(ROOT, "os", folder)
        else:  # Réseaux & Interfaces
            full_path = os.path.join(ROOT, "reseaux_interfaces", folder)

        n_files = count_md_files(full_path)
        label = LABELS.get(folder, folder)
        lines.append(f"- {label} ({n_files})")
    lines.append("")  # ligne vide après chaque section

# Écriture dans index.md
with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"index.md généré dans {OUTPUT}")
