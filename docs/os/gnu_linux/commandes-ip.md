# Résumé des commandes `ip` (iproute2)

## 1. Gestion des interfaces (`ip link`)
| Commande                          | Description                                      |
|-----------------------------------|--------------------------------------------------|
| `ip link show`                    | Affiche toutes les interfaces et leur état.      |
| `ip link set <interface> up`      | Active une interface.                            |
| `ip link set <interface> down`    | Désactive une interface.                        |
| `ip link set <interface> mtu <valeur>` | Modifie la taille MTU.                   |

---

## 2. Gestion des adresses IP (`ip addr`)
| Commande                                      | Description                                      |
|-----------------------------------------------|--------------------------------------------------|
| `ip addr show` ou `ip a`                       | Affiche les adresses IP de toutes les interfaces.|
| `ip addr add <IP>/<masque> dev <interface>`    | Ajoute une adresse IP à une interface.          |
| `ip addr del <IP>/<masque> dev <interface>`    | Supprime une adresse IP d'une interface.        |

---

## 3. Gestion des routes et passerelles (`ip route`)
| Commande                                      | Description                                      |
|-----------------------------------------------|--------------------------------------------------|
| `ip route show`                               | Affiche la table de routage.                     |
| `ip route add <réseau> via <gateway>`         | Ajoute une route via une passerelle.            |
| `ip route add default via <gateway>`         | Ajoute une route par défaut.                     |
| `ip route del <réseau>`                       | Supprime une route.                              |

---

## 4. Gestion du cache ARP/NDP (`ip neigh`)
| Commande                                      | Description                                      |
|-----------------------------------------------|--------------------------------------------------|
| `ip neigh show`                               | Affiche le cache ARP/NDP.                        |
| `ip neigh add <IP> lladdr <MAC> dev <interface>` | Ajoute une entrée ARP manuellement.          |
| `ip neigh del <IP> dev <interface>`           | Supprime une entrée ARP.                        |

---

## 5. Gestion des règles de routage (`ip rule`)
| Commande                                      | Description                                      |
|-----------------------------------------------|--------------------------------------------------|
| `ip rule show`                                | Affiche les règles de routage.                   |
| `ip rule add from <IP> lookup <table>`        | Ajoute une règle de routage.                    |
| `ip rule del from <IP> lookup <table>`        | Supprime une règle de routage.                  |

---

## 6. Gestion des tunnels (`ip tunnel`)
| Commande                                      | Description                                      |
|-----------------------------------------------|--------------------------------------------------|
| `ip tunnel show`                              | Affiche les tunnels configurés.                  |
| `ip tunnel add <nom> mode <type> remote <IP> local <IP>` | Ajoute un tunnel.          |
| `ip tunnel del <nom>`                         | Supprime un tunnel.                              |

---

## 7. Gestion des adresses multicast (`ip maddr`)
| Commande                                      | Description                                      |
|-----------------------------------------------|--------------------------------------------------|
| `ip maddr show`                               | Affiche les adresses multicast.                  |
| `ip maddr add <IP> dev <interface>`           | Ajoute une adresse multicast.                    |
| `ip maddr del <IP> dev <interface>`           | Supprime une adresse multicast.                  |

---

## 8. Commandes IPv6
| Commande                                      | Description                                      |
|-----------------------------------------------|--------------------------------------------------|
| `ip -6 addr show`                             | Affiche les adresses IPv6.                      |
| `ip -6 route add <réseau>/<masque> via <gateway>` | Ajoute une route IPv6.      |

---

## 9. Surveillance des changements (`ip monitor`)
| Commande                                      | Description                                      |
|-----------------------------------------------|--------------------------------------------------|
| `ip monitor`                                  | Surveille les changements réseau en temps réel.  |
