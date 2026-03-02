# Authentification GitHub : HTTPS et SSH

## Table des matières
1. [Pourquoi une authentification ?](#1-pourquoi-une-authentification)
2. [HTTPS avec Personal Access Token](#2-https-avec-personal-access-token)
3. [SSH : la méthode recommandée](#3-ssh--la-methode-recommandee)
4. [HTTPS ou SSH : que choisir ?](#4-https-ou-ssh--que-choisir)

---

## 1. Pourquoi une authentification ?

Depuis **août 2021**, GitHub n'accepte plus les mots de passe pour les opérations Git en ligne de commande (`push`, `pull`, `clone`).

Il faut obligatoirement utiliser l'une de ces deux méthodes :

| Méthode | Principe |
|---------|----------|
| **HTTPS + Token** | On remplace le mot de passe par un token généré sur GitHub |
| **SSH** | On génère une paire de clés cryptographiques, GitHub reconnaît votre machine |

---

## 2. HTTPS avec Personal Access Token

### 2.1 Créer un token sur GitHub {#2-https-avec-personal-access-token}

1. Aller sur **GitHub → Settings** (icône de profil en haut à droite)
2. Descendre jusqu'à **Developer settings** (tout en bas du menu)
3. Cliquer sur **Personal access tokens → Tokens (classic)**
4. Cliquer **"Generate new token (classic)"**
5. Remplir :

    - **Note** : un nom pour identifier le token (ex: `laptop-iut`)
    - **Expiration** : choisir une durée (90 jours recommandé)
    - **Scopes** : cocher au minimum **`repo`** (accès complet aux dépôts)
6. Cliquer **"Generate token"**

> ⚠️ **Copiez le token immédiatement** : il ne sera plus affiché après avoir quitté la page.

### 2.2 Utiliser le token

**Option 1 — Le saisir manuellement à chaque fois**
```bash
git push
# Username: votre-pseudo-github
# Password: collez-votre-token  ← pas votre vrai mot de passe
```

**Option 2 — L'intégrer dans l'URL du dépôt**
```bash
git remote set-url origin https://VOTRE_TOKEN@github.com/pseudo/repo.git
```

> ⚠️ Cette option inscrit le token en clair dans la config Git. Déconseillé sur un ordinateur partagé.

**Option 3 — Le mémoriser avec le credential store (recommandé)**
```bash
# Activer la mémorisation des identifiants
git config --global credential.helper store

# Faire un premier push → Git vous demande le token une seule fois
git push
# Username: votre-pseudo
# Password: votre-token

# Les prochains push/pull seront automatiques
```

> 💡 Les identifiants sont stockés en clair dans `~/.git-credentials`. Sur Windows, préférer `credential.helper manager` qui utilise le trousseau Windows de façon sécurisée.

### 2.3 Vérifier ou changer l'URL d'un dépôt

```bash
# Voir l'URL actuelle
git remote -v

# Changer l'URL (si vous avez cloné en SSH et voulez passer en HTTPS)
git remote set-url origin https://github.com/pseudo/repo.git
```

---

## 3. SSH : la méthode recommandée

SSH utilise une **paire de clés cryptographiques** :  

- une **clé privée** → reste sur votre machine, ne se partage jamais
- une **clé publique** → déposée sur GitHub

Quand vous faites un `push`, GitHub vérifie que votre clé privée correspond à la clé publique enregistrée. Pas besoin de token ni de mot de passe.

### 3.1 Générer une paire de clés SSH

```bash
ssh-keygen -t ed25519 -C "votre@email.com"
```

Git vous pose quelques questions :
```
Enter file in which to save the key: ← Appuyer sur Entrée (emplacement par défaut)
Enter passphrase: ← Optionnel mais recommandé (mot de passe local pour protéger la clé)
```

Les clés sont créées dans `~/.ssh/` :
- `id_ed25519` → clé privée (ne jamais partager !)
- `id_ed25519.pub` → clé publique (à déposer sur GitHub)

### 3.2 Ajouter la clé publique sur GitHub

**Afficher la clé publique :**
```bash
cat ~/.ssh/id_ed25519.pub
# Copier tout le contenu affiché
```

**Sur GitHub :**
1. Aller sur **Settings → SSH and GPG keys**
2. Cliquer **"New SSH key"**
3. Donner un titre (ex: `laptop-iut`)
4. Coller la clé publique dans le champ **"Key"**
5. Cliquer **"Add SSH key"**

### 3.3 Tester la connexion SSH

```bash
ssh -T git@github.com
# Réponse attendue :
# Hi votre-pseudo! You've successfully authenticated...
```

### 3.4 Cloner et utiliser un dépôt en SSH

Lors du clone, utiliser l'URL SSH (et non HTTPS) :
```bash
# URL SSH (format git@)
git clone git@github.com:pseudo/repo.git

# Et non l'URL HTTPS
# git clone https://github.com/pseudo/repo.git
```

> 💡 Sur GitHub, le bouton **"Code"** propose les deux formats : basculer sur **"SSH"** pour copier la bonne URL.

### 3.5 Passer un dépôt existant de HTTPS à SSH

```bash
# Vérifier l'URL actuelle
git remote -v
# origin  https://github.com/pseudo/repo.git (fetch)

# Changer pour SSH
git remote set-url origin git@github.com:pseudo/repo.git

# Vérifier
git remote -v
# origin  git@github.com:pseudo/repo.git (fetch)
```

### 3.6 Ajouter la clé au ssh-agent (optionnel)

Si vous avez défini une passphrase, vous pouvez la saisir une seule fois par session grâce au ssh-agent :

```bash
# Démarrer le ssh-agent
eval "$(ssh-agent -s)"

# Ajouter la clé privée
ssh-add ~/.ssh/id_ed25519
# → Saisir la passphrase une seule fois
```

---

## 4. HTTPS ou SSH : que choisir ? {#4-https-ou-ssh--que-choisir}

| Critère | HTTPS + Token | SSH |
|---------|--------------|-----|
| Mise en place | Rapide | Un peu plus longue |
| Utilisation quotidienne | Token à gérer (expiration) | Transparente après configuration |
| Sécurité | Bien si credential store | Très bonne |
| Réseau restreint (proxy, firewall) | ✅ Fonctionne toujours (port 443) | ⚠️ Port 22 parfois bloqué |
| Plusieurs machines | Token à recréer par machine | Clé à générer par machine |
| **Recommandation** | Démarrage rapide, usage ponctuel | **Usage régulier et projets perso** |

> 💡 **Conseil pour débutants** : commencez par HTTPS + credential store pour démarrer vite. Passez à SSH dès que vous utilisez Git régulièrement.
