# dbconnector

**dbconnector** es un paquete ligero de Python para **estandarizar** y
**simplificar** las conexiones a bases de datos relacionales mediante un
archivo de configuración por alias.\
Está diseñado para extenderse fácilmente a diferentes motores de bases
de datos.

> **Idea clave**: el proyecto que consume `dbconnector` no guarda
> credenciales en código. En su lugar define un archivo
> `db_connections.yaml` y expone su ruta con la variable de entorno
> `DB_CONNECTIONS_PATH` (o vía `.env` con `python-dotenv`).

------------------------------------------------------------------------

## 📦 Instalación

``` bash
pip install --no-cache-dir "git+https://github.com/ZenThos-Lab/dbconnector.git@main"
```

> Requisitos: Python **3.9+** y el **driver ODBC** de SQL Server
> instalado en tu sistema (por ejemplo, *ODBC Driver 18 for SQL
> Server*).

------------------------------------------------------------------------

## 🚀 Uso básico

Consulta la guía completa en el siguiente [enlace](docs/uso_basico.md).

------------------------------------------------------------------------

## 🛠️ Compilación

Si deseas compilar el paquete con **Cython** para generar wheels
binarias, sigue los pasos en el siguiente [enlace](docs/compilacion.md).

------------------------------------------------------------------------

## ❗ Solución de problemas

Consulta la guía completa en el siguiente [enlace](docs/solucion_problemas.md).

------------------------------------------------------------------------
