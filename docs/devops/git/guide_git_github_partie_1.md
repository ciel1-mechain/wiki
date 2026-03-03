# Git et GitHub : partie 1

## 1. Introduction

### Qu'est-ce que Git ?

Git est un **logiciel de gestion de versions distribué**. Il permet de :

- Sauvegarder l'historique complet de votre code
- Revenir à une version précédente en cas d'erreur
- Travailler à plusieurs sur un même projet sans se marcher dessus

  
> 💡 **Analogie** : Git c'est comme un "Ctrl+Z" surpuissant qui garde en mémoire *toutes* les modifications depuis le début du projet, avec la possibilité de revenir à n'importe quel point.

### Qu'est-ce que GitHub ?

GitHub est une **plateforme en ligne** qui héberge des dépôts Git. Il permet de :

- Stocker son code en ligne (sauvegarde distante)
- Collaborer avec d'autres développeurs
- Partager ses projets et faire de la revue de code

> ⚠️ **Git ≠ GitHub** : Git est l'outil (local), GitHub est le service en ligne. On peut tout à fait utiliser Git sans GitHub.

---

## 2. Installation et configuration

### Installer Git

**Windows** : télécharger depuis https://git-scm.com/download/win

**Linux (Debian/Ubuntu)** :
```bash
sudo apt install git
```

**Vérifier l'installation** :
```bash
git --version
# Exemple : git version 2.43.0
```

### Configurer Git

Avant toute chose, il faut dire à Git qui vous êtes. Ces informations apparaîtront dans l'historique de chaque commit.

```bash
git config --global user.name "Prénom Nom"
git config --global user.email "votre@email.com"
```

Vérifier la configuration :
```bash
git config --list
```

---

## 3. Concepts fondamentaux

### Le dépôt (repository)
Un **dépôt** (ou *repo*) est un dossier suivi par Git. Il contient votre code + tout l'historique des modifications, stocké dans un dossier caché `.git` créé automatiquement.

### Les 3 zones de Git

C'est le concept le plus important à comprendre :

```
┌──────────────────┐   git add    ┌───────────────┐   git commit  ┌────────────────┐
│  Répertoire de   │ ──────────►  │      Index    │ ────────────► │  Dépôt local   │
│   travail        │              │   (Staging)   │               │  (Historique)  │
│  (vos fichiers)  │              │               │               │                │
└──────────────────┘              └───────────────┘               └────────────────┘
```

| Zone | Rôle |
|------|------|
| **Répertoire de travail** | Vos fichiers texte/binaires tels que vous les éditez |
| **Index (Staging Area)** | Zone de préparation : fichiers sélectionnés pour la prochaine sauvegarde. Snapshot intermédiaire, les blobs sont déjà dans `objects/` mais pas encore liés à un commit|
| **Dépôt local** | L'historique complet des sauvegardes (*commits*) |

> `.git/` → base d'objets compressés zlib + refs

---

**"dépôt" / "repo"** — le terme dépend du contexte :
- au sens strict = juste `.git/` (les objets, l'historique)
- au sens large = `.git/` + working dir ensemble
- un **bare repo** (`git clone --bare`) = `.git/` seul, sans working dir — c'est ce qu'utilisent les serveurs

---

**GitHub** stocke uniquement l'équivalent d'un **bare repo** — les objets compressés zlib, les refs, les pack files. Pas de working dir décompressé sur disque.

Quand tu navigues sur github.com et vois les fichiers, GitHub les **décompresse à la volée** depuis les objets blob pour les afficher dans le navigateur. C'est du rendu dynamique, pas des fichiers stockés en clair quelque part.

### Le commit
Un **commit** est une **photo** de votre projet à un instant T. Chaque commit possède :

- Un identifiant unique (hash SHA-1, ex: `a3f5c2d`)
- Un message décrivant les changements
- La date et l'auteur

---

## 4. Travailler en local

### Initialiser un dépôt
```bash
git init
```
Un dossier caché `.git` est créé : c'est là que Git stocke tout l'historique.  
Ne le supprimez jamais !

### Vérifier l'état du dépôt
```bash
git status
```
Cette commande est votre meilleure amie ! Elle indique :

- Les fichiers modifiés non encore ajoutés (en rouge)
- Les fichiers prêts à être commités (en vert)
- Les fichiers non suivis par Git

### Ajouter des fichiers à l'index
```bash
# Ajouter un fichier spécifique
git add mon_fichier.c

# Ajouter tous les fichiers modifiés
git add .
```

### Créer un commit
```bash
git commit -m "Message décrivant les changements"
```

> 💡 **Bonne pratique** : Un message de commit doit être court et descriptif.  
> ✅ `"Ajout de la fonction calcul_moyenne"`  
> ❌ `"modif"` 

### Voir l'historique
```bash
# Historique complet (auteur, date, message)
git log

# Historique condensé — une ligne par commit
git log --oneline
```

### Voir les modifications
```bash
# Voir les modifications non encore ajoutées à l'index
git diff
```

### Revenir en arrière
```bash
# Annuler les modifications d'un fichier (avant git add)
git restore mon_fichier.c

# Retirer un fichier de l'index (après git add, avant git commit)
git restore --staged mon_fichier.c
```

### Exemple de workflow complet
```bash
# 1. Je modifie mon fichier main.c
# 2. Je vérifie ce qui a changé
git status

# 3. J'ajoute mes modifications à l'index
git add main.c

# 4. Je sauvegarde avec un message
git commit -m "Ajout de la boucle principale"

# 5. Je vérifie l'historique
git log --oneline
```

---

## 5. GitHub : travailler en ligne

### Lier un dépôt local à GitHub

```bash
# 1. Créer un dépôt vide sur GitHub (via l'interface web)

# 2. Lier votre dépôt local au dépôt distant
git remote add origin https://github.com/votre-pseudo/votre-repo.git

# 3. Envoyer votre code sur GitHub pour la première fois
git push -u origin main
```

Cloner un dépôt existant
```bash
git clone https://github.com/utilisateur/nom-du-repo.git
```
Cela télécharge tout le contenu et l'historique dans un nouveau dossier local.

### Les commandes distantes au quotidien

```bash
# Envoyer ses commits locaux vers GitHub
git push

# Récupérer les nouveaux commits depuis GitHub et les fusionner
git pull

# Récupérer les modifications sans fusionner (pour inspecter d'abord)
git fetch

# Voir les dépôts distants configurés
git remote -v
```

> 💡 **pull = fetch + merge** : `git pull` récupère ET fusionne automatiquement. `git fetch` récupère seulement, vous fusionnez quand vous voulez.

## 6. Utiliser GitHub sur deux postes de travail (ou plus)

### Objectif

Travailler sur un même dépôt GitHub depuis le lycée **et** votre ordinateur personnel, sans jamais perdre de modifications.


### Rappel important

Votre dépôt GitHub est le **point central**. Chaque poste de travail possède une copie locale du dépôt.


### Routine à suivre sur chaque poste de travail

#### 1. Avant de commencer à travailler

Pour récupérer la version la plus récente du dépôt :

```bash
git pull
```


#### 2. Après avoir travaillé (ajouts, modifications…)

Enregistrez vos modifications localement :

```bash
git add --all
git commit -m "Votre message de commit"
```


#### 3. À la fin de la session de travail

Envoyez vos modifications vers GitHub :

```bash
git push
```


#### 4. Quand vous changez de poste

1. Sur le nouveau poste, commencez toujours par :
   
   ```bash
   git pull
   ```

2. Travaillez normalement (modifiez, ajoutez, supprimez, commit…).

3. Terminez par :
   
   ```bash
   git push
   ```


### Conseils pratiques

- En cas de message d’erreur ou de conflit, lisez attentivement l’explication ou demandez de l’aide.
- Faites des *commits* réguliers avec des messages explicites.
- Ne supprimez **jamais** le dossier `.git` dans le dépôt !
- Faites régulièrement une sauvegarde de l'ensemble de votre dépôt sur un autre support (clé USB).


### Interface graphique

Pour plus de facilité, vous pourrez ensuite utiliser une interface graphique

- GUI **Git/GitHub**
  - pour *Windows* : [Github Desktop](https://github.com/apps/desktop)
  - pour *Linux* : [GitHub Desktop - The Linux Fork](https://github.com/shiftkey/desktop)
---
