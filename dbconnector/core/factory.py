# Python imports

# Third-party imports

# Project-specific imports
from ..config.loader import ConfigLoader
from .base import BaseConnector
from .mariadb_connector import MariaDBConnector
from .postgresql_connector import PostgreSQLConnector
from .sqlserver_connector import SQLServerConnector


CONNECTORS = {
    "postgresql": PostgreSQLConnector,
    "mariadb": MariaDBConnector,
    "sqlserver": SQLServerConnector,
}


class ConnectorFactory:
    """
    Factory class for managing database connections.

    This class provides a unified interface to create an manage connections to
    different types of databases based on a given configuration.
    """

    _connections = {}

    @classmethod
    def get_connection(cls, alias: str):
        """
        Retrieves a database connection for the given alias.

        If the connection already exists for the alias, it is reused.
        Otherwise, a new connection is established and cached.

        Args:
            alias (str): The key in the configuration file that indentifies
            a database connection.

        Returns:
            Any: An active database connection instance.

        Raises:
            KeyError: If the alias is not found in the configuration.
        """
        if alias in cls._connections:
            return cls._connections[alias]

        config = cls._get_db_config(alias)
        connector = cls._get_connector(config)
        connection = connector.connect()
        cls._connections[alias] = connection

        return connection

    @classmethod
    def _get_db_config(cls, alias: str) -> dict:
        """
        Loads the configuration dictionary for the given alias.

        Args:
            alias (str): The key in the configuration file that indentifies
            a database connection.

        Returns:
            dict: A dictionary with the database connection parameters.

        Raises:
            KeyError: If the alias is not found in the configuration file.
        """
        config = ConfigLoader().load()
        if alias not in config:
            raise KeyError(f"Configuration for alias:{alias} not found")

        return config[alias]

    @classmethod
    def _get_connector(cls, config: dict) -> BaseConnector:
        """
        Selects and initializes the appropriate connector based on the database
        type.

        Args:
            config (dict): A dictionary containing the database connection
            parameters.

        Returns:
            BaseConnector: An instance of the selected connector.

        Raises:
            KeyError: If the database type is not supported.
        """
        db_type = config["type"]

        if db_type not in CONNECTORS:
            raise KeyError(f"Connector for db_type:{db_type} not found")

        return CONNECTORS[db_type](config)

    @staticmethod
    def _is_connection_valid(connection) -> bool:
        """
        Verifies if a given database connection is valid.

        Args:
            connection (Any): A database connection instance.

        Returns:
            bool: True if the connection is valid, False otherwise
        """
        try:
            connection.cursor()
            return True
        except Exception:
            return False

    @classmethod
    def close(cls, alias: str):
        """
        Closes and removes the cached connection for the given alias.

        Args:
            alias (str): The key in the configuration file that indentifies
            a database connection.
        """
        if alias in cls._connections:
            try:
                cls._connections[alias].close()
            except Exception:
                pass
            finally:
                del cls._connections[alias]

    @classmethod
    def close_all(cls):
        """
        Closes and removes all cached connections managed by the factory.
        """
        for alias, connection in list(cls._connections.items()):
            try:
                connection.close()
            except Exception:
                pass
            finally:
                del cls._connections[alias]

        cls._connections = {}
