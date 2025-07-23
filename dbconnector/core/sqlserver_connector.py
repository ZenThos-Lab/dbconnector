# Python imports

# Third-party imports
import pyodbc

# Project-specific imports
from .base import BaseConnector


class SQLServerConnector(BaseConnector):
    def connect(self):
        return pyodbc.connect(
            f"DRIVER={{{self.config['driver']}}};"
            f"SERVER={self.config['host']},{self.config['port']};"
            f"DATABASE={self.config['database']};"
            f"UID={self.config['user']};"
            f"PWD={self.config['password']};"
        )
