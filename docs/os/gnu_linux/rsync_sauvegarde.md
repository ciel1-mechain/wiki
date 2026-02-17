# Sauvegarde avec rsync sous Fedora Linux

## Principe

Deux sauvegardes complémentaires :

- **Miroir** — copie exacte et à jour de la source 
- **Incrémentale** — historique des versions avec les anciennes versions conservées par date

---

## Structure des répertoires

```
/home/user/travail/          ← source

/home/user/backup/miroir/    ← copie miroir (local)

/mnt/hdd/backup/
├── miroir/                  ← miroir sur HDD
└── historique/
    ├── 2026-02-10/          ← anciennes versions écrasées ce jour-là
    ├── 2026-02-13/
    └── 2026-02-17/
```

---

## Commandes

### Miroir seul (local ou HDD)

```bash
rsync -av --delete /home/user/travail/ /home/user/backup/miroir/
```

### Miroir + historique incrémental sur HDD (une seule commande)

```bash
rsync -av --delete \
  --backup \
  --backup-dir=/mnt/hdd/backup/historique/$(date +%Y-%m-%d) \
  /home/user/travail/ /mnt/hdd/backup/miroir/
```

### Test à blanc (sans rien modifier)

```bash
rsync -av --delete --dry-run \
  --backup \
  --backup-dir=/mnt/hdd/backup/historique/$(date +%Y-%m-%d) \
  /home/user/travail/ /mnt/hdd/backup/miroir/
```

---

## Options rsync expliquées

| Option | Rôle |
|---|---|
| `-a` | Archive : préserve permissions, dates, liens symboliques |
| `-v` | Verbeux : affiche les fichiers traités |
| `--delete` | Supprime dans la destination ce qui n'existe plus dans la source |
| `--backup` | Déplace les anciens fichiers avant de les écraser |
| `--backup-dir` | Répertoire de destination des anciennes versions |
| `--dry-run` | Simule sans rien modifier |

> ⚠️ **Le slash final sur la source est crucial** : `/source/` copie le *contenu*, `/source` copie le *répertoire lui-même*.

---

## Logique de l'historique

> L'historique d'une date contient la version **d'avant** les modifications de ce jour-là.

Exemple avec `document.odt` modifié le 2026-02-10 :

```
miroir/document.odt                        ← version B (nouvelle, actuelle)
historique/2026-02-10/document.odt         ← version A (ancienne, d'avant le 10)
```

---

## Retrouver et restaurer une ancienne version

### Lister les fichiers sauvegardés un jour donné

```bash
ls /mnt/hdd/backup/historique/2026-02-10/
```

### Trouver toutes les versions d'un fichier

```bash
find /mnt/hdd/backup/historique/ -name "document.odt" -ls
```

### Comparer deux versions (fichiers texte)

```bash
diff /mnt/hdd/backup/historique/2026-02-10/document.odt \
     /mnt/hdd/backup/miroir/document.odt
```

### Restaurer un fichier à une date précise

```bash
cp /mnt/hdd/backup/historique/2026-02-10/document.odt \
   /home/user/travail/document.odt
```

### Restaurer un répertoire entier à une date

```bash
rsync -av /mnt/hdd/backup/historique/2026-02-10/ /home/user/travail/
```

---

## Automatisation avec cron

```bash
crontab -e
```

Ajouter la ligne suivante pour une sauvegarde tous les jours à 2h du matin :

```cron
0 2 * * * rsync -av --delete --backup --backup-dir=/mnt/hdd/backup/historique/$(date +\%Y-\%m-\%d) /home/user/travail/ /mnt/hdd/backup/miroir/
```

---

## Nettoyage automatique de l'historique

Sans nettoyage, l'historique grossit indéfiniment. Pour ne garder que les **30 derniers jours** :

```bash
find /mnt/hdd/backup/historique/ -maxdepth 1 -type d -mtime +30 -exec rm -rf {} \;
```

Intégré dans cron (juste après le rsync) :

```cron
0 2 * * * rsync -av --delete --backup --backup-dir=/mnt/hdd/backup/historique/$(date +\%Y-\%m-\%d) /home/user/travail/ /mnt/hdd/backup/miroir/ && find /mnt/hdd/backup/historique/ -maxdepth 1 -type d -mtime +30 -exec rm -rf {} \;
```
