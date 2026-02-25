# Zephyr sur microbit v2

## Répertoires

Réperoire du projet : `~/zephyrproject/monprojet`
Programme dans `src/main.c`
Répertoire courant : `~/zephyrproject/monprojet`

## Structure du répertoire 
```
.
├── boards
├── build
├── CMakeLists.txt
├── prj.conf
├── sample.yaml
└── src
```

## Compilation et téléversement

```bash
west build -b bbc_microbit_v2 . --pristine
cp build/zephyr/zephyr.hex <chemin vers la carte micribit>
```
## Programme "Hello World!"

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/printk.h>

int main(void)
{
    while (1) {
        printk("Hello World! (depuis Zephyr sur micro:bit v2)\n");
        k_msleep(2000); // Pause de 2 secondes
    }
    return 0;
}
```



