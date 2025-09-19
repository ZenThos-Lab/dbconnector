# Python imports

# Third-party imports
import pyodbc

# Project-specific imports
from .base import BaseConnector


class SQLServerConnector(BaseConnector):
    TYPE = "sqlserver"

    @classmethod
    def required_fields(cls):
        return {
            "driver": str,
            "host": str,
            "port": int,
            "database": str,
            "user": str,
            "password": str,
            "trust_server_certificate": str,
        }

    def connect(self):
        trust_server_certificate = str(
            self.config.get('trust_server_certificate', 'Yes')
        )

        return pyodbc.connect(
            f"DRIVER={{{self.config['driver']}}};"
            f"SERVER={self.config['host']},{self.config['port']};"
            f"DATABASE={self.config['database']};"
            f"UID={self.config['user']};"
            f"PWD={self.config['password']};"
            f"TrustServerCertificate={trust_server_certificate};"
        )
