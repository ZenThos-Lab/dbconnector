REQUIRED_FIELDS = {
    "mariadb": {
        "host": str,
        "port": int,
        "database": str,
        "user": str,
        "password": str
    },
    "postgresql": {
        "host": str,
        "port": int,
        "database": str,
        "user": str,
        "password": str
    },
    "sqlserver": {
        "driver": str,
        "host": str,
        "port": int,
        "database": str,
        "user": str,
        "password": str,
        "trust_server_certificate": str,
    },
}
