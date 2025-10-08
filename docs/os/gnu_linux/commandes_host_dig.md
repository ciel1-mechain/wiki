# Guide : Commandes `host` et `dig` sous Linux

---

## 1. Introduction
Les commandes **`host`** et **`dig`** permettent d’interroger le système de noms de domaine (**DNS**) pour obtenir des informations sur :  
- les adresses IP associées à un nom de domaine,  
- les noms de domaine associés à une adresse IP (**résolution inverse**),  
- les enregistrements DNS spécifiques (A, AAAA, MX, NS, CNAME, PTR, etc.),  
- la résolution pas à pas d’un domaine.  

Elles sont particulièrement utiles pour :  
✅ le **diagnostic réseau**,  
✅ la **vérification de configuration DNS**,  
✅ l’**analyse de propagation DNS**.

---

## 2. La commande `host`

### Syntaxe
```bash
host [options] nom_domaine [serveur_dns]
```

### Exemples
1. Résolution simple d’un nom de domaine :  
```bash
host www.example.com
```
👉 Retourne l’adresse IP associée (par défaut IPv4 et IPv6 si disponible).

2. Résolution inverse (IP → nom de domaine) :  
```bash
host 93.184.216.34
```

3. Résolution en spécifiant un serveur DNS particulier :  
```bash
host www.example.com 8.8.8.8
```

4. Obtenir les serveurs de messagerie (MX) :  
```bash
host -t MX example.com
```

5. Obtenir les serveurs de noms (NS) :  
```bash
host -t NS example.com
```

6. Vérifier un enregistrement spécifique (ex. TXT pour SPF ou DKIM) :  
```bash
host -t TXT example.com
```

---

## 3. La commande `dig`

### Présentation
`dig` (**Domain Information Groper**) est plus complet que `host`.  
Il permet de contrôler finement la requête DNS et d’obtenir davantage de détails sur la résolution.

### Syntaxe
```bash
dig [options] nom_domaine [type_enregistrement] [@serveur_dns]
```

### Exemples
1. Requête simple (par défaut, type **A**) :  
```bash
dig www.example.com
```

2. Spécifier le type d’enregistrement :  
- IPv4 :  
```bash
dig example.com A
```
- IPv6 :  
```bash
dig example.com AAAA
```

3. Réponse concise (adresse uniquement) :  
```bash
dig +short www.example.com
```

4. Obtenir un enregistrement MX (serveurs mail) :  
```bash
dig example.com MX
```

5. Obtenir un alias (CNAME) :  
```bash
dig www.example.com CNAME
```

6. Obtenir les serveurs de noms (NS) :  
```bash
dig example.com NS
```

7. Requête inverse (PTR) :  
```bash
dig -x 93.184.216.34
```

8. Interroger un serveur DNS spécifique (Google DNS 8.8.8.8) :  
```bash
dig @8.8.8.8 www.example.com
```

9. Suivre la résolution pas à pas (**trace**) :  
```bash
dig +trace www.example.com
```

10. Obtenir uniquement la section réponse :  
```bash
dig +noall +answer www.example.com
```

11. Vérifier plusieurs enregistrements en une commande :  
```bash
dig example.com A MX NS TXT
```

---

## 4. Cas pratiques

1. Vérifier la configuration DNS complète d’un domaine :  
```bash
dig +noall +answer example.com A
dig +noall +answer example.com AAAA
dig +noall +answer example.com MX
dig +noall +answer example.com NS
dig +noall +answer example.com TXT
```

2. Diagnostiquer un problème de résolution avec un serveur DNS donné :  
```bash
dig @1.1.1.1 www.example.com
```

3. Vérifier la propagation DNS d’un nouveau domaine (traverse les serveurs racine → TLD → DNS autoritaires) :  
```bash
dig +trace example.com
```

4. Vérifier l’enregistrement PTR d’une IP (utile pour la configuration des serveurs mail) :  
```bash
dig -x 203.0.113.5 +short
```

---

