# Python imports
from typing import Dict, Type

# Third-party imports

# Project-specific imports
from .base import BaseConnector
from .sqlserver import SQLServerConnector


REGISTRY: Dict[str, Type[BaseConnector]] = {
    SQLServerConnector.TYPE: SQLServerConnector
}


def get_connector_class(db_type: str) -> Type[BaseConnector]:
    try:
        return REGISTRY[db_type]
    except KeyError:
        raise KeyError(f"Connector for db_type:{db_type} not found")
