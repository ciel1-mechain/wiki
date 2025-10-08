# 🧾 Fiche d'installation Alpine Linux + Nginx (VirtualBox)

## 🎯 Objectif
Installer **Alpine Linux** dans **VirtualBox** avec :
- 512 Mo de RAM
- 512 Mo de disque (ou plus si gros site web à héberger)
- Uniquement l'utilisateur **root**
- Installation et configuration de **Nginx**

---

## 🖥️ 1. Création de la VM dans VirtualBox

1. **Nouveau > Nom :** `Alpine`
2. **Type :** Linux
3. **Version :** `Other Linux (64-bit)`
4. **Mémoire vive :** `512 Mo`
5. **Disque dur :** `Créer un disque virtuel maintenant`
6. **Type :** `VDI` – **Taille dynamique**
7. **Taille :** `512 Mo`

---

## 💿 2. Installation d'Alpine Linux

### Monter l'image ISO
Télécharger l’image ISO minimale :  
➡️ https://alpinelinux.org/downloads/

Choisir **Standard x86_64**.

Dans VirtualBox :
- Ouvrir les **Paramètres** → **Stockage** → monter l’ISO dans le lecteur optique.

### Démarrer la VM
Dans le shell Alpine, se connecter :
```bash
login: root
```

### Lancer le script d’installation
```bash
setup-alpine
```

Répondre aux questions :
- Keyboard layout : `fr`
- Hostname : `alpine`
- Network : auto (DHCP)
- Root password : définir un mot de passe
- Timezone : `Europe/Paris`
- Proxy : (laisser vide)
- Mirror : choisir automatique (ou `f` pour fastest)
- SSH : `no`
- Disk : `sda`
- Use it for sys : `sys`

⚙️ Attendre la fin de l’installation, puis :
```bash
reboot
```

Retirer l’ISO après redémarrage.

---

## 🔑 3. Première connexion
Se connecter en root :
```bash
login: root
```

Mettre à jour les paquets :
```bash
apk update
apk upgrade
```

---

## 🌐 4. Installation de Nginx

```bash
apk add nginx
```

Créer les répertoires nécessaires :
```bash
mkdir -p /run/nginx
mkdir -p /var/www/localhost/htdocs
```

Vérifier la configuration :
```bash
nginx -t
```

Démarrer le service :
```bash
rc-service nginx start
```

Activer Nginx au démarrage :
```bash
rc-update add nginx default
```

---

## 🧩 5. Configuration minimale de Nginx

Après avoir installé le petit éditeur de texte **nano** avec :

```bash
apk add nano
```

### Fichier : `/etc/nginx/http.d/default.conf`
```nginx
server {
    listen 80;
    server_name localhost;

    root /var/www/localhost/htdocs;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Page de test : `/var/www/localhost/htdocs/index.html`
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Bienvenue sur Alpine + Nginx</title>
</head>
<body>
  <h1>Alpine + Nginx fonctionne ✅</h1>
</body>
</html>
```

Redémarrer Nginx :
```bash
rc-service nginx restart
```

---

## 🔎 6. Vérification

Dans le navigateur de votre machine hôte :
```
http://<adresse_IP_de_la_VM>
```

Pour connaître l’adresse IP :
```bash
ip a
```

Vous devriez voir la page « Alpine + Nginx fonctionne ».
