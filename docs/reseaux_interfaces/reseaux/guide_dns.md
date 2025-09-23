# Guide DNS

##  1. Concepts fondamentaux du DNS

### Qu'est ce que le DNS ?
Le **DNS (Domain Name System)** est le système qui traduit les **noms de domaine** (ex: `example.com`) en **adresses IP** (ex: `93.184.216.34`).  
C'est l’équivalent d’un **annuaire téléphonique** d’Internet.
Le DNS est une **base de données distribuée** organisée de façon **hiérarchique** 

### Base de données distribuée
- Le DNS est une **base de données distribuée** :
    - **Base de données** : une collection de **données** ayant une structure similaire.
    - **Distribuée** : les données sont réparties sur un ensemble de machines physiques.
- Ces **données** sont appelées enregistrements, nommés **Resource Records (RR)** pour le DNS.
- Chaque RR a une structure comprenant :
    - **Nom** : le nom du nœud ou domaine
    - **Type** : type d’enregistrement (`A`, `AAAA`, `CNAME`, `MX`, `NS`, `PTR`, etc.)
    - **Valeur** : l’information associée (IP, nom canonique, etc.)
    - **TTL** : Time To Live, durée de validité du cache
- Exemples de RR : `A`, `AAAA`, `CNAME`, `MX`, `NS`, `PTR`.

!!! note "Types d'enregistrements DNS"

    -   **A** : adresse IPv4.
    -   **AAAA** : adresse IPv6.
    -   **CNAME** : alias, redirection vers un autre nom de domaine.
    -   **MX** : serveur de messagerie (Mail eXchanger).
    -   **NS** : serveur de noms faisant autorité pour la zone.
    -   **PTR** : pointeur, utilisé pour la résolution inverse (IP → nom).
    -   **SOA** : Start Of Authority, informations de base sur la zone.
    -   **TXT** : texte libre (souvent utilisé pour SPF, DKIM,
        vérifications).
    -   **SRV** : localisation d'un service (ex: SIP, XMPP).
    -   **CAA** : Certification Authority Authorization (contrôle des
        certificats TLS).
 
###  Espace de noms DNS
- C’est l’**arborescence hiérarchique** qui organise tous les noms sur Internet.  
- Chaque niveau est séparé par un point (`.`).  
- Exemple : `www.example.com.` fait partie de l’espace de noms DNS.

### Racine DNS
- Niveau le plus haut de l’arborescence DNS.
- Représentée par un simple **.** (point).
- Les serveurs racine (root servers) sont responsables de cette partie.

### Noeud DNS, Domaine et nom de Domaine
- Un noeud est une position dans l'arbre.
- Un domaine est un nœud qui peut contenir des sous-domaines et éventuellement une zone DNS.
- Un nom de domaine identifie un nœud dans l’arborescence.
- Chaque domaine correspond à une **zone d’autorité**.
  
!!! example "Exemple" 
    - Domaine racine : `.`  
    - Domaine `.com` : c’est un domaine de premier niveau (TLD)   
      **TLD (Top-Level Domain)** : `.com`, `.org`, `.fr`, etc.
    - Domaine `.com` contient les domaines `example.com`, `google.com`, etc.  
      Ce sont des sous domaines de `.com`.
    - Domaine `example.com` contient `www.example.com`, `mail.example.com`, etc.
  
### FQDN (Fully Qualified Domain Name)
- C’est le **nom de domaine complet** qui inclut **tous les niveaux** jusqu’à la racine (`.`).  
!!! example "Exemple"  
    - `www.example.com.` est un **FQDN** (note le point final représentant la racine).  
    - `www.example.com` (sans point) est souvent considéré comme un FQDN implicite.

### Hôte
- Extrémité d'une branche, correspond à une machine ou une entité du réseau.
- un FQDN peut identifier un hôte, mais également un service ou un alias (CNAME).

### Zones DNS
Une **zone DNS** est une portion de l’espace de noms gérée par un serveur.  
- Une zone contient des **Resource Records (RR)**.  
- Exemple : la zone `example.com` peut définir les enregistrements `A`, `MX`, etc.  
- Une zone DNS peut contenir plusieurs sous-domaines.
- Un sous-domaine peut être délégué à une zone séparée sur un autre serveur.

### Serveurs DNS
- **Serveurs racines** : point de départ de la résolution, connaissent les adresses des serveurs des TLD. Il existe **13 ensembles** de serveurs racine répartis dans le monde. 
- **Serveur primaire (master)** : contient la copie officielle de la zone.  
- **Serveurs secondaires (slaves)** : reçoivent des copies du primaire pour la redondance.  
- **Serveurs intermédiaires / Résolveurs DNS (caches)** : 
    - Ne font pas partie de la hiérarchie DNS.
    - Servent de point d’entrée pour les clients DNS des machines : ils reçoivent les requêtes des clients et résolvent les noms en interrogeant d’autres serveurs DNS (racines, TLD, zones).
    - Ils stockent temporairement les réponses dans un cache pour accélérer les requêtes futures.
    - Exemple : Google Public DNS (8.8.8.8)

### Authoritative Answer
Un serveur DNS est **authoritative** pour une zone quand il fournit une réponse officielle depuis sa base locale (et pas un cache).  

---

## 2. Structure et fonctionnement d'un message DNS

### Types de requêtes DNS

!!! note "Requête itérative"
    Le serveur DNS ne fait pas tout le travail; il donne l’adresse d’un autre serveur à interroger. 

!!! note "Requête récursive"
    Le serveur DNS fait tout le travail; il donne une réponse complète.

### Principe de la résolution de nom

-   Le client demande au résolveur DNS de trouver la réponse complète.\
-   Le résolveur utilise des **requêtes itératives** auprès d'autres
    serveurs si nécessaire.\
-   Le résolveur retourne finalement la réponse complète au client.

---

## Structure d'un message DNS

Chaque message DNS contient :

- **En-tête** (Header, 12 octets).
- **Questions** (nom + type demandé).
- **Réponses** (enregistrements trouvés).
- **Authorities** (serveurs faisant autorité).
- **Additionals** (informations supplémentaires).

### Format de l'en-tête (12 octets)

    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                Identification (16 bits)       |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |QR|   Opcode  |AA|TC|RD|RA| Z|AD|CD|   RCODE   |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                QDCOUNT (16 bits)              |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                ANCOUNT (16 bits)              |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                NSCOUNT (16 bits)              |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+
    |                ARCOUNT (16 bits)              |
    +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+

### Description des champs

-   **Identification (16 bits)** : numéro unique pour associer une
    réponse à une requête.
-   **Flags (16 bits)** :
    -   **QR (1 bit)** : 0 = requête, 1 = réponse.
    -   **Opcode (4 bits)** : type de requête (0 = standard, 1 =
        inverse, 2 = status, ...).
    -   **AA (1 bit)** : réponse faisant autorité.
    -   **TC (1 bit)** : réponse tronquée (si \> 512 octets en UDP).
    -   **RD (1 bit)** : récursion désirée par le client.
    -   **RA (1 bit)** : récursion disponible (serveur capable de
        récursion).
    -   **Z (3 bits)** : réservé, toujours 0.
    -   **AD (1 bit)** : données authentifiées (DNSSEC).
    -   **CD (1 bit)** : vérification désactivée (DNSSEC).
    -   **RCODE (4 bits)** : code retour (0 = OK, 1 = format invalide, 2
        = échec serveur, 3 = nom inexistant, ...).
-   **QDCOUNT** : nombre de questions.
-   **ANCOUNT** : nombre de réponses.
-   **NSCOUNT** : nombre d'enregistrements dans la section Authority.
-   **ARCOUNT** : nombre d'enregistrements dans la section Additional.

------------------------------------------------------------------------

## Exemple concret : requête pour `www.example.com` (Type A)

!!! important "DNS et modèle OSI"
    📌 DNS est transporté par UDP/TCP sur IP. 

    📌 Dans le modèle OSI :  

    - **Couche Application (7)**   
        DNS est avant tout un service applicatif (comme HTTP, SMTP, FTP).  
        Il fournit la traduction nom de domaine ↔ adresse IP aux applications.

    - **Couche Transport (4)**   
        DNS s’appuie sur UDP (port 53) la plupart du temps.

    - **Couche Réseau (3)**  
        Comme tout trafic IP, les paquets DNS sont encapsulés dans IPv4/IPv6.

**Requête DNS standard (Octets du protocole DNS uniquement)** :

    AA BB 01 00 00 01 00 00 00 00 00 00
    03 77 77 77 07 65 78 61 6D 70 6C 65
    03 63 6F 6D 00 00 01 00 01



### Décomposition :

-   **AA BB** → Identification (aléatoire choisi par le client).
-   **01 00** → Flags (QR=0, RD=1 → requête récursive).
-   **00 01** → QDCOUNT = 1 (une seule question).
-   **00 00** → ANCOUNT = 0 (aucune réponse, c'est une requête).
-   **00 00** → NSCOUNT = 0.
-   **00 00** → ARCOUNT = 0.
-   **03 77 77 77 ... 63 6F 6D 00** → Nom demandé : `www.example.com`.
-   **00 01** → Type A (IPv4).
-   **00 01** → Classe IN (Internet).

------------------------------------------------------------------------