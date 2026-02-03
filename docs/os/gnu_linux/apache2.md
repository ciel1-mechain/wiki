# Apache : Fonctionnement, Modes et Sécurité

---

## 1. Introduction à Apache
Apache est un **serveur web** open source utilisé pour héberger des sites web. Il fonctionne en **gérant des requêtes HTTP** et en servant des pages web aux utilisateurs.

---

## 2. Fonctionnement général d'Apache

### a) Processus parent et enfants
- **Processus parent** : Lancé par `root` pour ouvrir les ports privilégiés (comme le port 80 ou 443).
- **Processus enfants** : Créés pour traiter les requêtes. Ils basculent généralement vers un utilisateur peu privilégié (comme `www-data`) pour des raisons de sécurité.

### b) Pourquoi ce modèle ?
- **Sécurité** : Limiter les privilèges des processus exposés au réseau.
- **Performance** : Réutiliser les processus pour traiter plusieurs requêtes successives.

---

## 3. Modes de fonctionnement d'Apache

### a) Mode Prefork (multi-processus)
- **Un processus par requête** : Chaque processus enfant traite une requête à la fois.
- **Utilisateur** : Les processus enfants basculent vers `www-data` après le démarrage.
- **Avantages** : Compatible avec tous les modules Apache (comme `mod_php`).
- **Inconvénients** : Consommation mémoire plus élevée.

**Exemple de configuration :**
```apache
<IfModule mpm_prefork_module>
    StartServers             5
    MinSpareServers          5
    MaxSpareServers         10
    MaxRequestWorkers       150
    MaxConnectionsPerChild   0
</IfModule>
```

---

### b) Mode Worker (multi-threads)
- **Un processus avec plusieurs threads** : Chaque thread traite une requête.
- **Utilisateur** : Les processus et threads restent sous `root` (pas de basculement vers `www-data`).
- **Avantages** : Meilleure performance pour les connexions simultanées.
- **Inconvénients** : Certains modules (comme `mod_php`) ne sont pas compatibles. Nécessite l'utilisation de **PHP-FPM** pour exécuter PHP sous `www-data`.

**Exemple de configuration :**
```apache
<IfModule mpm_worker_module>
    StartServers             2
    MinSpareThreads         25
    MaxSpareThreads         75
    ThreadLimit              64
    ThreadsPerChild         25
    MaxRequestWorkers       150
    MaxConnectionsPerChild   0
</IfModule>
```

---

## 4. Vérification des processus Apache

### a) Lister les processus Apache
```bash
ps aux | grep apache2
```

**Exemple de sortie (mode Prefork) :**
```
root      1234  0.0  0.5 123456 7890 ?        Ss   10:00   0:00 /usr/sbin/apache2
www-data  1235  0.0  0.3 123456 4567 ?        S    10:00   0:00 /usr/sbin/apache2
www-data  1236  0.0  0.3 123456 4567 ?        S    10:00   0:00 /usr/sbin/apache2
```

**Exemple de sortie (mode Worker) :**
```
root      1234  1 1234  1  0 10:00 ?        00:00:00 /usr/sbin/apache2
root      1235 1234 1234  1  0 10:00 ?        00:00:00 /usr/sbin/apache2
root      1235 1234 1236  1  0 10:00 ?        00:00:00 /usr/sbin/apache2
```

---

### b) Vérifier le mode actif
```bash
apache2ctl -V | grep "Server MPM"
```

**Exemple de sortie :**
```
Server MPM: prefork
```
ou
```
Server MPM: worker
```

---

## 5. Sécurité et bonnes pratiques

### a) Mode Prefork
- **Sécurité** : Les processus enfants s'exécutent sous `www-data`, limitant les risques.
- **Compatibilité** : Fonctionne avec tous les modules Apache.

### b) Mode Worker
- **Sécurité** : Les threads s'exécutent sous `root`. Utiliser **PHP-FPM** pour exécuter PHP sous `www-data`.
- **Configuration de PHP-FPM** :
  ```bash
  sudo apt install php-fpm
  sudo a2enmod proxy_fcgi setenvif
  sudo a2enconf php7.x-fpm
  sudo systemctl restart apache2
  ```

---

## 6. Configuration et optimisation

### a) Ajuster le nombre de processus/threads
- **Mode Prefork** : Augmenter `MaxRequestWorkers` pour permettre plus de processus enfants.
- **Mode Worker** : Ajuster `ThreadsPerChild` et `MaxRequestWorkers` pour optimiser les threads.

### b) Redémarrer Apache après modification
```bash
sudo systemctl restart apache2
```

---

## 7. Résumé comparatif

| Élément                | Mode Prefork                     | Mode Worker                      |
|------------------------|----------------------------------|----------------------------------|
| **Type**               | Multi-processus                 | Multi-threads                    |
| **Utilisateur**        | Processus enfants : `www-data`  | Processus/threads : `root`      |
| **Sécurité**           | Plus sécurisé                    | Moins sécurisé (nécessite PHP-FPM) |
| **Performance**        | Moins efficace en mémoire       | Plus efficace pour les connexions simultanées |
| **Compatibilité**      | Tous les modules Apache          | Modules thread-safe uniquement   |

---

## 8. Cas pratique pour un lycée
- **Site web du lycée** : Utiliser le mode **Prefork** pour une compatibilité maximale avec les modules.
- **Intranet avec beaucoup de connexions** : Utiliser le mode **Worker** avec PHP-FPM pour une meilleure performance.
- **Optimisation** : Ajuster `MaxRequestWorkers` en fonction du trafic attendu.

---

## 9. Commandes utiles

| Besoin                                  | Commande                                                                 |
|-----------------------------------------|--------------------------------------------------------------------------|
| Lister les processus Apache             | `ps aux | grep apache2`                                            |
| Vérifier le mode MPM                    | `apache2ctl -V | grep "Server MPM"`                                      |
| Redémarrer Apache                       | `sudo systemctl restart apache2`                                        |
| Voir les logs d'Apache                  | `journalctl -u apache2 --no-pager -n 20`                                |
| Configurer PHP-FPM                      | `sudo apt install php-fpm; sudo a2enmod proxy_fcgi setenvif; sudo a2enconf php7.x-fpm` |

---
