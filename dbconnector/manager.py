# Python imports

# Third-party imports

# Project-specific imports
from .core.factory import ConnectorFactory


class ConnectorManager:
    """
    Manage database connections using aliases defined in the configuration

    This class provides a simple static interface to get or close connections
    via the underlying ConnectorFactory. It supports multiple engines like
    PostgreSQL, MariaDB and SQL Server.
    """

    @staticmethod
    def get_connection(alias: str):
        """
        Return a live connection for the specified alias.

        If the connection does not exist, it is created using the configuration

        Args:
            alias (str): The alias defined in the configuration file.

        Returns:
            Any: An active database connection object.

        Raises:
            KeyError: If the alias is not found in the configuration
        """
        return ConnectorFactory.get_connection(alias)

    @staticmethod
    def close(alias: str):
        """
        Close the connection associated with the given alias.

        If no connection is found, nothin happens.

        Args:
            alias (str): The alias of the connection to close.
        """
        return ConnectorFactory.close(alias)

    @staticmethod
    def close_all():
        """
        Close all active connections managed by the factory.
        """
        return ConnectorFactory.close_all()
