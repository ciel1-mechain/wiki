# Guide Git et GitHub

**Git** est un système de gestion de versions distribué qui permet de suivre les modifications dans un projet de code. Il fonctionne principalement **en local**, mais peut être utilisé avec des services distants comme **GitHub** pour collaborer avec d'autres développeurs.

**GitHub** est une plateforme d'hébergement de code qui permet de stocker des repositories Git en ligne, faciliter la collaboration, la revue de code, et l'intégration continue.

---

## 1. Concepts clés

### 1.1 Repository (dépôt)

* Un repository est un projet Git. Il peut être **local** (sur ton ordinateur) ou **distant** (sur GitHub).
* Il contient tout l’historique du projet dans le dossier caché `.git`.

### 1.2 .git

* Le dossier `.git` contient **toutes les informations sur l’historique, les branches, les commits et la configuration**.
* Il est créé avec `git init`.

### 1.3 Local vs Remote

* **Local** : ton environnement de travail sur ton ordinateur.
* **Remote** : repository sur GitHub (ou autre serveur).
* Tu synchronises les deux avec `git push` (local → remote) et `git pull` (remote → local).

### 1.4 Branches

* Une branche est une version parallèle du code.
* La branche par défaut est généralement `main` ou `master`.
* Tu peux créer, changer ou fusionner des branches.

### 1.5 Commit

* Un commit est un **instantané de ton projet**.
* Il enregistre les modifications locales dans l’historique Git.

### 1.6 Fusion et rebase

* **Merge (fusion)** : combine les modifications d’une branche dans une autre, créant un commit de fusion si nécessaire.
* **Rebase** : applique les commits d’une branche par-dessus une autre, réécrivant l’historique pour un historique linéaire.

### 1.7 Pull et Push

* **git push** : envoie les commits locaux vers le remote (GitHub).
* **git pull** : récupère les modifications depuis le remote et les fusionne avec la branche locale.

### 1.8 Staging et Working Directory

* **Working Directory** : fichiers sur lesquels tu travailles.
* **Staging Area (index)** : fichiers préparés pour le prochain commit (`git add`).
* **Commit** : sauvegarde du contenu de l’index dans l’historique Git.

### 1.9 Résolution de conflits

* Survenue quand deux branches ont modifié les mêmes lignes d’un fichier.
* Git te demande de choisir quelle version garder, puis `git add` + `git commit`.

### 1.10 Remote Tracking

* Chaque branche locale peut suivre une branche distante.
* `git fetch` : récupère les modifications sans fusionner.
* `git pull` : récupère et fusionne automatiquement.

---

## 2. Workflow Git et GitHub

1. **Initialiser le repo local** :

```bash
git init
```

2. **Ajouter un remote (GitHub)** :

```bash
git remote add origin https://github.com/utilisateur/repo.git
```

3. **Travailler sur les fichiers** : modifier, ajouter avec `git add`.

4. **Commit des modifications** :

```bash
git commit -m "Message du commit"
```

5. **Envoyer vers GitHub** :

```bash
git push origin main
```

6. **Récupérer les changements du remote** :

```bash
git pull origin main
```

7. **Branches et fusion** :

```bash
git checkout -b nouvelle_branche   # créer et changer de branche
# travailler
git checkout main
git merge nouvelle_branche          # fusionner
```

8. **Rebase** :

```bash
git checkout feature
git rebase main  # réapplique les commits de feature sur main
```

9. **Résolution de conflits** : modifier fichiers conflictuels, puis :

```bash
git add fichier_conflit
git rebase --continue  # ou git commit si merge
```

---

## 3. Tableau des commandes essentielles

| Commande                  | Description                                                 |
| ------------------------- | ----------------------------------------------------------- |
| `git init`                | Crée un nouveau repository Git local                        |
| `git clone <url>`         | Récupère un repo distant sur ton local                      |
| `git status`              | Affiche l’état des fichiers (modifiés, staged, non suivis)  |
| `git add <fichier>`       | Ajoute un fichier à l’index (staging area)                  |
| `git commit -m "message"` | Crée un commit avec les fichiers staged                     |
| `git log`                 | Affiche l’historique des commits                            |
| `git diff`                | Affiche les différences non staged                          |
| `git branch`              | Liste les branches locales                                  |
| `git branch <nom>`        | Crée une nouvelle branche                                   |
| `git checkout <branche>`  | Change de branche                                           |
| `git merge <branche>`     | Fusionne une branche dans la branche courante               |
| `git rebase <branche>`    | Réapplique les commits de la branche courante sur une autre |
| `git remote -v`           | Liste les dépôts distants                                   |
| `git fetch`               | Récupère les commits depuis le remote sans fusionner        |
| `git pull`                | Récupère et fusionne les commits depuis le remote           |
| `git push`                | Envoie les commits locaux vers le remote                    |
| `git stash`               | Sauvegarde temporairement les modifications non committées  |
| `git stash pop`           | Récupère les modifications sauvegardées                     |
| `git reset --hard`        | Annule toutes les modifications locales non committées      |

---

### Remarques finales

* Git permet un **historique complet et distribué** de ton projet.
* GitHub facilite la **collaboration** en ligne et la revue de code.
* Les conflits sont normaux lors de la collaboration et Git fournit les outils pour les résoudre.

---

