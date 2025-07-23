# Python imports

# Third-party imports
import mariadb

# Project-specific imports
from .base import BaseConnector


class MariaDBConnector(BaseConnector):
    def connect(self):
        return mariadb.connect(
            host=self.config["host"],
            port=self.config["port"],
            database=self.config["database"],
            user=self.config["user"],
            password=self.config["password"],
        )
