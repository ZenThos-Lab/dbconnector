# Python imports
from abc import ABC, abstractmethod
from typing import Any, Dict

# Third-party imports

# Project-specific imports


class BaseConnector(ABC):
    TYPE: str

    def __init__(self, config: Dict[str, Any]) -> None:
        self.config = config

    @abstractmethod
    def connect(self):
        """Return a live PEP 249 connection (db-api)."""

    @classmethod
    @abstractmethod
    def required_fields(cls) -> Dict[str, type]:
        """Fields required for this connector type (for validation)."""
