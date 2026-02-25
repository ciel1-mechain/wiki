# Installation du serveur http apache2 sous Debian

----
## 🎯 Objectifs et remarques
Installer **Debian** dans **VirtualBox** avec :

- 4 Gio de RAM
- 20 Go de disque
- Installation et configuration du serveur **Apache2**
- On n'utilisera pas la commande `sudo` sous Debian
- Les opérations qui nécessitent des privilèges se feront sous le compte root. (Commande `su -`)


## Notations
**$** indique que la commande doit être lancée en tant qu'utilisateur.  
 **#** indique que la commande doit être lancée en tant que super-utilisateur (root).

## 🖥️ 1. Création de la VM dans VirtualBox

**Configuration machine** :  

  * Dans la configuration réseau de la machine virtuelle sélectionner **accès par pont**.
  * RAM : 4 Gio
  * Disque : 20 Go
  
## 💿 2. Installation de Debian
**1.** Télécharger l’image ISO (choisir la netinstall)

➡️  [ISO Debian](https://www.debian.org/distrib/)

**2.** Procéder à l'installation :

  * Démarrer la VM :
  * Ouvrir les **Paramètres** → **Stockage** → monter l’ISO dans le lecteur optique.
  * Sélectionner **graphical install** puis suivre la procédure indiquée.
  * Nom de votre machine : `srv-web`.
  * Nom utilisateur : `user` et mdp `debian`. Mdp root : `debian`
  * Mettre **local** dans le domaine.
  * Sélectionner **Assisté – utiliser un disque entier**
  * Sélectionner **Tout dans une seule partition**
  * Sélectionner **oui** pour l’application des changements
  * Sélectionner **non** pour analyser un autre cd/dvd (si demandé)
  * Sélectionner **oui** pour l’utilisation d’un miroir réseau
  * Pour le proxy (Mandataire HTTP) laisser vide.
  * Lors de la sélection des logiciels **supprimer les interfaces graphiques**.
  * Sélectionner **oui** pour installer grub ensuite bien sélectionner **/dev/sda**

**3.** Vérifier que les lignes qui contiennent ''deb cdrom ...'' commencent par `#` dans le fichier `/etc/apt/sources.list` 

**4.** Retirer l’ISO après redémarrage.

## 💿 2. Installation du serveur apache2

### Installation du serveur

**1. Installer** apache2 :  
<code bash># apt update && apt upgrade -y</code>  
<code bash># apt install apache2</code>


**2. Vérification du fonctionnement du serveur**  
**Vérifier** le fonctionnement du serveur :  
<code bash># systemctl status apache2</code>

**3. Saisir** dans un navigateur lancé sur la machine sous Linux Mint l'adresse ip du serveur (Commande `ip -4 a` pour obtenir l'adresse IP du serveur). Une page web doit s'afficher.

### Configuration des répertoires

**1. Définir** `www-data` comme proprétaire et groupe auquel le répertoire `/var/www/html` appartient. Utiliser la commande `chown`.

**2. Ajouter** l'utilisateur courant au groupe `www-data`  à l'aide de la commande `usermod` et des options `-a` et `-G`.

**3. Définir** les droits du répertoire `/var/www/html`. Donner les droits `-rwxrwxr-x`.



## ⚙️  3. Administrer votre serveur à distance
### Installation de ssh
**1. Installer** `openssh-server` sur votre machine sous Debian.

**2. Se déconnecter puis se reconnecter.**

### Utilisation 

A partir d'une machine cliente se connecter à la machine Debian. Pour cela, dans un terminal saisir :  
<code bash>$ ssh user@ip-srv-web</code> 
Remplacer ip-srv-web par l'adresse ip du serveur.

Vous êtes maintenant connectés à votre Debian via `ssh`.

### Déposer vos pages sur le serveur
  * A partir de l’explorateur de fichier de la machine cliente, saisir : `sftp://user@ip-srv-web` (Remplacer ip-srv-web par l'adresse ip du serveur).

  * Vous pouvez déposer vos pages html dans `/var/www/html`.   
  * Penser à nommer un fichier `index.html` dans chaque répertoire. 
  * Faire en sorte que tous les fichiers et répertoires dans `/var/www/html` appartiennent à `www-data` (proprétaire et groupe). 

## Compléments 
  * En cas de problème avec le fichier `/etc/apt/sources.list` on peut le modifier comme ci-dessous (Pour debian 12)
  * A adapter à la version de Debian (voir la page [Debian sources.list](https://wiki.debian.org/fr/SourcesList)) :
```
deb http://deb.debian.org/debian bookworm main
deb-src http://deb.debian.org/debian bookworm main

deb http://deb.debian.org/debian-security/ bookworm-security main
deb-src http://deb.debian.org/debian-security/ bookworm-security main

deb http://deb.debian.org/debian bookworm-updates main
deb-src http://deb.debian.org/debian bookworm-updates main

```
