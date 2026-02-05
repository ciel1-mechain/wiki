# Qualificateurs de Type et Classes de Stockage en C

---

## **Définitions**

### **Qualificateurs de Type**
Les **qualificateurs de type** déterminent comment une variable peut être utilisée ou modifiée,
Exemples : `const`, `volatile`.

### **Classes de Stockage**
Les **classes de stockage** déterminent la **durée de vie** et la **portée** (visibilité) d'une variable.
Exemples : `static`, `extern`.

---

## **Tableau Récapitulatif**

| **Catégorie**         | **Mot-clé**  | **Description**                                                                                     | **Exemple**                                                                                     | **Utilisation actuelle**                                                                                     |
|-----------------------|--------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Qualificateurs**    | `const`      | Indique que la variable ne peut pas être modifiée après initialisation.                            | `const int MAX = 100;`                                                                          | Très courante.                                                                                                |
|                       | `volatile`   | Indique que la variable peut être modifiée de manière imprévisible (ex. : registre matériel).       | `volatile int *reg = (int *)0x8000;`                                                            | Courante en systèmes embarqués.                                                                               |
| **Classes de stockage**| `static`    | Pour une variable locale : conserve sa valeur entre les appels de fonction. Pour une variable globale : limite la portée au fichier. | `static int count = 0;` (locale) ou `static int global_var;` (globale)                          | Très courante.                                                                                                |
|                       | `extern`     | Déclare une variable définie dans un autre fichier (lien entre fichiers).                          | `extern int global_var;` (déclarée dans un autre fichier)                                       | Courante pour partager des variables entre fichiers.                                                          |

---

## **Remarques**
- **`const`** et **`volatile`** sont des **qualificateurs** : ils précisent comment la variable est utilisée.
- **`static`**, **`auto`**, **`register`**, et **`extern`** sont des **classes de stockage** : elles définissent la durée de vie et la portée.
- **`static`** a un comportement différent selon qu'il est appliqué à une variable locale ou globale.


---

## **Exemple Complet**
```c
#include <stdio.h>

const int TAILLE_MAX = 100; // Qualificateur de type
static int compteur = 0;    // Classe de stockage

void incrementer() {
    static int local = 0;   // Classe de stockage (locale persistante)
    local++;
    compteur++;
    printf("Local: %d, Global: %d\n", local, compteur);
}

int main() {
    incrementer(); // Local: 1, Global: 1
    incrementer(); // Local: 2, Global: 2
    return 0;
}
```