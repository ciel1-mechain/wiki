# Gestion réseau sous GNU/Linux

---

## 1. Identifier l'outil actif

```bash
systemctl is-active NetworkManager && echo "→ nmcli"
systemctl is-active systemd-networkd && echo "→ networkctl"
```

Avec Netplan :
```bash
ls -l /etc/netplan/          # existe ? → Netplan actif
sudo netplan get             # affiche la config active
grep renderer /etc/netplan/*.yaml  # voir le backend utilisé
```

> Les trois outils peuvent coexister **mais ne doivent pas gérer la même interface simultanément**.

---

## 2. Architecture

```
Applications / utilisateur
        │
    Netplan (front-end YAML, Ubuntu/Debian)
        │
   ┌────┴────┐
   │         │
systemd-   NetworkManager
networkd    (nmcli)
   │         │
   └────┬────┘
        │
   noyau Linux (ip, iproute2)
```

| Outil | Rôle | Source de vérité |
|---|---|---|
| `ip` | outil bas niveau, parle au **noyau** | kernel |
| `networkctl` | parle à **systemd-networkd** | systemd |
| `nmcli` | parle à **NetworkManager** | NetworkManager |
| `netplan` | front-end YAML, génère la config pour NM ou systemd | fichiers YAML |

---

## 3. Netplan

**Front-end unifié** pour configurer le réseau sur Ubuntu/Debian. Utilise des fichiers YAML dans `/etc/netplan/` et délègue à `systemd-networkd` ou `NetworkManager` selon le `renderer`.

### Fichiers de configuration

```yaml
# /etc/netplan/01-config.yaml

# IP statique avec systemd-networkd
network:
  version: 2
  renderer: networkd        # ou NetworkManager
  ethernets:
    eth0:
      addresses: [192.168.1.100/24]
      gateway4: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]

# DHCP
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: yes
```

### Commandes

| Commande | Description |
|---|---|
| `sudo netplan apply` | applique la configuration |
| `sudo netplan --debug apply` | applique avec logs détaillés |
| `sudo netplan get` | affiche la config active |
| `sudo netplan try` | applique temporairement (annulation auto si pas confirmé) |

---

## 4. systemd-networkd

**Backend léger** intégré à systemd. Idéal pour les serveurs et systèmes sans interface graphique. Géré via des fichiers `.network` dans `/etc/systemd/network/`.

### Fichier de configuration

```ini
# /etc/systemd/network/10-eth0.network

[Match]
Name=eth0

[Network]
Address=192.168.1.100/24
Gateway=192.168.1.1
DNS=8.8.8.8
DNS=8.8.4.4

# DHCP à la place :
# DHCP=yes
```

### Commandes

| Commande | Description |
|---|---|
| `systemctl enable systemd-networkd` | active au démarrage |
| `systemctl start systemd-networkd` | démarre le service |
| `systemctl restart systemd-networkd` | redémarre / recharge la config |
| `networkctl list` | liste les interfaces |
| `networkctl status` | état global |
| `networkctl status enp0s3` | détails d'une interface |
| `networkctl up enp0s3` | active une interface |
| `networkctl down enp0s3` | désactive une interface |
| `resolvectl status` | voir les DNS |

---

## 5. NetworkManager (`nmcli`)

**Backend avancé** pour les connexions dynamiques (Wi-Fi, VPN, bonds, VLANs). Utilisé par défaut sur les distributions Desktop.

### Commandes

| Commande | Description |
|---|---|
| `nmcli d` | liste les interfaces (raccourci) |
| `nmcli device status` | état des interfaces |
| `nmcli device show enp0s3` | détails d'une interface |
| `nmcli device connect enp0s3` | active une interface |
| `nmcli device disconnect enp0s3` | désactive une interface |
| `nmcli device reapply enp0s3` | recharge la config sans déconnecter |
| `nmcli g` | état global NetworkManager |
| `nmcli connection show` | liste les connexions configurées |
| `nmcli connection up <nom>` | active une connexion |
| `nmcli connection down <nom>` | désactive une connexion |
| `nmcli connection modify <nom> ipv4.dns "8.8.8.8"` | modifie les DNS |
| `nmcli connection modify <nom> ipv4.method auto` | passe en DHCP |
| `nmcli connection add type ethernet ifname eth0 con-name "lan" ip4 192.168.1.100/24 gw4 192.168.1.1` | crée une connexion statique |
| `nmcli dev wifi list` | liste les réseaux Wi-Fi |
| `nmcli dev wifi connect <SSID> password <mdp>` | connexion Wi-Fi |
| `nmcli d show \| grep DNS` | voir les DNS |
| `nmcli d show \| grep ROUTE` | voir les routes |

---

## 6. Outil bas niveau : `ip`

Parle directement au noyau. Les changements sont **non persistants** (perdus au redémarrage).

| Commande | Description |
|---|---|
| `ip link` | liste les interfaces |
| `ip -br a` | état résumé des interfaces |
| `ip a` | voir les IPs |
| `ip a show enp0s3` | détails d'une interface |
| `ip r` | voir les routes |
| `ip link set enp0s3 up` | active une interface |
| `ip link set enp0s3 down` | désactive une interface |
| `ip addr add 192.168.1.20/24 dev enp0s3` | ajoute une IP temporaire |
| `ip addr del 192.168.1.20/24 dev enp0s3` | supprime une IP |

---

## 7. Tableau comparatif par action

| Action | nmcli | networkctl | ip |
|---|---|---|---|
| Lister interfaces | `nmcli d` | `networkctl list` | `ip link` |
| Statut global | `nmcli g` | `networkctl status` | `ip -br a` |
| Détails interface | `nmcli d show enp0s3` | `networkctl status enp0s3` | `ip a show enp0s3` |
| Voir IP | `nmcli -p d show` | `networkctl status` | `ip a` |
| Voir routes | `nmcli d show \| grep ROUTE` | `networkctl status` | `ip r` |
| Voir DNS | `nmcli d show \| grep DNS` | `resolvectl status` | `resolvectl status` |
| Activer interface | `nmcli d connect enp0s3` | `networkctl up enp0s3` | `ip link set enp0s3 up` |
| Désactiver interface | `nmcli d disconnect enp0s3` | `networkctl down enp0s3` | `ip link set enp0s3 down` |
| Recharger config | `nmcli d reapply enp0s3` | `systemctl restart systemd-networkd` | ❌ |
| IP temporaire | ❌ | ❌ | `ip addr add 192.168.1.20/24 dev enp0s3` |
| IP statique persistante | `nmcli c mod` | fichier `.network` | ❌ |
| DHCP | `nmcli c mod ipv4.method auto` | `DHCP=yes` dans `.network` | ❌ |
| DNS persistant | `nmcli c mod ipv4.dns` | `DNS=` dans `.network` | ❌ |
| Fichiers config | `/etc/NetworkManager/` | `/etc/systemd/network/` | ❌ |
| Scan Wi-Fi | `nmcli dev wifi list` | ❌ | `iw dev wlan0 scan` |
| Connexion Wi-Fi | `nmcli dev wifi connect` | wpa_supplicant | wpa_supplicant |
| VPN | ✅ | ❌ | ❌ |
| Persistance | profils | fichiers | ❌ non persistant |

---

## 8. Comparaison systemd-networkd vs NetworkManager en production

| Critère | systemd-networkd | NetworkManager |
|---|---|---|
| **Type d'environnement** | Serveurs statiques (web, DB, cache) | Serveurs dynamiques (VPN, Wi-Fi, bonds) |
| **Complexité réseau** | Faible (IP statique, routes) | Élevée (Wi-Fi, VPN, basculement) |
| **Outils** | Fichiers `.network` + `networkctl` | `nmcli`, `nmtui`, Netplan |
| **Stabilité** | Très stable, peu de dépendances | Stable mais plus complexe |
| **Automatisation** | Idéal pour Ansible/Puppet/Chef | Possible via `nmcli` |
| **Cloud/Conteneurs** | Intégration native `cloud-init` | Supporté mais moins léger |

### Recommandations

- **80% des cas (serveurs statiques)** → `systemd-networkd` + Netplan : simplicité, stabilité.
- **20% des cas (besoins dynamiques)** → `NetworkManager` + `nmcli` : Wi-Fi, VPN, VLANs, bonds.

---

## 10. Bonding (agrégation d'interfaces)

Un **bond** = regroupement de plusieurs interfaces réseau en une seule interface logique.

**Objectifs :**
- **Haute disponibilité** → si une interface tombe, l'autre prend le relais
- **Agrégation de bande passante** → cumul des débits

```
eth0 ──┐
        ├── bond0 (192.168.1.100)  → switch
eth1 ──┘
```

### Modes courants

| Mode | Nom | Description |
|---|---|---|
| 0 | `balance-rr` | round-robin, agrégation de bande passante |
| 1 | `active-backup` | une seule active, l'autre en secours ✅ le plus utilisé |
| 2 | `balance-xor` | répartition par hash MAC |
| 4 | `802.3ad` | LACP, agrégation standard (switch doit supporter) |
| 6 | `balance-alb` | équilibrage adaptatif |

### Configuration Netplan

```yaml
network:
  version: 2
  bonds:
    bond0:
      interfaces: [eth0, eth1]
      parameters:
        mode: active-backup
      addresses: [192.168.1.100/24]
      gateway4: 192.168.1.1
```

### Configuration nmcli

```bash
# Créer le bond
nmcli connection add type bond con-name bond0 ifname bond0 bond.options "mode=active-backup"

# Ajouter les interfaces esclaves
nmcli connection add type ethernet con-name bond0-eth0 ifname eth0 master bond0
nmcli connection add type ethernet con-name bond0-eth1 ifname eth1 master bond0

# Configurer l'IP
nmcli connection modify bond0 ipv4.addresses 192.168.1.100/24 ipv4.gateway 192.168.1.1 ipv4.method manual

# Activer
nmcli connection up bond0
```

> Très utilisé en production sur les serveurs critiques pour la redondance réseau.


### Vers NetworkManager

```yaml
# /etc/netplan/01-config.yaml
network:
  version: 2
  renderer: NetworkManager
```
```bash
sudo netplan apply
```

### Vers systemd-networkd

```yaml
# /etc/netplan/01-config.yaml
network:
  version: 2
  renderer: networkd
```
```bash
sudo nmcli dev set eth0 managed no   # libérer l'interface de NM
sudo netplan apply
```
