# Python imports
from typing import Any, Dict

# Third-party imports

# Project-specific imports
from ..config.loader import ConfigLoader
from ..connectors import get_connector_class
from ..connectors.base import BaseConnector


class ConnectorFactory:
    """
    Factory class for managing database connections.

    This class provides a unified interface to create an manage connections to
    different types of databases based on a given configuration.
    """

    _connections: Dict[str, Any] = {}

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
        db_type = config["type"]

        connector_cls = get_connector_class(db_type)
        connector: BaseConnector = connector_cls(config)

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
