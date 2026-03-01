# Commandes Git - Référence

## git clone

Crée une copie locale **indépendante** d'un repo distant.

```bash
git clone git@github.com:user/mon-projet.git
```

| Commande | Description |
|---|---|
| `git clone <url>` | clone dans un dossier du même nom |
| `git clone <url> mon-dossier` | clone dans un dossier personnalisé |
| `git clone --depth 1 <url>` | clone uniquement le dernier commit (plus rapide) |

> `git clone` configure automatiquement `origin` pointant vers le repo cloné.

---

## Fork

Le fork n'est **pas une commande git**, c'est une fonctionnalité **GitHub uniquement**.

Un fork crée une copie du repo sur **ton compte GitHub**, indépendante de l'original.

**Faire un fork :**
1. Aller sur `github.com/prof/mon-projet`
2. Cliquer **Fork** en haut à droite
3. GitHub crée `github.com/eleve1/mon-projet`
4. Cloner ensuite son fork :
```bash
git clone git@github.com:eleve1/mon-projet.git
```

**Fork vs Clone :**

| | Fork | Clone |
|---|---|---|
| Où | Sur GitHub | En local |
| Commande | Bouton GitHub | `git clone` |
| Résultat | Copie sur ton compte GitHub | Copie sur ta machine |
| Lien avec l'original | Via PR | Via remote origin |
| Usage | Contribuer sans droits d'écriture | Travailler en local |

---

## git init

Initialise un nouveau repo git dans le dossier courant.

```bash
git init
```

Crée le dossier `.git/` qui contient toute l'histoire du repo.

---

## git config

Configure git (nom, email, éditeur...).

| Commande | Description |
|---|---|
| `git config --global user.name "Prénom Nom"` | définit le nom pour tous les repos |
| `git config --global user.email "email@example.com"` | définit l'email |
| `git config --global core.editor "vim"` | définit l'éditeur par défaut |
| `git config --global pull.rebase true` | utilise rebase par défaut au lieu de merge |
| `git config --list` | liste toute la configuration |
| `git config --global --list` | liste la config globale |
| `git config --local --list` | liste la config du repo courant |

---

## git add

Stage les fichiers pour le prochain commit.

| Commande | Description |
|---|---|
| `git add fichier.c` | stage un fichier précis |
| `git add .` | stage tous les fichiers modifiés |
| `git add -A` | stage tout (modifications + suppressions + nouveaux) |
| `git add -p` | stage par morceaux interactif (choisir quoi stager) |

> `git add -p` est très utile pour faire des commits atomiques : on choisit exactement quelles modifications vont dans le commit.

---

## git commit

| Commande | Description |
|---|---|
| `git commit -m "message"` | commit avec message inline |
| `git commit -a -m "message"` | stage et commit les fichiers suivis en une commande |
| `git commit --amend` | modifie le dernier commit (message ou contenu) |
| `git commit --amend -m "nouveau message"` | modifie uniquement le message du dernier commit |

> ⚠️ `--amend` modifie l'historique, ne pas utiliser si le commit est déjà pushé.

---

## git rm

Supprime un fichier **et** stage la suppression en une seule commande.

```bash
rm fichier.c        # supprime le fichier mais git add nécessaire ensuite
git rm fichier.c    # supprime + stage en une commande
```

| Commande | Description |
|---|---|
| `git rm fichier.c` | supprime et stage la suppression |
| `git rm --cached fichier.c` | retire du suivi git sans supprimer le fichier local |

> `git rm --cached` utile pour retirer un fichier accidentellement commité (ex: `.env`).

---

## git mv

Déplace ou renomme un fichier **et** stage le changement.

```bash
mv ancien.c nouveau.c        # renomme mais git add nécessaire ensuite
git mv ancien.c nouveau.c    # renomme + stage en une commande
```

---

## git tag

Marque un commit précis avec un nom (version, release...).

| Commande | Description |
|---|---|
| `git tag v1.0` | crée un tag léger sur HEAD |
| `git tag -a v1.0 -m "version 1.0"` | crée un tag annoté avec message |
| `git tag` | liste tous les tags |
| `git push origin v1.0` | pousse un tag vers le remote |
| `git push origin --tags` | pousse tous les tags |
| `git tag -d v1.0` | supprime un tag local |

---

## git revert

Annule un commit en créant un **nouveau commit** qui inverse les changements. Ne modifie pas l'historique.

```bash
git revert abc123       # annule le commit abc123
git revert HEAD         # annule le dernier commit
git revert HEAD~1       # annule l'avant-dernier commit
```

**revert vs reset :**

| | revert | reset |
|---|---|---|
| Historique | conservé | modifié |
| Sûr sur remote | ✅ oui | ⚠️ non |
| Usage | annuler un commit déjà pushé | annuler un commit local |

---

## git cherry-pick

Applique un commit précis sur la branche courante.

```bash
git cherry-pick abc123      # applique le commit abc123 sur la branche courante
git cherry-pick abc123 def456   # applique plusieurs commits
```

Utile pour récupérer un fix d'une branche sans merger toute la branche.

---

## git blame

Affiche qui a modifié chaque ligne d'un fichier et dans quel commit.

```bash
git blame fichier.c
git blame -L 10,20 fichier.c    # uniquement les lignes 10 à 20
```

---

## git clean

Supprime les fichiers **non suivis** (untracked) du répertoire de travail.

| Commande | Description |
|---|---|
| `git clean -n` | aperçu de ce qui sera supprimé (dry run) |
| `git clean -f` | supprime les fichiers non suivis |
| `git clean -fd` | supprime fichiers et dossiers non suivis |
| `git clean -fx` | supprime aussi les fichiers ignorés (.gitignore) |

> ⚠️ Toujours faire `git clean -n` avant `git clean -f` pour vérifier.

---

## git bisect

Trouve quel commit a introduit un bug par dichotomie.

```bash
git bisect start
git bisect bad              # le commit actuel est buggé
git bisect good abc123      # abc123 était correct
# git teste automatiquement les commits entre les deux
# pour chaque commit testé :
git bisect good             # si ce commit est ok
git bisect bad              # si ce commit est buggé
# git trouve le commit fautif
git bisect reset            # fin du bisect
```

---

## git fetch

Télécharge les commits du remote **sans modifier les fichiers locaux**.
Stocké dans `.git/refs/remotes/` sous forme de branches fantômes.

| Commande | Description |
|---|---|
| `git fetch origin` | télécharge depuis origin |
| `git fetch upstream` | télécharge depuis le repo référence |
| `git fetch --all` | télécharge depuis tous les remotes |

---



## git branch

| Commande | Description |
|---|---|
| `git branch` | liste les branches locales |
| `git branch -r` | liste les branches remote (fantômes) |
| `git branch -a` | liste toutes les branches (locales + remote) |
| `git branch ma-branche` | crée une branche sans basculer |
| `git branch -d ma-branche` | supprime une branche locale (si mergée) |
| `git branch -D ma-branche` | supprime une branche locale (force) |
| `git branch -m nouveau-nom` | renomme la branche courante |

---

## git checkout / git switch

| Commande | Description |
|---|---|
| `git checkout main` | bascule sur une branche existante |
| `git checkout -b nouvelle` | crée une branche et bascule dessus |
| `git switch main` | bascule sur une branche (syntaxe moderne) |
| `git switch -c nouvelle` | crée une branche et bascule (syntaxe moderne) |

---

## git diff

Compare des états entre eux. Toujours faire `git fetch <remote>` avant de comparer avec un remote pour avoir une version à jour.

> ⚠️ `git diff` ne détecte pas les **nouveaux fichiers** (untracked). Utiliser `git status` pour les voir.

| Commande | Modifications | Fichiers supprimés | Nouveaux fichiers |
|---|---|---|---|
| `git diff` | ✅ | ✅ | ❌ |
| `git diff --staged` | ✅ | ✅ | ✅ (si git add fait) |
| `git status` | ✅ | ✅ | ✅ |

```bash
# Comparer avec ton fork
git fetch origin
git diff origin/main

# Comparer avec le repo référence
git fetch upstream
git diff upstream/main
```

| Commande | Compare |
|---|---|
| `git diff` | working directory vs staging (non stagé) |
| `git diff --staged` | staging vs dernier commit (stagé) |
| `git diff HEAD~1` | dernier commit vs avant-dernier |
| `git diff HEAD~2` | dernier commit vs 2 commits en arrière |
| `git diff abc123 def456` | entre deux commits précis |
| `git diff main feature/ble` | entre deux branches |
| `git diff origin/main` | local vs ton fork (après `git fetch origin`) |
| `git diff upstream/main` | local vs repo référence (après `git fetch upstream`) |
| `git diff --name-only` | affiche uniquement les noms de fichiers |
| `git diff --name-only --diff-filter=U` | fichiers en conflit uniquement |

---

## git log

| Commande | Description |
|---|---|
| `git log` | historique complet |
| `git log --oneline` | une ligne par commit |
| `git log --oneline --graph` | graphe de la branche courante |
| `git log --oneline --graph --all` | graphe de toutes les branches |
| `git log --author="eleve1"` | commits d'un auteur précis |
| `git log fichier.c` | historique d'un fichier |
| `git log -n 5` | les 5 derniers commits |
| `git log main..feature/ble` | commits de feature absents de main |

---

## git status

| Commande | Description |
|---|---|
| `git status` | état complet du repo |
| `git status -s` | version courte/compacte |

**Légende `git status -s` :**

| Symbole | Signification |
|---|---|
| `M` | modifié |
| `A` | ajouté (stagé) |
| `?? ` | non suivi (untracked) |
| `UU` | conflit |

---

## git show

| Commande | Description |
|---|---|
| `git show` | détail du dernier commit |
| `git show abc123` | détail d'un commit précis |
| `git show HEAD~1` | détail de l'avant-dernier commit |

---

## HEAD

`HEAD` pointe vers le dernier commit de la branche courante.

| Référence | Signification |
|---|---|
| `HEAD` | dernier commit |
| `HEAD~1` | avant-dernier commit |
| `HEAD~2` | 2 commits en arrière |

---

## Les 3 zones Git

```
Fichiers modifiés        Zone de staging           Repo git
(working directory)         (index)                 (.git)

    fichier.c  ──git add──► fichier.c  ──git commit──► commit

    non stagé                 stagé                  commité
```

| Zone | Commande pour voir |
|---|---|
| Non stagé | `git diff` |
| Stagé | `git diff --staged` |
| Commité | `git log` / `git show` |

---

## git pull

Équivalent à `git fetch` + `git merge` en une seule commande.

| Commande | Description |
|---|---|
| `git pull upstream main` | récupère et fusionne le repo référence dans main local |
| `git pull origin main` | récupère et fusionne depuis ton fork |
| `git pull --rebase upstream main` | récupère et rebase au lieu de merger (historique plus propre) |

---

## git merge

Fusionne une branche dans la branche courante. Crée un **commit de merge**.

```bash
# Fusionner upstream/main dans main local
git checkout main
git merge upstream/main
```

| Commande | Description |
|---|---|
| `git merge upstream/main` | fusionne upstream/main dans la branche courante |
| `git merge feature/ble` | fusionne une branche locale |
| `git merge --no-ff feature/ble` | force un commit de merge même si fast-forward possible |
| `git merge --abort` | annule le merge en cours (si conflit) |

**Résultat visuel :**
```
main    : A → B → C ──────────── M   (M = commit de merge)
                    \           /
feature :            D → E → F
```

---

## git rebase

Réapplique les commits de la branche courante **par dessus** une autre branche. Historique linéaire, pas de commit de merge.

```bash
# Rebase ma branche feature par dessus main à jour
git checkout feature/ble
git rebase upstream/main
```

| Commande | Description |
|---|---|
| `git rebase upstream/main` | rebase par dessus upstream/main |
| `git rebase --abort` | annule le rebase en cours |
| `git rebase --continue` | continue après résolution d'un conflit |
| `git rebase -i HEAD~3` | rebase interactif sur les 3 derniers commits |

**Résultat visuel :**
```
avant rebase :
main    : A → B → C → D
feature :     B → X → Y

après rebase :
main    : A → B → C → D
feature :             X' → Y'   (X et Y réappliqués après D)
```

**merge vs rebase :**

| | merge | rebase |
|---|---|---|
| Historique | avec commit de merge | linéaire |
| Lisibilité | moins lisible | plus lisible |
| Usage | intégrer dans main | mettre à jour sa branche feature |

> ⚠️ Ne jamais rebase une branche déjà poussée sur un remote partagé.

---

## git push

`origin` = le repo depuis lequel tu as cloné :
- **projet solo** → origin = repo de départ
- **projet collaboratif avec fork** → origin = ton fork

| Commande | Description |
|---|---|
| `git push origin main` | pousse main vers origin |
| `git push origin feature/ble` | pousse une branche vers origin |
| `git push -u origin feature/ble` | pousse et définit le tracking upstream |
| `git push --force origin feature/ble` | force le push (écrase le remote) ⚠️ |
| `git push origin --delete feature/ble` | supprime une branche remote |

> ⚠️ `--force` écrase l'historique remote, à utiliser avec précaution.

---

## git remote

| Commande | Description |
|---|---|
| `git remote -v` | liste les remotes avec leurs URL |
| `git remote add origin <url>` | ajoute un remote origin |
| `git remote add upstream <url>` | ajoute le repo référence |
| `git remote set-url origin <url>` | change l'URL d'un remote |
| `git remote remove upstream` | supprime un remote |

---

## git stash

Met de côté les modifications en cours sans commiter. Utile pour changer de branche rapidement.

| Commande | Description |
|---|---|
| `git stash` | met les modifs de côté |
| `git stash pop` | récupère les modifs mises de côté |
| `git stash list` | liste les stashs |
| `git stash drop` | supprime le dernier stash |
| `git stash apply stash@{1}` | applique un stash précis sans le supprimer |

```bash
# Exemple : changer de branche sans perdre son travail
git stash
git checkout main
git pull upstream main
git checkout feature/ble
git stash pop
```

---

## git reset

Annule des commits ou déstagge des fichiers.

| Commande | Description |
|---|---|
| `git reset HEAD fichier.c` | déstagge un fichier (annule git add) |
| `git reset --soft HEAD~1` | annule le dernier commit, garde les modifs stagées |
| `git reset --mixed HEAD~1` | annule le dernier commit, garde les modifs non stagées |
| `git reset --hard HEAD~1` | annule le dernier commit, **supprime les modifs** ⚠️ |
| `git reset --hard origin/main` | remet à l'état du remote ⚠️ |

> ⚠️ `--hard` supprime définitivement les modifications locales.

---



```bash
# 1. Identifier les fichiers en conflit
git status
git diff --name-only --diff-filter=U

# 2. Dans le fichier, git insère :
<<<<<<< HEAD
ton code local
=======
code du remote
>>>>>>> upstream/main

# 3. Éditer le fichier → supprimer les marqueurs → garder le bon code

# 4. Marquer comme résolu
git add fichier_resolu.c
git commit -m "resolve merge conflict"
```
