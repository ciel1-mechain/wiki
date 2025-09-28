
# Cycle de vie d’un conteneur Alpine avec Docker

## Introduction : pourquoi Alpine ?
Alpine Linux est une distribution **très légère** (environ 5 Mo) souvent utilisée comme base d’images Docker.  
- Elle inclut **BusyBox** pour les commandes Unix de base.  
- Elle possède un gestionnaire de paquets (`apk`) pour installer facilement des logiciels.  
- Son faible poids la rend idéale pour créer des conteneurs applicatifs rapides et sécurisés.

---

## 1. Lancer un nouveau conteneur nommé
```sh
docker run -it --name mon_alpine alpine sh
```
- `--name mon_alpine` : donne un nom explicite au conteneur.
- `-it` : interactif avec terminal.
- `sh` : lance le shell fourni par Alpine (BusyBox).

👉 Quand on quitte (`exit` ou `Ctrl+D`), le conteneur **s’arrête**.

---

## 2. Lister les conteneurs (y compris arrêtés)
```sh
docker ps -a
```
Exemple :
```
CONTAINER ID   IMAGE    COMMAND   STATUS                      NAMES
abc123456789   alpine   "sh"      Exited (0) 2 minutes ago    mon_alpine
```

---

## 3. Redémarrer un conteneur existant
```sh
docker start -ai mon_alpine
```
- `-a` : attacher le terminal
- `-i` : mode interactif

👉 On reprend la session dans le conteneur existant.

---

## 4. Créer un autre conteneur
```sh
docker run -it --name mon_alpine2 alpine sh
```
Chaque appel à `run` crée **un nouveau conteneur** basé sur l’image (il faut donc donner un autre nom si `mon_alpine` existe déjà).

---

## 5. Supprimer un conteneur
```sh
docker rm mon_alpine
```
👉 Supprime le conteneur définitivement (il doit être arrêté).

---

## 6. Différence entre les commandes
- `docker run` = crée **et démarre** un conteneur.
- `docker start` = relance un conteneur déjà créé (arrêté).
- `docker exec` = exécute une commande dans un conteneur en cours d’exécution.
- `docker rm` = supprime un conteneur arrêté.

---

✅ **Résumé pédagogique** :  
- `run` = création + démarrage.  
- `start` = redémarrage.  
- `exec` = commande dans un conteneur actif.  
- `rm` = suppression.  

Ceci illustre bien le **cycle de vie complet d’un conteneur Alpine**.

