[⬅️ Volver al README](../README.md)

# ❗ Solución de problemas

A continuación se listan algunos errores comunes y sus posibles
soluciones al usar **dbconnector**.

------------------------------------------------------------------------

## 1. `EnvironmentError: DB_CONNECTIONS_PATH not set`

No se encontró la variable de entorno. Define `DB_CONNECTIONS_PATH` o
carga `.env` con `load_dotenv()` antes de usar el paquete.

------------------------------------------------------------------------

## 2. `FileNotFoundError: Configuration file not found: ...`

La ruta en `DB_CONNECTIONS_PATH` no existe. Verifica que sea
**absoluta** y que el archivo esté presente.

------------------------------------------------------------------------

## 3. `KeyError: Configuration for alias:<alias> not found`

El alias que pasaste a `get_connection()` **no existe** en el YAML (o el
YAML cargado no es el correcto).\
Revisa la clave de nivel superior del YAML y la ruta que estás usando.

------------------------------------------------------------------------

## 4. Errores de `pyodbc` (por ejemplo: *driver no encontrado*, *login failed*)

-   Asegúrate de tener instalado el **ODBC Driver 18 for SQL Server** (o
    el que especifiques en `driver`).
-   Verifica credenciales, host/puerto y accesibilidad de red.
-   Si estás en contenedor/WSL, revisa networking y drivers ODBC del
    sistema huésped.
