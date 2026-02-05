# La gestion réseau sous GNU/Linux


Linux propose plusieurs outils pour **configurer et gérer les interfaces réseau**. Voici un résumé des principaux outils modernes.

---
## Comment savoir lequel utiliser ?
```bash
systemctl is-active NetworkManager && echo "→ nmcli"
systemctl is-active systemd-networkd && echo "→ networkctl"
```

Ou avec netplan :
* Netplan est utilisé s’il existe AU MOINS un fichier YAML valide dans /etc/netplan.
```
ls -l /etc/netplan/
sudo netplan get
grep renderer /etc/netplan/*.yaml
```

## NetworkManager CLI

* **Description :** Interface en ligne de commande de **NetworkManager**, pour gérer les connexions réseau (Ethernet, Wi-Fi, VPN…).
* **Fonctions principales :**

  * Lister les interfaces et connexions :

    ```bash
    nmcli device status
    ```
  * Activer / désactiver une interface :

    ```bash
    nmcli device connect eth0
    nmcli device disconnect eth0
    ```
  * Gérer les connexions (IP statique, DHCP) :

    ```bash
    nmcli connection add type ethernet ifname eth0 con-name "lan" ip4 192.168.1.100/24 gw4 192.168.1.1
    nmcli connection up "lan"
    ```
* **Avantages :**

  * Simple et rapide pour les utilisateurs Desktop et serveurs avec NetworkManager.
  * Supporte Wi-Fi et VPN nativement.

---

## **systemd-networkd**

* **Description :** Service **système de `systemd`** pour gérer les interfaces réseau.
* **Fichiers de configuration :**

  * Situés dans `/etc/systemd/network/`
  * Exemple pour une interface Ethernet en DHCP (`eth0.network`) :

    ```ini
    [Match]
    Name=eth0

    [Network]
    DHCP=yes
    ```
* **Commandes utiles :**

  ```bash
  systemctl enable systemd-networkd
  systemctl start systemd-networkd
  networkctl status
  ```
* **Avantages :**

  * Léger et intégré à `systemd`
  * Idéal pour les serveurs ou les systèmes sans interface graphique.

---

## **Netplan**

* **Description :** Outil **Ubuntu / Debian moderne** pour déclarer la configuration réseau en YAML.
* **Fichiers de configuration :**

  * `/etc/netplan/*.yaml`
  * Exemple pour configurer DHCP sur Ethernet :

    ```yaml
    network:
      version: 2
      ethernets:
        eth0:
          dhcp4: yes
    ```
* **Application de la configuration :**

  ```bash
  sudo netplan apply
  ```
* **Avantages :**

  * Syntaxe claire (YAML)
  * Peut générer la configuration pour `NetworkManager` ou `systemd-networkd` selon la directive `renderer`.

---

## **Résumé comparatif**

| Outil              | Niveau              | Type de configuration                | Usage recommandé            |
| ------------------ | ------------------- | ------------------------------------ | --------------------------- |
| `nmcli`            | CLI Desktop/Serveur | Connexions gérées par NetworkManager | Desktop ou serveurs avec NM |
| `systemd-networkd` | Service système     | Fichiers `.network`                  | Serveurs ou systèmes légers |
| `netplan`          | Front-end YAML      | Génère NM ou systemd                 | Ubuntu/Debian modernes      |

---
| Besoin / Action | nmcli (NetworkManager) | networkctl (systemd-networkd) | ip (outil bas niveau) |
|-----------------|------------------------|--------------------------------|------------------------|
| 🔍 Lister interfaces | `nmcli d` | `networkctl list` | `ip link` |
| 📡 Statut global | `nmcli g` | `networkctl status` | `ip -br a` |
| 🔎 Détails interface | `nmcli d show enp0s3` | `networkctl status enp0s3` | `ip a show enp0s3` |
| 🌐 Voir IP | `nmcli -p d show` | `networkctl status` | `ip a` |
| 🧭 Voir routes | `nmcli d show \| grep ROUTE` | `networkctl status` | `ip r` |
| 🧠 Voir DNS | `nmcli d show \| grep DNS` | `resolvectl status` | `resolvectl status` |
| 🔌 Activer interface | `nmcli d connect enp0s3` | `networkctl up enp0s3` | `ip link set enp0s3 up` |
| 🔕 Désactiver interface | `nmcli d disconnect enp0s3` | `networkctl down enp0s3` | `ip link set enp0s3 down` |
| 🔄 Recharger config | `nmcli d reapply enp0s3` | `systemctl restart systemd-networkd` | ❌ |
| ✏️ IP temporaire | `nmcli d set enp0s3 ipv4.addresses …` | ❌ | `ip addr add 192.168.1.20/24 dev enp0s3` |
| 🧪 Supprimer IP | `nmcli d set … ""` | ❌ | `ip addr del 192.168.1.20/24 dev enp0s3` |
| 🏠 IP statique persistante | `nmcli c mod` | fichier `.network` | ❌ |
| 🌍 DHCP | `nmcli c mod ipv4.method auto` | `DHCP=yes` | ❌ |
| 🧠 DNS persistant | `nmcli c mod ipv4.dns` | `DNS=` dans `.network` | ❌ |
| 📂 Fichiers config | `/etc/NetworkManager/` | `/etc/systemd/network/` | ❌ |
| 🧪 Test sans couper | ❌ | ❌ | ❌ |
| 📶 Scan Wi-Fi | `nmcli dev wifi list` | ❌ | `iw dev wlan0 scan` |
| 🔐 Connexion Wi-Fi | `nmcli dev wifi connect` | wpa_supplicant | wpa_supplicant |
| 🔁 Auto-connect Wi-Fi | oui | service systemd | ❌ |
| 🔧 VPN | oui | ❌ | ❌ |
| 🔎 Diagnostic rapide | `nmcli d status` | `networkctl list` | `ip -br a` |
| 🧠 Source de vérité | NetworkManager | systemd | kernel |
| ⚡ Changements dynamiques | excellent | limité | oui (non persistant) |
| 🧩 Persistance | profils | fichiers | non |

### 💡 Remarque

* Les trois outils peuvent coexister **mais ne doivent pas gérer la même interface simultanément**.
* ip parle qu noyau
* nmcli parle à NetworkManager
* networkctl parle à systemd
