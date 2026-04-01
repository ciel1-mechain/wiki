# Commandes Git : à connaître

|                                                  |                                                                                                                                                                |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `git status` ou `git status --short`            | afficher état du dépôt                                                                                                                                         |
| `git status --porcelain | grep '^??'`            | `??` : untacked, `M` : modifié et non indexé, `A` : index, `D` : supprimé                                                                                      |
| `git rm --cached`                                | désindexer et marquer comme untrack                                                                                                                            |
| `git  checkout -- <fichier>`                     | annuler les modifications dans le working directory                                                                                                            |
| `git  reset HEAD` ou `git  reset HEAD <fichier>` | retirer de l'index (staging area) après git add; modifications conservés dans répertoire de travail (suivi conservé)                                           |
| `git diff`, `git diff --staged`, `git diff HEAD` | différence espace de travail<->index, index<->dépot (Repository) (dernier commit), répertoire de travail<->dépôt (dernier commit)                              |
| `git  rm <fichier>`                              | supprime de l'espace de travail et de l'index                                                                                                                  |
| `git ls-files --others --exclude-standard`       | liste et filtre les fichiers suivis par Git dans le dépôt. `--others` pour afficher les untracked, `--exclude-standard` pour afficher les ignorés (.gitignore) |
| `git log` ou `git log --oneline`                 | afficher historique                                                                                                                                            |
| `git show <hash>` ou `git show`                  | afficher info sur objet, afficher dernier commit                                                                                                            |
|                                                  |                                                                                                                                                                |
|                                                  |                                                                                                                                                                |
|                                                  |                                                                                                                                                                |
|                                                  |                                                                                                                                                                |
|                                                  |                                                                                                                                                                |
