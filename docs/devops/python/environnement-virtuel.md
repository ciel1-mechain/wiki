# Installation et utilisation d’un environnement virtuel Python (`venv`)

## 1. Création d’un environnement virtuel

```bash
python3 -m venv nom_du_venv
```

* `nom_du_venv` : dossier qui contiendra l’environnement virtuel.

---

## 2. Activation de l’environnement virtuel

* **Sous Linux / macOS :**

  ```bash
  source nom_du_venv/bin/activate
  ```
  
* **Sous Windows :**

  ```cmd
  nom_du_venv\Scripts\activate
  ```

> Lorsque l’environnement est activé, le prompt affiche généralement le nom du venv entre parenthèses.

---

## 3. Désactivation de l’environnement virtuel

```bash
deactivate
```

---

# Utilisation de `pip` dans un venv

## Installer une bibliothèque

```bash
pip install nom_de_la_bibliotheque
```

## Mettre à jour toutes les bibliothèques

1. **Lister les bibliothèques installées dans un fichier :**

   ```bash
   pip freeze > requirements.txt
   ```

2. **Mettre à jour toutes les bibliothèques d’un coup** (méthode avec une boucle) :

   ```bash
   pip list --outdated --format=freeze | cut -d = -f 1 | xargs -n1 pip install -U
   ```

3. **Mettre à jour une bibliothèque spécifique :**

   ```bash
   pip install --upgrade nom_de_la_bibliotheque
   ```

---

# Utilisation d’un fichier `requirements.txt`

## Exporter les bibliothèques installées

```bash
pip freeze > requirements.txt
```

## Installer toutes les bibliothèques listées

```bash
pip install -r requirements.txt
```

---

# À retenir

* Créez un venv pour isoler vos projets Python.
* Activez ou désactivez le venv avec `source .../activate` et `deactivate`.
* Installez, exportez, et mettez à jour vos bibliothèques avec `pip`.
* Utilisez `requirements.txt` pour partager ou reproduire l’environnement d’un projet.

