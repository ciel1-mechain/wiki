# Commandes à connaître par coeur

## 5 commandes réseaux

``` bash
ip addr
ss -tlnp
ping -c 2 8.8.8.8
nc -zv google.com 443
dig +short github.com
```

## Commande `ss` : socket statistics

- t : tcp
- l : en écoute
- n : numérique (pas le nom du service)
- p : processus

## Commande `nc` : ncat - Concatenate and redirect sockets

- z : statut connexion uniquement
- v : mode verbeux
  