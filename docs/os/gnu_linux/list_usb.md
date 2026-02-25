# Gestion des Ports USB et Série sous Linux

Ce document explique comment lister, identifier et utiliser les périphériques USB (Arduino, micro:bit, cartes relais USB, etc.) sous Linux.

---
## 1. Types de périphériques `/dev/tty*`

| Nom         | Exemple        | Description |
|-------------|----------------|-------------|
| **ttyS***   | `/dev/ttyS0`   | Ports série matériels (RS-232 intégrés à la carte mère). |
| **ttyUSB*** | `/dev/ttyUSB0` | Ports créés par un convertisseur **USB ↔ UART** (puces FTDI, Prolific, CH340, etc.). |
| **ttyACM*** | `/dev/ttyACM0` | Périphériques **USB CDC ACM** (Arduino officiel, micro:bit, STM32, etc.). |

---

## 2. Lister les périphériques USB

### Commandes de base

```bash
lsusb
```

- Affiche tous les périphériques USB connectés avec **Vendor ID** et **Product ID**.
- Exemple de sortie :

```bash
Bus 001 Device 005: ID 2341:0043 Arduino SA Uno R3
Bus 001 Device 006: ID 0d28:0204 ARM mbed Micro:bit
Bus 001 Device 007: ID 16c0:05df USB-Relay-8
```

```bash
dmesg -w
```

- Affiche les logs du noyau en temps réel.
- Très utile pour voir quel `/dev/tty*` est créé lors du branchement.

```bash
[ 1234.5678 ] usb 1-1.2: ch341-uart converter now attached to ttyUSB0
[ 1234.5680 ] cdc_acm 1-1.3:1.0: ttyACM0: USB ACM device
```

```bash
ls /dev/ttyUSB* /dev/ttyACM*
```

- Liste les périphériques séries accessibles.

---



## 3. Identifier quel port correspond à ton matériel

### Méthode pratique

1. Débranche ton périphérique.
2. Tape :  

```bash
ls /dev/ttyUSB* /dev/ttyACM*
```

3. Branche ton périphérique.
4. Re-tape la même commande : le nouveau device est ton port série.

### Vérification détaillée

```bash
udevadm info -q all -n /dev/ttyUSB0
```

- Affiche les infos **Vendor ID**, **Product ID** et **numéro de série**.

---

## 4. Exemples pratiques

### 🟦 Arduino Uno

- **Officiel** : `/dev/ttyACM0` (CDC ACM)
- **Clone CH340/FTDI** : `/dev/ttyUSB0` (USB↔UART)

### 🟩 micro:bit

- `/dev/ttyACM0` (CDC ACM)


---

## 5. Règles `udev` pour noms stables

- Permet de donner un **nom fixe** à ton Arduino/micro:bit.
- Exemple pour Arduino Uno officiel :

1. Trouver Vendor ID et Product ID :

```bash
lsusb
```

Sortie :

```
ID 2341:0043 Arduino SA Uno R3
```

2. Créer la règle `udev` :

```bash
sudo nano /etc/udev/rules.d/99-arduino.rules
```

Contenu :

```
SUBSYSTEM=="tty", ATTRS{idVendor}=="2341", ATTRS{idProduct}=="0043", SYMLINK+="arduino_uno"
```

!!! information
    Pourquoi 99 comme numéro en préfixe ?

    - udev lit les fichiers de règles dans l’ordre alphabétique.

    - Les fichiers numérotés sont donc lus dans l’ordre croissant.

    - En mettant 99-, tu t’assures que cette règle est lue après toutes les autres règles système (comme celles de 10- ou 50- pour les périphériques génériques).

    - C’est pratique pour écraser ou compléter les règles existantes pour un périphérique spécifique (ici Arduino).

3. Recharger les règles :

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

- Ton Arduino est maintenant accessible via `/dev/arduino_uno`.

---


