#!/usr/bin/env python3
"""
Génère automatiquement index.md pour MkDocs Material
avec le nombre de fichiers Markdown dans chaque sous-dossier.
Les liens restent statiques et seuls les compteurs sont ajoutés.
"""

import os

ROOT = "./docs"  # dossier docs
OUTPUT = os.path.join(ROOT, "index.md")

# Sections et sous-dossiers
SECTIONS = {
    "DevOps": ["python", "c", "web", "git", "docker", "microbit"],
    "Réseaux & Liaisons": ["reseaux", "liaisons"],
    "Systèmes exploitation": ["windows", "gnu_linux"]
}

# Liens statiques avec icônes Material
LINKS = {
    "python": "[:material-language-python: Guide Python](devops/python.md)",
    "c": "[:material-language-cpp: Guide C](devops/c.md)",
    "web": "[:material-web: HTML/CSS/JS](devops/web.md)",
    "git": "[:material-github: Git & GitHub](devops/git.md)",
    "docker": "[:material-docker: Docker](devops/docker.md)",
    "microbit": "[:material-chip: Micro:Bit](devops/microbit.md)",
    "reseaux": "[:material-network: Réseaux TCP/IP](reseaux_liaisons/reseaux.md)",
    "liaisons": "[:material-connection: Liaisons numériques](reseaux_liaisons/liaisons.md)",
    "windows": "[:material-microsoft-windows: Windows](os/windows.md)",
    "gnu_linux": "[:material-linux: GNU/Linux](os/gnu_linux.md)"
}

def count_md_files(path):
    """Compte le nombre de fichiers Markdown dans un dossier."""
    if not os.path.isdir(path):
        return 0
    return len([f for f in os.listdir(path) if f.endswith(".md")])

lines = ["---", "hide:", "  - navigation", "  - toc", "---", "", "# Accueil", ""]

for section, subfolders in SECTIONS.items():
    lines.append(f"## {section}")
    for folder in subfolders:
        # Chemin complet vers le dossier
        if section == "DevOps":
            full_path = os.path.join(ROOT, "devops", folder)
        elif section == "Systèmes exploitation":
            full_path = os.path.join(ROOT, "os", folder)
        else:  # Réseaux & Interfaces
            full_path = os.path.join(ROOT, "reseaux_liaisons", folder)

        n_files = count_md_files(full_path)
        link = LINKS.get(folder, folder)
        # Ajoute juste le compteur à droite du lien
        # On injecte le compteur avant la parenthèse de fin si besoin
        link_with_count = f"{link} ({n_files})"
        lines.append(f"- {link_with_count}")
    lines.append("")  # ligne vide après chaque section

# Écriture dans index.md
with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"index.md généré dans {OUTPUT}")
