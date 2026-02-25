# Résumé sur Nginx : Fonctionnement, Configuration et Avantages

---

## 1. Introduction à Nginx
Nginx est un **serveur web asynchrone et événementiel**, conçu pour gérer un grand nombre de connexions simultanées avec une faible consommation de ressources. Contrairement à Apache, il utilise une architecture légère et performante.

---

## 2. Architecture de Nginx

### a) Modèle asynchrone et événementiel
- **1 processus maître** : Lancé par `root` pour gérer les workers.
- **Plusieurs processus workers** (1 par CPU par défaut) : Tous s'exécutent sous un utilisateur non privilégié (ex: `www-data`).
- **Pas de processus ou thread par requête** : Un seul worker peut gérer **des milliers de connexions simultanées** grâce à une boucle d'événements.

### b) Avantages
- **Performance** : Gère efficacement un grand nombre de connexions avec peu de ressources.
- **Faible consommation mémoire** : Contrairement à Apache, pas de création de processus/threads par requête.
- **Scalabilité** : Idéal pour les sites à fort trafic.

---

## 3. Gestion des utilisateurs et permissions
- **Processus maître** : Lancé par `root` (pour ouvrir les ports privilégiés).
- **Processus workers** : Tous s'exécutent sous un utilisateur non privilégié (ex: `www-data`).
- **Configuration** :
  ```nginx
  user www-data;
  worker_processes auto;
  ```

---

## 4. Configuration de base

### a) Nombre de workers
Nginx ajuste automatiquement le nombre de workers en fonction des CPU disponibles :
```nginx
worker_processes auto;
```

### b) Gestion des connexions
Chaque worker peut gérer un grand nombre de connexions simultanées :
```nginx
events {
    worker_connections 1024;  # Chaque worker peut gérer 1024 connexions
}
```

---

## 5. Vérification des processus Nginx
Pour lister les processus Nginx en cours d'exécution :
```bash
ps aux | grep nginx
```
**Exemple de sortie :**
```
root      1234  0.0  0.1 123456 7890 ?        Ss   10:00   0:00 nginx: master process
www-data  1235  0.0  0.2 123456 4567 ?        S    10:00   0:00 nginx: worker process
www-data  1236  0.0  0.2 123456 4567 ?        S    10:00   0:00 nginx: worker process
```

---

## 6. Pourquoi choisir Nginx ?
- **Performance** : Idéal pour les sites à **fort trafic** (ex: intranet d'un lycée très fréquenté).
- **Faible consommation** : Moins de mémoire et de CPU qu'Apache pour le même nombre de requêtes.
- **Reverse Proxy** : Peut être utilisé comme reverse proxy devant Apache pour combiner les avantages des deux serveurs.

---

## 7. Commandes utiles pour Nginx

| Besoin                                  | Commande                                                                 |
|-----------------------------------------|--------------------------------------------------------------------------|
| Lister les processus Nginx              | `ps aux | grep nginx`                                              |
| Redémarrer Nginx                        | `sudo systemctl restart nginx`                                         |
| Vérifier la configuration               | `sudo nginx -t`                                                         |
| Voir les logs d'erreur                  | `sudo tail -f /var/log/nginx/error.log`                                |
| Voir les logs d'accès                   | `sudo tail -f /var/log/nginx/access.log`                               |

---

## 8. Comparaison Nginx vs Apache

| Critère               | Apache                          | Nginx                          |
|-----------------------|---------------------------------|--------------------------------|
| **Architecture**      | Multi-processus/threads        | Asynchrone/événementiel        |
| **Utilisateur**       | Bascule vers `www-data` (Prefork)| Workers sous `www-data`        |
| **Performance**       | Bonne (limité par les processus)| Excellente (milliers de connexions) |
| **Compatibilité**     | Tous les modules                | Modules asynchrones            |
| **Cas d'usage**       | Sites simples, compatibilité    | Sites à fort trafic, performance|

---
