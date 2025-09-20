[⬅️ Volver al README](../README.md)

# 🚀 Uso básico de dbconnector

Este documento muestra ejemplos mínimos de cómo utilizar el paquete
**dbconnector** una vez instalado y configurado en tu proyecto.

------------------------------------------------------------------------

## 1. Definir variable de entorno

`dbconnector` requiere que definas la variable de entorno
**`DB_CONNECTIONS_PATH`**, la cual apunta al archivo de configuración
YAML con tus conexiones.

La forma más simple es crear un archivo `.env` en la raíz de tu proyecto
con el contenido:

``` dotenv
DB_CONNECTIONS_PATH=/ruta/absoluta/a/tu/db_connections.yaml
```

Carga este `.env` al inicio de tu aplicación:

``` python
from dotenv import load_dotenv

load_dotenv()
```

------------------------------------------------------------------------

## 2. Estructura de `db_connections.yaml`

Ejemplo para **SQL Server**:

``` yaml
mi_sqlserver:
  type: sqlserver
  driver: ODBC Driver 18 for SQL Server
  host: 127.0.0.1
  port: 1433
  database: mi_base
  user: sa
  password: mi_password
  trust_server_certificate: 'Yes'
```

-   La clave de nivel superior (`mi_sqlserver`) es el **alias** que
    usarás al pedir la conexión.
-   `type` define el motor de base de datos (actualmente soportado:
    **sqlserver**).
-   Puedes definir múltiples alias en el mismo archivo (ejemplo: `etl`,
    `reporting`, `analytics`).

------------------------------------------------------------------------

## 3. Obtener una conexión por alias

``` python
from dbconnector import ConnectorManager

# Obtén la conexión usando el alias definido en tu db_connections.yaml
conn = ConnectorManager.get_connection("mi_sqlserver")

# Trabaja con la conexión (DB-API 2.0 / PEP 249)
cur = conn.cursor()
cur.execute("SELECT TOP 1 name FROM sys.databases;")
row = cur.fetchone()
print(row)
```

------------------------------------------------------------------------

## 4. Cerrar conexiones

``` python
# Cierra la conexión específica
ConnectorManager.close("mi_sqlserver")

# O cierra todas las conexiones activas
ConnectorManager.close_all()
```

------------------------------------------------------------------------

## 5. Ejemplo rápido con script

``` python
# test_db.py
from dotenv import load_dotenv
from dbconnector import ConnectorManager

load_dotenv()

conn = ConnectorManager.get_connection("mi_sqlserver")
cur = conn.cursor()
cur.execute("SELECT 1 AS ok;")
print(cur.fetchone())
ConnectorManager.close_all()
```

Ejecuta el script:

``` bash
python test_db.py
```

------------------------------------------------------------------------
