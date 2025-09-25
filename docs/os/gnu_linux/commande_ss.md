# Guide de la commande `ss` sous Linux

**`ss`** (socket statistics) est un outil puissant pour examiner les sockets et connexions réseau sur un système Linux. Il remplace et est plus rapide que l'ancien `netstat`.

Avec `ss`, vous pouvez lister les connexions TCP/UDP, les sockets d'écoute, les sockets Unix et obtenir des informations détaillées sur chaque connexion.

---

## Syntaxe de base

```bash
ss [options] [filtres]
```

* **Options principales** :

  * `-t` : TCP
  * `-u` : UDP
  * `-l` : Liste les sockets en écoute (listening)
  * `-a` : Tous les sockets (listening + non listening)
  * `-n` : N'affiche pas les noms de service (affiche les numéros de port)
  * `-p` : Affiche le processus utilisant le socket
  * `-s` : Résumé global des sockets

---

## Exemples pratiques

| Commande                  | Description                                                         |
| ------------------------- | ------------------------------------------------------------------- |
| `ss -t`                   | Liste toutes les connexions TCP actives                             |
| `ss -u`                   | Liste toutes les connexions UDP actives                             |
| `ss -l`                   | Liste les sockets en écoute                                         |
| `ss -t -l`                | Liste les ports TCP en écoute                                       |
| `ss -u -l`                | Liste les ports UDP en écoute                                       |
| `ss -a`                   | Liste tous les sockets (écoute et non-écoute)                       |
| `ss -t -n`                | Affiche les connexions TCP avec numéros de port sans résolution DNS |
| `ss -t -p`                | Affiche les connexions TCP et les PID/processus associés            |
| `ss -s`                   | Affiche un résumé global des sockets (statistiques TCP/UDP)         |
| `ss -t state ESTABLISHED` | Liste uniquement les connexions TCP établies                        |
| `ss -o`                   | Affiche les options TCP comme les timers                            |
| `ss -x -a`                | Liste tous les sockets Unix                                         |

---

## Filtres utiles

* Par port :

```bash
ss -t '( dport = :80 or sport = :443 )'
```

* Par adresse :

```bash
ss -t dst 192.168.1.10
```

* Par processus :

```bash
ss -t -p | grep nginx
```

---

