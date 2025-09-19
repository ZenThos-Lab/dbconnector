# dbconnector

**dbconnector** es un paquete ligero de Python para **estandarizar** y **simplificar** las conexiones a bases de datos relacionales mediante un archivo de configuración por alias.
En su versión actual soporta **SQL Server** (vía `pyodbc`) y está diseñado para extenderse fácilmente a otros motores.

> **Idea clave**: el proyecto que consume `dbconnector` no guarda credenciales en código. En su lugar define un archivo `db_connections.yaml` y expone su ruta con la variable de entorno `DB_CONNECTIONS_PATH` (o vía `.env` con `python-dotenv`).

---

## 📦 Instalación

```bash
pip install "dbconnector @ git+https://github.com/ZenThosLab/dbconnector.git@main"
```

> Requisitos: Python **3.9+** y el **driver ODBC** de SQL Server instalado en tu sistema (por ejemplo, *ODBC Driver 18 for SQL Server*).

---

## ⚙️ Configuración

`dbconnector` lee la configuración desde un **YAML** cuya ruta se obtiene por la variable de entorno **`DB_CONNECTIONS_PATH`**.

### 1) Define la variable de entorno

#### a) Con `.env` (recomendado)
Crea un archivo `.env` en la raíz de tu proyecto **consumidor** (no en el paquete) con la ruta **absoluta** a tu YAML:

```dotenv
DB_CONNECTIONS_PATH=/ruta/absoluta/a/tu/db_connections.yaml
```

Carga el `.env` al inicio de tu aplicación:

```python
from dotenv import load_dotenv
load_dotenv()  # busca .env en el cwd y carpetas superiores
```

#### b) Export directo del entorno (Linux/macOS)
```bash
export DB_CONNECTIONS_PATH=/ruta/absoluta/a/tu/db_connections.yaml
```

#### c) Con el CLI de python-dotenv (sin modificar código)
```bash
python -m dotenv run -- python main.py
```

### 2) Crea `db_connections.yaml`

Ejemplo para **SQL Server**:

```yaml
mi_sqlserver:
  type: sqlserver
  driver: ODBC Driver 18 for SQL Server
  host: 127.0.0.1
  port: 1433
  database: mi_base
  user: sa
  password: MiPasswordSuperSegura1!
  trust_server_certificate: 'Yes'
```

- La clave de nivel superior (`mi_sqlserver`) es el **alias** que usarás al pedir la conexión.
- `type` define el motor (actualmente **sqlserver**).
- `trust_server_certificate` puede ser `'Yes'` o `'No'` según tu entorno.

> ✅ Puedes tener **múltiples alias** en el mismo YAML (por ejemplo `reporting`, `etl`, `analytics`, etc.).

---

## 🚀 Uso básico

```python
from dotenv import load_dotenv
from dbconnector import ConnectorManager

# 1) Carga variables de entorno (si usas .env)
load_dotenv()

# 2) Obtén una conexión por alias
conn = ConnectorManager.get_connection("mi_sqlserver")

# 3) Usa la conexión (DB-API 2.0 / PEP 249)
cur = conn.cursor()
cur.execute("SELECT TOP 1 name FROM sys.databases;")
row = cur.fetchone()
print(row)

# 4) Cierra la conexión (opcional; también puedes cerrar todas)
ConnectorManager.close("mi_sqlserver")
# ConnectorManager.close_all()
```

---

## 🧠 API pública

- `ConnectorManager.get_connection(alias: str) -> Connection`
  Devuelve (y cachea) una conexión activa para el alias indicado.

- `ConnectorManager.close(alias: str) -> None`
  Cierra y elimina del caché la conexión del alias.

- `ConnectorManager.close_all() -> None`
  Cierra y limpia **todas** las conexiones administradas.

> El caché por alias evita reconexiones innecesarias durante la vida del proceso.

---

## 🧪 Prueba rápida (script)

```python
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

```bash
python test_db.py
```

---

## ❗ Solución de problemas

- **`EnvironmentError: DB_CONNECTIONS_PATH not set`**
  No se encontró la variable de entorno. Define `DB_CONNECTIONS_PATH` o carga `.env` con `load_dotenv()` antes de usar el paquete.

- **`FileNotFoundError: Configuration file not found: ...`**
  La ruta en `DB_CONNECTIONS_PATH` no existe. Verifica que sea **absoluta** y que el archivo esté presente.

- **`KeyError: Configuration for alias:<alias> not found`**
  El alias que pasaste a `get_connection()` **no existe** en el YAML (o el YAML cargado no es el correcto). Revisa la clave de nivel superior del YAML y la ruta que estás usando.

- **Errores de `pyodbc` (por ejemplo: driver no encontrado, login failed)**
  - Asegúrate de tener instalado el **ODBC Driver 18 for SQL Server** (o el que especifiques en `driver`).
  - Verifica credenciales, host/puerto y accesibilidad de red.
  - Si estás en contenedor/WSL, revisa networking y drivers ODBC del sistema huésped.

---

## 📚 Estructura del proyecto (paquete)

```
dbconnector/
├── dbconnector/
│   ├── config/
│   │   └── loader.py          # Carga & validación de YAML (vía DB_CONNECTIONS_PATH)
│   ├── connectors/
│   │   ├── base.py            # Interfaz abstracta de conectores
│   │   └── sqlserver.py       # Conector para SQL Server (pyodbc)
│   ├── core/
│   │   └── factory.py         # Orquestación y caché de conexiones
│   ├── __init__.py            # API pública (ConnectorManager)
│   └── manager.py             # Fachada de uso
├── db_connections_example.yaml
├── pyproject.toml
└── README.md
```

---

## ✅ Soporte actual y extensibilidad

- **Actual**: SQL Server (`pyodbc`).
- **Diseño**: arquitectura por conectores (`connectors/`) y fábrica genérica, pensada para agregar motores en el futuro (PostgreSQL, MySQL, etc.) sin cambiar la API pública.

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia **MIT**. Consulta el archivo `LICENSE` (o ajusta la licencia según tus necesidades).
