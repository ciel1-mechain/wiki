# Programmation de la micro:bit v2 avec MicroPython

---
## Faire une pause

Pour suspendre l'exécution du programme, utilisez la fonction `sleep_ms` ou `sleep` du module `utime`.

**Syntaxe** :
```python
import utime
utime.sleep(durée_en_seconds)  # durée en secondes
# ou
utime.sleep_ms(durée_en_millisecondes)  # durée en millisecondes
```

**Exemple** :
Allumer une LED pendant 1 seconde, puis l'éteindre pendant 500 millisecondes.
```python
from microbit import *
import utime

while True:
    print("Test")              # Envoi d'une chaîne de caractères sur la liaison USB
    utime.sleep(1.5)           # Pause de 1,5 seconde
    display.clear()            # Éteint la matrice
    utime.sleep_ms(500)        # Pause de 500 ms
```

---
## Utilisation de la matrice à LEDs

La micro:bit dispose d'une matrice de **25 LEDs (5x5)** adressables individuellement.

### Fonctions principales

| Fonction | Description |
|----------|-------------|
| `display.set_pixel(x, y, n)` | Allume la LED en position `(x, y)` avec une intensité `n` (0=éteint, 9=max). |
| `display.clear()` | Éteint toutes les LEDs. |
| `display.show(icon)` | Affiche un icône prédéfini (ex: `Image.HEART`). |

**Exemple** : Allumer une LED en (2, 2) avec une intensité maximale.
```python
from microbit import *
import utime

while True:
    display.set_pixel(2, 2, 9)  # Allume la LED centrale
    utime.sleep(1)              # Pause de 1 seconde
    display.clear()             # Éteint tout
    utime.sleep(1)              # Pause de 1 seconde
```

**Remarque** :  

- `x` : Numéro de **colonne** (0 à 4) ou **position dans la ligne**.
- `y` : Numéro de **ligne** (0 à 4) ou **position dans la colonne**.

#### Schéma des 25 LEDs de la micro:bit (coordonnées x, y)
            0     1     2     3     4
          +-----+-----+-----+-----+-----+
        0 | 0,0 | 1,0 | 2,0 | 3,0 | 4,0 |
          +-----+-----+-----+-----+-----+
        1 | 0,1 | 1,1 | 2,1 | 3,1 | 4,1 |
          +-----+-----+-----+-----+-----+
        2 | 0,2 | 1,2 | 2,2 | 3,2 | 4,2 |
          +-----+-----+-----+-----+-----+
        3 | 0,3 | 1,3 | 2,3 | 3,3 | 4,3 |
          +-----+-----+-----+-----+-----+
        4 | 0,4 | 1,4 | 2,4 | 3,4 | 4,4 |
          +-----+-----+-----+-----+-----+

---
## Utilisation des boutons poussoirs A et B

### Méthodes disponibles

| Méthode | Description |
|---------|-------------|
| `button_a.is_pressed()` | Retourne `True` si le bouton A est **enfoncé**. |
| `button_a.was_pressed()` | Retourne `True` si le bouton A a été **pressé une fois** (efface la mémorisation après appel). |
| `button_b.is_pressed()` | Idem pour le bouton B. |
| `button_b.was_pressed()` | Idem pour le bouton B. |

**Exemple** : Allumer une LED quand le bouton A est pressé.
```python
from microbit import *
import utime

while True:
    if button_a.is_pressed():
        display.set_pixel(2, 2, 9)  # Allume la LED centrale
    else:
        display.clear()            # Éteint tout
    utime.sleep_ms(100)            # Pause
```

**Exemple avec `was_pressed()`** :
```python
from microbit import *
import utime

while True:
    if button_a.was_pressed():
        display.set_pixel(2, 2, 9)  # Allume la LED centrale
        utime.sleep(1)
        display.clear()
```


---
## Utilisation du CAN (Convertisseur Analogique-Numérique)

La micro:bit v2 dispose de **3 entrées analogiques** (P0, P1, P2) pour lire des tensions entre **0 V et 3.3 V**.

### Fonction principale

| Fonction | Description |
|----------|-------------|
| `pin.read_analog()` | Lit la tension sur une broche et retourne une valeur entre **0 et 1023**, où **1023 correspond à une tension proche de 3.3 V** (résolution ≈ 3.22 mV par incrément). |

**Exemple** : Lire la tension sur la broche **P0** et afficher une barre de LEDs proportionnelle.
```python
from microbit import *
import utime

while True:
    valeur = pin0.read_analog()  # Lit la tension sur P0 (0-1023)
    print("U =  {:.2f}".format(valeur*3.3/1024)) # Affiche la valeur de la
                                                 # tension avec 2 chiffres après la virgule
    utime.sleep_ms(500)
```

---
## Entrées/Sorties logiques

Les broches **P0 à P20** peuvent être configurées en **entrée ou sortie logique** (0 V = `False`, 3.3 V = `True`).

### Fonctions principales

| Fonction | Description |
|----------|-------------|
| `pin.write_digital(value)` | Écrit une valeur logique (`0` ou `1`) sur une broche. |
| `pin.read_digital()` | Lit une valeur logique (`0` ou `1`) sur une broche. |

**Exemple** : Applique une tension sur **P0**.
```python
from microbit import *
import utime

while True:
    pin0.write_digital(1)  # 3.3 V sur P0
    utime.sleep(1)
    pin0.write_digital(0)  # 0 V sur P0
    utime.sleep(1)
```

**Exemple avec entrée logique** : Lire un bouton poussoir externe sur **P1**.
```python
from microbit import *
import utime

while True:
    if pin1.read_digital():  # Si le bouton est enfoncé (3.3 V)
        print("ON")
    utime.sleep(0.2)
```

---
## MLI (Modulation de Largeur d'Impulsion)

La MLI permet de **simuler une tension analogique** en faisant varier le rapport cyclique d'un signal carré.

### Fonction principale

| Fonction | Description |
|----------|-------------|
| `pin.write_analog(value)` | Génère un signal MLI avec un rapport cyclique de `value/1023`. `value` peut varier de 0 à 1023. |

**Exemple** : Faire varier la luminosité d'une LED externe sur **P0** avec un potentiomètre sur **P1**.
```python
from microbit import *
import utime

while True:
    valeur_pot = pin1.read_analog()  # Lit le potentiomètre (0-1023)
    pin0.write_analog(valeur_pot)    # Applique la MLI sur P0
    utime.sleep_ms(10)
```
---
## Communiquer sans fil
### Envoyer un message via la liaison radio

```python
from microbit import *
import utime
import radio

radio.on()
radio.config(channel=9)

val = 100

while True:
  
  radio.send("{}".format(val))
  utime.sleep(1)
```

### Recevoir un message via la liaison radio

```python
from microbit import *
import utime
import radio

radio.on()
radio.config(channel=9)

while True:
  message = radio.receive()
  if message is not None:
    print(message)
  utime.sleep(0.2)
```

---
## Commande d'un servomoteur

Les servomoteurs sont contrôlés par un **signal MLI spécifique** avec une période de **20 ms** et une largeur d'impulsion comprise entre **1 ms (0°)** et **2 ms (180°)**.

### Fonctions principales

| Fonction | Description |
|----------|-------------|
| `pin.set_analog_period_microseconds(20000)` | Définit la période du signal MLI à 20 ms (50 Hz). |
| `pin.write_analog(value)` | Envoie une impulsion de durée `value` (en µs). `value` doit être compris entre 1000 et 2000 pour couvrir la plage 0°-180°. |

**Exemple** : Contrôler un servomoteur sur **P0** pour balayer de 0° à 180°.
```python
from microbit import *
import utime

# Configuration de la période MLI à 20 ms (50 Hz)
pin0.set_analog_period_microseconds(20000)

while True:
    # Balaye de 0° (1000 µs) à 180° (2000 µs)
    for angle in range(0, 181, 10):
        # Convertit l'angle en durée d'impulsion (1000 µs à 2000 µs)
        impulsion = 1000 + (angle * 1000 // 180)
        pin0.write_analog(impulsion)
        utime.sleep_ms(500)
```

---
## Bilan des instructions

| Catégorie               | Fonction / Méthode                          | Description                                                                 |
|-------------------------|---------------------------------------------|-----------------------------------------------------------------------------|
| **Temporisation**       | `utime.sleep(seconds)`                      | Suspend l'exécution pendant `seconds` secondes.                            |
|                         | `utime.sleep_ms(milliseconds)`              | Suspend l'exécution pendant `milliseconds` millisecondes.                 |
| **Matrice LED**         | `display.set_pixel(x, y, n)`               | Allume la LED en `(x, y)` avec une intensité `n` (0-9).                    |
|                         | `display.clear()`                           | Éteint toutes les LEDs.                                                    |
|                         | `display.show(icon)`                        | Affiche un icône prédéfini.                                                |
| **Boutons**             | `button_a.is_pressed()`                     | Retourne `True` si le bouton A est enfoncé.                                |
|                         | `button_a.was_pressed()`                    | Retourne `True` si le bouton A a été pressé (mémorisation).               |
| **CAN**                 | `pin.read_analog()`                         | Lit une tension analogique (0-1023). **1023 ≈ 3.3 V**. Résolution ≈ 3.22 mV. |
| **E/S logiques**        | `pin.write_digital(value)`                  | Écrit une valeur logique (`0` ou `1`) sur une broche.                      |
|                         | `pin.read_digital()`                        | Lit une valeur logique (`0` ou `1`) sur une broche.                        |
| **MLI**                 | `pin.write_analog(value)`                   | Génère un signal MLI avec un rapport cyclique `value/1023`.                 |
|                         | `pin.set_analog_period_microseconds(µs)`    | Définit la période du signal MLI en microsecondes.                         |
| **Servomoteur**         | `pin.set_analog_period_microseconds(20000)` | Configure une période de 20 ms pour un servomoteur.                        |
|                         | `pin.write_analog(µs)`                       | Envoie une impulsion de durée `µs` (1000-2000 µs pour 0°-180°).             |

---

