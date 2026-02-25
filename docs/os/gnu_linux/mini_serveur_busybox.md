# Mini-serveur web avec BusyBox et extraction du texte

## 1. Lancer un serveur web minimaliste
On utilise **BusyBox** qui contient un serveur HTTP (`httpd`) très simple :
```sh
busybox httpd -v -f -p 8000 -h .
```

- `-v` : mode verbeux (affiche les requêtes reçues)  
- `-f` : reste au premier plan (pratique pour voir les logs)  
- `-p 8000` : écoute sur le port 8000  
- `-h .` : sert les fichiers du dossier courant (`.` = répertoire actuel)  

---

## 2. Créer une page web
Dans le dossier courant, créer un fichier `index.html` :
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Test</title>
  </head>
  <body>
    <main>C'est un test.</main>
  </body>
</html>
```

---

## 3. Vérifier avec `curl`
On peut interroger le serveur :
```sh
curl http://localhost:8000
```
👉 Cela affiche le **code HTML brut**.

---

## 4. Extraire uniquement le texte du `<body>`
On peut chaîner avec `html2text` :
```sh
curl -s http://localhost:8000 | html2text
```
👉 Résultat :
```
C'est un test.
```

---

✅ En résumé :
- BusyBox sert à monter un mini-serveur web sans installer Apache/Nginx.  
- `curl` permet de récupérer le contenu en ligne de commande.  
- Avec un tube (`|`), on peut traiter le HTML pour n’afficher que le texte utile.