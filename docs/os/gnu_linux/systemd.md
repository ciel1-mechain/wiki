# Gestion des services avec systemd

**systemd** est le système d'initialisation et de gestion des services sous la plupart des distributions Linux modernes. Il remplace l'ancien système SysVinit et offre des fonctionnalités avancées pour démarrer, arrêter, surveiller et gérer les services système.

Les commandes principales s'utilisent via `systemctl`, qui permet de contrôler l'état des services, de les activer/désactiver au démarrage, et bien plus encore.

> Remarque : taper simplement `systemctl` équivaut par défaut à `systemctl list-units`, affichant toutes les unités **actives**. L'utilisation explicite de `list-units` est surtout pour être clair ou pour filtrer les types d'unités (services, sockets, timers, etc.).

---

## Tableau des commandes systemctl les plus utiles

| Commande                                                                                         | Description                                                                      |                                                     |
| ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------- | --------------------------------------------------- |
| `systemctl list-units --type=service`                                                            | Lister tous les services **actifs** (équivalent à `systemctl --type=service`)    |                                                     |
| `systemctl list-units --type=service --state=running --no-pager`                                 | Lister uniquement les services en cours d'exécution                              |                                                     |
| `systemctl list-units --type=service --state=running --no-pager --no-legend \| awk '{print $1}'` | Lister uniquement les noms des services actifs d'exécution                       |                                                     |
| `systemctl list-units --type=service --state=failed`                                             | Lister les services en échec                                                     |                                                     |
| `systemctl list-units --type=service --all`                                                      | Lister **tous les services**, y compris les inactifs et morts                    |                                                     |
| `systemctl list-units --all`                                                                     | Lister toutes les unités (services, sockets, timers, etc.), actives ou inactives |                                                     |
| `systemctl list-units --type=service --all         `                                             | grep -i "mot_clé"`                                                               | Trouver un service à partir d’un mot-clé            |
| `systemctl list-unit-files `                                                                     | grep -i "mot_clé"`                                                               | Trouver un fichier de service à partir d’un mot-clé |
| `systemctl status <nom_du_service>`                                                              | Afficher le statut détaillé d'un service                                         |                                                     |
| `systemctl start <nom_du_service>`                                                               | Démarrer un service                                                              |                                                     |
| `systemctl stop <nom_du_service>`                                                                | Arrêter un service                                                               |                                                     |
| `systemctl restart <nom_du_service>`                                                             | Redémarrer un service                                                            |                                                     |
| `systemctl reload <nom_du_service>`                                                              | Recharger la configuration d'un service sans interruption                        |                                                     |
| `systemctl enable <nom_du_service>`                                                              | Activer un service pour qu'il démarre au boot                                    |                                                     |
| `systemctl disable <nom_du_service>`                                                             | Désactiver un service pour qu'il ne démarre pas au boot                          |                                                     |
| `systemctl is-enabled <nom_du_service>`                                                          | Vérifier si un service est activé au démarrage                                   |                                                     |
| `systemctl is-active <nom_du_service>`                                                           | Vérifier si un service est actuellement actif                                    |                                                     |
| `systemctl daemon-reload`                                                                        | Recharger la configuration de systemd après modification des fichiers de service |                                                     |
| `journalctl -u <nom_du_service>`                                                                 | Afficher les logs d'un service spécifique                                        |                                                     |
| `journalctl -xeu <nom_du_service>`                                                               |                                                                                  |                                                     |
| `systemctl --failed`                                                                             | Lister les services en échec                                                     |                                                     |
| `journalctl -u apache2 --no-pager -n 20`                                                         | Afficher les logs d'un service (ex: apache2)                                     |                                                     |
| `cat /lib/systemd/system/apache2.service`                                                        | Vérifier le fichier de configuration d'un service                                |                                                     |
| `ps aux \| grep cron`                                                                            | Voir les processus d'un service (ex: cron)                                       |                                                     |
| `ps -u www-data -o pid,user,group,comm`                                                          | Filtrer par utilisateur (ex: www-data)                                           |                                                     |
| `top -c -o %CPU`                                                                                 | Lister les services par consommation CPU/mémoire                                 |                                                     |
---

## Scripts utiles

### Trouver les services actifs pour un utilisateur donné (ex: www-data)
```bash
for pid in $(ps -u www-data -o pid=); do
    systemctl status $pid 2>/dev/null | grep -q "Loaded:" && systemctl status $pid | head -n 3
done
```

### Vérifier les services sans utilisateur ou groupe défini
```bash
systemctl list-units --type=service --state=running --no-pager | awk '{print $1}' | while read service; do
    systemctl show "$service" -p User,Group 2>/dev/null | grep -q "User=" || echo "Service $service : utilisateur non défini (root par défaut)"
done
```


## Remarques supplémentaires

* `systemctl` sans sous-commande **affiche par défaut les unités actives**, ce qui équivaut à `systemctl list-units`.
* L'option `--all` ne fonctionne **que combinée avec `list-units`** : `systemctl list-units --all` pour lister toutes les unités, actives ou inactives.