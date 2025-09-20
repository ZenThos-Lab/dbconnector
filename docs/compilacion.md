[⬅️ Volver al README](../README.md)

# 🛠️ Compilación con Cython

Este documento describe el proceso para compilar el paquete
`dbconnector` en una wheel binaria utilizando **Cython**.

------------------------------------------------------------------------

## 1. Crear o activar entorno virtual

Se recomienda trabajar dentro de un entorno virtual para aislar
dependencias:

``` bash
python3 -m venv env
source env/bin/activate
```

------------------------------------------------------------------------

## 2. Instalación de herramientas

Instala las dependencias de Python y del sistema:

``` bash
pip install -r requirements.txt
sudo apt install binutils
```

------------------------------------------------------------------------

## 3. Construcción de la wheel

Genera únicamente el paquete wheel con:

``` bash
python -m build --wheel
```

------------------------------------------------------------------------

## 4. Resultado de la compilación

La salida se genera en la carpeta `dist/`, por ejemplo:

    dist/dbconnector-0.1.0-cp311-cp311-linux_x86_64.whl

Esta wheel ya contendrá los módulos compilados como `.so` en lugar de
`.py`.

------------------------------------------------------------------------

## 5. Instalación en otro proyecto

Instala la wheel generada en tu entorno o en otro proyecto:

``` bash
pip install dist/dbconnector-0.1.0-cp311-cp311-linux_x86_64.whl
```

------------------------------------------------------------------------

## 6. Uso básico

Para ejemplos de uso consulta la guía: [Uso Básico](uso_basico.md).
