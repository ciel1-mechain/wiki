# Git et GitHub : partie 2

## 1. Les branches (bases)

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

## 2. Branches avancées : rebase

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

## 3. Travailler en équipe

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

## 4. Commandes utiles avancées

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

## 5. Résumé des commandes

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

## 6. Erreurs courantes

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
