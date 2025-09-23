# Gestion des services avec systemd

**systemd** est le système d'initialisation et de gestion des services sous la plupart des distributions Linux modernes. Il remplace l'ancien système SysVinit et offre des fonctionnalités avancées pour démarrer, arrêter, surveiller et gérer les services système.

Les commandes principales s'utilisent via `systemctl`, qui permet de contrôler l'état des services, de les activer/désactiver au démarrage, et bien plus encore.

---

## Tableau des commandes systemctl les plus utiles

| Commande | Description |
| - | - |
| `systemctl list-units --type=service` | Lister tous les services chargés (actifs et inactifs) |
| `systemctl list-units --type=service --state=running` | Lister uniquement les services en cours d'exécution |
| `systemctl list-units --type=service --state=failed` | Lister les services en échec |
| `systemctl list-units --type=service --all` | Lister tous les services (y compris inactifs) |
| `systemctl list-units --type=service --all | grep -i "mot_clé"` | Trouver un service à partir d’un mot-clé |
| `systemctl list-unit-files | grep -i "mot_clé"` | Trouver un fichier de service à partir d’un mot-clé |
| `systemctl status <nom_du_service>` | Afficher le statut détaillé d'un service |
| `systemctl start <nom_du_service>` | Démarrer un service |
| `systemctl stop <nom_du_service>` | Arrêter un service |
| `systemctl restart <nom_du_service>` | Redémarrer un service |
| `systemctl reload <nom_du_service>` | Recharger la configuration d'un service sans interruption |
| `systemctl enable <nom_du_service>` | Activer un service pour qu'il démarre au boot |
| `systemctl disable <nom_du_service>` | Désactiver un service pour qu'il ne démarre pas au boot |
| `systemctl is-enabled <nom_du_service>` | Vérifier si un service est activé au démarrage |
| `systemctl is-active <nom_du_service>` | Vérifier si un service est actuellement actif |
| `systemctl daemon-reload` | Recharger la configuration de systemd après modification des fichiers de service |
| `journalctl -u <nom_du_service>` | Afficher les logs d'un service spécifique |
| `systemctl --failed` | Lister les services en échec |

