# Python imports
from abc import ABC, abstractmethod

# Third-party imports

# Project-specific imports


class BaseConnector(ABC):
    def __init__(self, config: dict):
        self.config = config

    @abstractmethod
    def connect(self):
        """
        Establishes and return the database connection
        """
        pass
