# Python imports

# Third-party imports
import psycopg2

# Project-specific imports
from .base import BaseConnector


class PostgreSQLConnector(BaseConnector):
    def connect(self):
        return psycopg2.connect(
            host=self.config["host"],
            port=self.config["port"],
            database=self.config["database"],
            user=self.config["user"],
            password=self.config["password"],
        )
