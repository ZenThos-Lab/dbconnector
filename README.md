# dbconnector

**dbconnector** is a lightweight Python package that simplifies connections to relational databases like **PostgreSQL**, **MariaDB**, and **SQL Server** using an alias-based configuration file.

## 🚀 Features

- Unified interface for multiple databases
- Minimal configuration via `db_connections.yaml`
- Built-in connection caching (singleton per alias)
- Easily extensible to support more engines
- Designed with clean architecture and SOLID principles

---

## 📦 Installation

```bash
pip install dbconnector
```

Or install from source:

```bash
git clone https://github.com/ZenThos-Lab/dbconnector.git
cd dbconnector
pip install .
```

---

## 🛠️ Configuration

Create a file called `db_connections.yaml` in your project root:

```yaml
my_postgres:
  type: postgresql
  host: 127.0.0.1
  port: 5432
  database: my_database
  user: postgres
  password: secret

my_mariadb:
  type: mariadb
  host: 127.0.0.1
  port: 3306
  database: my_database
  user: root
  password: secret

my_sqlserver:
  type: sqlserver
  driver: ODBC Driver 17 for SQL Server
  host: 127.0.0.1
  port: 1433
  database: my_database
  user: sa
  password: VerySecure123
```

---

## 🧪 Usage

```python
from dbconnector import ConnectorManager

# Get a connection
conn = ConnectorManager.get_connection("my_postgres")
# conn = ConnectorManager.get_connection("my_mariadb")
# conn = ConnectorManager.get_connection("my_sqlserver")

# Use the connection...
cursor = conn.cursor()
cursor.execute("SELECT * FROM example LIMIT 1;")
# cursor.execute("SELECT * FROM example LIMIT 1;")
# cursor.execute("SELECT TOP 1 * FROM example;")
rows = cursor.fetchall()

# Close a specific connection
ConnectorManager.close("my_postgres")
# ConnectorManager.close("my_mariadb")
# ConnectorManager.close("my_sqlserver")

# Or close all connections
ConnectorManager.close_all()
```

---

## 🧱 Supported Databases

- PostgreSQL (`psycopg2-binary`)
- MariaDB (`mariadb`)
- SQL Server (`pyodbc`)

> You can easily add more connectors by extending the `core/` folder and updating the factory.

---

## 📂 Project Structure

```
dbconnector/
├── dbconnector/
│   ├── config/           # YAML config loader
│   ├── core/             # Connectors + factory
│   └── manager.py        # Public interface
├── db_connections.yaml   # Example config file
├── pyproject.toml
└── README.md
```

---

## 📃 License

-
