# Git — Internals & Commandes de référence

## 1. Stockage interne des objets

Git stocke tout dans `.git/objects/` sous forme de **contenu brut compressé zlib**.

Avant compression, chaque objet a ce format :
```
"<type> <taille>\0<contenu>"
ex: "blob 13\0Hello, World!"
```

Le **hash SHA-1** est calculé sur ce contenu brut (avant compression) → garantit l'intégrité.  
Un hash complet = **40 caractères hexadécimaux**. Git accepte les préfixes courts (7+ chars) tant qu'ils sont non-ambigus.

**Vérifier manuellement :**
``` bash
echo -e "blob 6\0Hello, World!" | sha1sum
# → doit correspondre au hash Git du fichier contenant "Hello, World!"
```
`git cat-file` existe pour cela. C'est le moyen propre de lire ces objets sans décompresser manuellement avec zlib.

```bash
git rev-parse a3f7c91        # → hash complet 40 chars
cat .git/objects/a3/f7c91…   # → binaire illisible (zlib)
git cat-file -p a3f7c91      # → contenu lisible (décompressé par Git)
```

### 4 types d'objets

| Type   | Contenu |
|--------|---------|
| blob   | Contenu brut d'un fichier |
| tree   | Liste de blobs/trees (= répertoire) |
| commit | Hash du tree racine + parent + métadonnées |
| tag    | Référence annotée vers un commit |

---

## 2. Références : de simples fichiers texte

```bash
cat .git/refs/heads/main     # → hash du dernier commit de main
cat .git/HEAD                # → "ref: refs/heads/main"
```

Structure :
```
.git/
├── HEAD                     ← branche courante
├── refs/
│   ├── heads/main           ← dernier commit de chaque branche
│   └── tags/v1.0            ← tags
└── objects/                 ← tous les objets compressés
```

---

## 3. git add et git commit

**`git add`** crée **un blob par fichier** immédiatement dans `.git/objects/`, avant même le commit.

**`git commit`** reconstruit les trees en **réutilisant** les objets inchangés :

```
Avant :  tree-root → tree-src → blob-main.c  (modifié)
                              → blob-utils.c (inchangé)
         tree-root → blob-README              (inchangé)

Après :  tree-root (NOUVEAU) → tree-src (NOUVEAU) → blob-main.c (NOUVEAU)
                                                   → blob-utils.c ← même hash
                             → blob-README          ← même hash
```

Les objets sont **immutables et dédupliqués par contenu** — même contenu = même hash = même objet partagé.

---

## 4. Lire les objets Git

```bash
git cat-file -t <HASH>       # Type de l'objet (blob/tree/commit/tag)
git cat-file -p <HASH>       # Contenu décompressé de l'objet
git cat-file --batch-all-objects --batch-check  # Tous les objets du repo
```

---

## 5. Accéder à une version d'un fichier

```bash
git show HEAD:fichier        # Version actuelle (dernier commit)
git show HEAD~1:fichier      # Version il y a 1 commit
git show HEAD~5:fichier      # Version il y a 5 commits
git show abc123:fichier      # Version à un commit précis
git show "main@{2024-01-15}":fichier  # Version à une date donnée
git show v1.0:fichier        # Version au tag v1.0
```

---

## 6. git log — options avancées

### `--` : séparateur chemin

Sépare les révisions des chemins de fichiers pour lever toute ambiguïté :
```bash
git log -- fichier.txt       # Historique du fichier
git log main -- fichier.txt  # Depuis main, sur ce fichier
```
Sans `--`, Git peut confondre un nom de branche et un nom de fichier.

C'est une convention Unix standard qu'on retrouve dans beaucoup d'outils (rm --, ssh --, etc.) qui signifie toujours la même chose : "fin des options, ce qui suit est un argument

### `--follow` : suivre les renommages

Suit l'historique d'un fichier **à travers ses renommages** :
```bash
git log --follow -- fichier.txt
```
Sans `--follow`, l'historique s'arrête au renommage.

### `--diff-filter` : filtrer par type de changement

| Lettre | Signification |
|--------|---------------|
| `A`    | Added — fichier ajouté |
| `M`    | Modified — fichier modifié |
| `D`    | Deleted — fichier supprimé |
| `R`    | Renamed |
| `C`    | Copied |

```bash
# Premier commit ayant créé un fichier
git log --follow --diff-filter=A -- fichier.txt

# Tous les commits ayant modifié un fichier
git log --diff-filter=M -- fichier.txt

# Combiner plusieurs filtres
git log --diff-filter=AM -- fichier.txt
```

### Autres options utiles de git log

```bash
git log --oneline            # Format compact (hash court + message)
git log --graph --oneline    # Arbre des branches ASCII
git log -p -- fichier        # Diff complet de chaque commit
git log --stat               # Résumé des fichiers modifiés
git log --name-only          # Noms des fichiers modifiés seulement
git log --author="Nom"       # Filtrer par auteur
git log --since="2 weeks ago" --until="yesterday"
git log --grep="fix"         # Filtrer par message de commit
```

---

## 7. Naviguer dans le temps

```bash
# Commit le plus proche avant une date
git rev-list -n 1 --before="2024-01-15 12:00" main

# Voir l'état complet du repo à un commit donné
git show abc123:./            # Tree racine à ce commit
```

---

## 8. Reconstruire / extraire les fichiers

```bash
# Reconstruire tous les fichiers depuis HEAD (plomberie)
git read-tree --reset HEAD
git checkout-index -a -f

# Reconstruire tous les fichiers (porcelaine)
git checkout HEAD -- .

# Restaurer un fichier spécifique depuis HEAD
git checkout HEAD -- fichier.txt

# Restaurer depuis un commit précis
git checkout abc123 -- fichier.txt
```

**Différence `checkout` vs `read-tree` + `checkout-index` :**
- `checkout` = porcelaine : déplace HEAD, gère conflits, usage quotidien
- `read-tree` + `checkout-index` = plomberie : chirurgical, ne touche pas HEAD, utile pour scripts ou extraire des fichiers d'une autre branche sans changer de branche

---

## 9. Commandes de plomberie utiles

```bash
git hash-object fichier.txt         # Hash SHA-1 d'un fichier (sans l'ajouter)
git hash-object -w fichier.txt      # Hash + stocke dans objects/

git ls-files                        # Fichiers dans l'index
git ls-files --stage                # Index avec hashes et modes

git ls-tree HEAD                    # Tree du dernier commit
git ls-tree -r HEAD                 # Récursif (tous les fichiers)
git ls-tree -r --name-only HEAD     # Juste les chemins

git diff-tree -r <HASH>             # Fichiers modifiés dans un commit
git diff-index HEAD                 # Diff entre index et HEAD

git update-index --add fichier.txt  # Ajouter à l'index manuellement
git write-tree                      # Créer un objet tree depuis l'index
git commit-tree <tree> -p <parent> -m "msg"  # Créer un commit manuellement
```

---

## 10. Inspecter et réparer

```bash
git fsck                            # Vérifier l'intégrité du repo
git fsck --lost-found               # Trouver les objets orphelins
git gc                              # Garbage collect + compresse en pack files
git count-objects -v                # Nombre d'objets et taille
git verify-pack -v .git/objects/pack/*.idx  # Inspecter un pack file

git reflog                          # Historique de tous les mouvements de HEAD
git reflog show main                # Reflog d'une branche spécifique
```

---

## 11. Récupérer des données perdues

```bash
# Retrouver un commit perdu (après reset --hard, etc.)
git reflog
git checkout -b rescue abc123

# Retrouver des fichiers supprimés
git log --diff-filter=D --summary -- fichier_supprime.txt
git show <commit-avant-suppression>:fichier_supprime.txt
```

---

## 12. Bare repo

Utilisé par les serveurs (GitHub, GitLab, SSH) — pas besoin d'éditer les fichiers, juste recevoir/servir des objets.

```
repo normal :          bare repo :
mon-projet/            mon-projet.git/
├── .git/              ├── objects/
├── fichier.txt        ├── refs/
└── src/               └── HEAD
```

```bash
git init --bare repo.git
git clone --bare .
```

Github stocke des **bare repos** (objets zlib compressés).  
Les fichiers affichés dans le navigateur sont **décompressés à la volée** — pas stockés en clair sur disque.

## Résumé visuel

```
git add       → crée blob(s) dans objects/
git commit    → crée tree(s) + commit dans objects/, met à jour refs/heads/
git show      → décompresse et affiche un objet
git cat-file  → lit les objets bruts (plomberie)
git log       → parcourt la chaîne de commits via les hashes parents
refs/heads/*  → fichiers texte pointant vers le dernier commit de chaque branche
HEAD          → fichier texte pointant vers la branche courante
```
