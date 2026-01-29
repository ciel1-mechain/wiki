# La gestion réseau sous GNU/Linux


Linux propose plusieurs outils pour **configurer et gérer les interfaces réseau**. Voici un résumé des principaux outils modernes.

---

## 1. NetworkManager CLI

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

## 2. **systemd-networkd**

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

## 3. **Netplan**

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

## 4. **Résumé comparatif**

| Outil              | Niveau              | Type de configuration                | Usage recommandé            |
| ------------------ | ------------------- | ------------------------------------ | --------------------------- |
| `nmcli`            | CLI Desktop/Serveur | Connexions gérées par NetworkManager | Desktop ou serveurs avec NM |
| `systemd-networkd` | Service système     | Fichiers `.network`                  | Serveurs ou systèmes légers |
| `netplan`          | Front-end YAML      | Génère NM ou systemd                 | Ubuntu/Debian modernes      |

---

### 💡 Remarque

* Les trois outils peuvent coexister **mais ne doivent pas gérer la même interface simultanément**.
* ?
