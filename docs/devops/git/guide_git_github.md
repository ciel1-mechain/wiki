# Cours complet : Git et GitHub

## Table des matières

### Partie 1 — Les bases
1. [Introduction](#1-introduction)
2. [Installation et configuration](#2-installation-et-configuration)
3. [Concepts fondamentaux](#3-concepts-fondamentaux)
4. [Travailler en local](#4-travailler-en-local)
5. [GitHub : travailler en ligne](#5-github--travailler-en-ligne)
6. [Les branches (bases)](#6-les-branches-bases)

### Partie 2 — Aller plus loin
7. [Branches avancées : rebase](#7-branches-avancées--rebase)
8. [Travailler en équipe](#8-travailler-en-équipe)
9. [Commandes utiles avancées](#9-commandes-utiles-avancées)
10. [Résumé des commandes](#10-résumé-des-commandes)
11. [Erreurs courantes](#11-erreurs-courantes)

---

# PARTIE 1 — LES BASES

---

## 1. Introduction

### Qu'est-ce que Git ?

Git est un **logiciel de gestion de versions distribué**. Il permet de :
- Sauvegarder l'historique complet de votre code
- Revenir à une version précédente en cas d'erreur
- Travailler à plusieurs sur un même projet sans se marcher dessus

> 💡 **Analogie** : Git c'est comme un "Ctrl+Z" surpuissant qui garde en mémoire *toutes* les modifications depuis le début du projet, avec la possibilité de revenir à n'importe quel point.

### Qu'est-ce que GitHub ?

GitHub est une **plateforme en ligne** qui héberge des dépôts Git. C'est le réseau social des développeurs. Il permet de :
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
| **Répertoire de travail** | Vos fichiers tels que vous les éditez |
| **Index (Staging Area)** | Zone de préparation : fichiers sélectionnés pour la prochaine sauvegarde |
| **Dépôt local** | L'historique complet des sauvegardes (*commits*) |

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

### Schéma global

```
GitHubDépôt GitHub (distant)
        │  ▲
 pull   │  │  push
        ▼  │
Dépôt local (git commit)
        │  ▲
git add │  │  git restore
        ▼  │
     Index (Staging)
        │  ▲
édition │  │  git restore
        ▼  │
  Répertoire de travail
```

### Cloner un dépôt existant
```bash
git clone https://github.com/utilisateur/nom-du-repo.git
```
Cela télécharge tout le contenu et l'historique dans un nouveau dossier local.

### Lier un dépôt local à GitHub

```bash
# 1. Créer un dépôt vide sur GitHub (via l'interface web)

# 2. Lier votre dépôt local au dépôt distant
git remote add origin https://github.com/votre-pseudo/votre-repo.git

# 3. Envoyer votre code sur GitHub pour la première fois
git push -u origin main
```

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

---

## 6. Les branches (bases)

### Concept
Une **branche** est une ligne de développement indépendante. Elles permettent de :
- Développer une fonctionnalité sans toucher au code stable
- Travailler à plusieurs en parallèle

```
main    : ●──────●──────────────●  ← (fusion ici)
               \                /
feature :        ●──────●──────●
```

### Commandes de base

```bash
# Lister les branches
git branch

# Créer et basculer vers une nouvelle branche (méthode moderne)
git switch -c ma-fonctionnalite

# Changer de branche existante
git switch main

# Fusionner une branche dans la branche courante
git switch main
git merge ma-fonctionnalite

# Supprimer une branche (après fusion)
git branch -d ma-fonctionnalite
```

> 💡 La branche principale s'appelle **main** (anciennement *master*).

### Les conflits de fusion

Un **conflit** survient quand deux branches ont modifié la même ligne du même fichier. Git marque les zones conflictuelles :

```
<<<<<<< HEAD
int x = 5;   // votre version
=======
int x = 10;  // version de l'autre branche
>>>>>>> feature
```

Pour résoudre : éditez le fichier manuellement, choisissez la bonne version, supprimez les marqueurs, puis :
```bash
git add fichier_conflit.c
git commit -m "Résolution du conflit"
```

---

# PARTIE 2 — ALLER PLUS LOIN

---

## 7. Branches avancées : rebase

### Merge vs Rebase

Il existe deux façons d'intégrer les modifications d'une branche dans une autre :

**Merge** : crée un commit de fusion, conserve l'historique tel quel.
```
main    : ●──●──────────●merge
              \         /
feature :      ●──●──●
```

**Rebase** : réécrit l'historique pour obtenir une ligne droite, sans commit de fusion.
```
main    : ●──●──●──●──●  ← commits de feature "rejoués" ici
```

```bash
# Se placer sur la branche à rebaser
git switch feature

# Rejouer les commits de feature par-dessus main
git rebase main
```

> ⚠️ **Règle d'or** : ne jamais rebaser une branche déjà partagée sur GitHub avec d'autres personnes, car cela réécrit l'historique et crée des problèmes de synchronisation.

### Après un rebase avec conflits

```bash
# Résoudre les conflits dans les fichiers concernés, puis :
git add fichier_conflit.c
git rebase --continue

# Ou annuler le rebase
git rebase --abort
```

---

## 8. Travailler en équipe

### Fork et Pull Request (sur GitHub)

Le **fork** permet de copier le dépôt de quelqu'un d'autre dans votre compte GitHub pour y contribuer librement.

La **Pull Request** (PR) est une demande de fusion de vos modifications vers le dépôt original. C'est aussi l'occasion de faire une **revue de code** entre coéquipiers.

### Workflow typique en équipe

```bash
# 1. Cloner le dépôt du projet
git clone https://github.com/equipe/projet.git

# 2. Créer une branche pour votre fonctionnalité
git switch -c feature/ajout-login

# 3. Travailler, faire des commits réguliers
git add .
git commit -m "Ajout du formulaire de connexion"

# 4. Mettre à jour sa branche par rapport à main (bonne pratique)
git fetch origin
git rebase origin/main

# 5. Envoyer la branche sur GitHub
git push origin feature/ajout-login

# 6. Créer une Pull Request sur GitHub (via l'interface web)
# 7. Un coéquipier relit, commente et valide → fusion dans main
```

### Remote tracking

Chaque branche locale peut **suivre** une branche distante. Cela permet à Git de savoir si vous êtes en avance ou en retard par rapport au distant.

```bash
# Voir l'état de toutes les branches (locales et distantes)
git branch -a

# Suivre explicitement une branche distante
git branch --set-upstream-to=origin/main main
```

---

## 9. Commandes utiles avancées

### git stash : mettre de côté des modifications

Très utile quand on doit changer de branche rapidement sans vouloir créer un commit.

```bash
# Sauvegarder temporairement les modifications en cours
git stash

# Changer de branche, corriger un bug, etc.
git switch main

# Revenir et récupérer ses modifications
git switch ma-branche
git stash pop
```

### git reset : annuler des commits

```bash
# Annuler le dernier commit mais garder les modifications dans l'index
git reset --soft HEAD~1

# Annuler le dernier commit et vider l'index (modifications toujours présentes)
git reset HEAD~1

# Annuler le dernier commit et supprimer toutes les modifications ⚠️ IRRÉVERSIBLE
git reset --hard HEAD~1
```

> ⚠️ `git reset --hard` supprime définitivement vos modifications. À utiliser avec précaution.

### git log avancé

```bash
# Historique avec graphe des branches
git log --oneline --graph --all

# Historique d'un fichier spécifique
git log --oneline mon_fichier.c
```

---

## 10. Résumé des commandes

### Commandes de base

| Commande | Description |
|----------|-------------|
| `git init` | Initialiser un dépôt |
| `git clone <url>` | Cloner un dépôt distant |
| `git status` | État du dépôt |
| `git add <fichier>` | Ajouter un fichier à l'index |
| `git add .` | Ajouter tous les fichiers modifiés |
| `git commit -m "msg"` | Créer un commit |
| `git log --oneline` | Historique condensé |
| `git diff` | Voir les modifications non indexées |
| `git restore <fichier>` | Annuler des modifications |
| `git push` | Envoyer sur GitHub |
| `git pull` | Récupérer et fusionner depuis GitHub |
| `git remote add origin <url>` | Lier à un dépôt distant |

### Commandes avancées

| Commande | Description |
|----------|-------------|
| `git branch` | Lister les branches |
| `git switch -c <branche>` | Créer et basculer vers une branche |
| `git merge <branche>` | Fusionner une branche |
| `git rebase <branche>` | Rebaser sur une branche |
| `git fetch` | Récupérer sans fusionner |
| `git stash` | Mettre de côté des modifications |
| `git stash pop` | Récupérer les modifications mises de côté |
| `git reset --hard` | Annuler toutes les modifications locales ⚠️ |
| `git log --graph --all` | Historique visuel des branches |
| `git branch -a` | Lister toutes les branches (locales + distantes) |

---

## 11. Erreurs courantes

### "fatal: not a git repository"
Vous n'êtes pas dans un dossier suivi par Git.
```bash
git init   # ou se placer dans le bon dossier avec cd
```

### "Please tell me who you are"
Git n'est pas configuré.
```bash
git config --global user.name "Votre Nom"
git config --global user.email "votre@email.com"
```

### "rejected — fetch first"
Quelqu'un a pushé avant vous. Il faut récupérer ses modifications d'abord.
```bash
git pull
git push
```

### Oublier le `-m` dans git commit
```bash
git commit   # sans -m ouvre vim — pour en sortir : Echap puis :wq puis Entrée
# Conseil : toujours utiliser git commit -m "message"
```

### Avoir pushé par erreur
```bash
# Annuler le dernier commit en local
git reset --soft HEAD~1
# Puis forcer le push (⚠️ uniquement sur une branche personnelle, jamais sur main partagé)
git push --force
```

---

> 📚 **Pour aller plus loin :**
> - Documentation officielle : https://git-scm.com/doc  
> - Visualiser Git interactivement : https://learngitbranching.js.org  
> - GitHub Skills (tutoriels guidés) : https://skills.github.com  
