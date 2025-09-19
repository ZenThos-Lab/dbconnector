# Python imports
import os

from pathlib import Path
from typing import Any, Dict, Optional

# Third-party imports
import yaml

# Project-specific imports
from ..connectors import get_connector_class


class ConfigLoader:
    def __init__(self):
        db_connections_path = os.getenv("DB_CONNECTIONS_PATH")
        if not db_connections_path:
            raise EnvironmentError(
                "Environment variable DB_CONNECTIONS_PATH not set. "
                "Please create a environment variable named "
                "DB_CONNECTIONS_PATH and set it to the path to your "
                "db_connections.yaml file."
            )

        self._path = Path(db_connections_path)
        self._config: Optional[Dict[str, Dict[str, Any]]] = None

    def load(self) -> Dict[str, Dict[str, Any]]:
        if self._config is None:
            if not self._path.exists():
                raise FileNotFoundError(
                    f"Configuration file not found: {self._path}"
                )

            with self._path.open("r", encoding="utf-8") as file:
                data = yaml.safe_load(file)

            if data is None:
                raise ValueError(
                    f"Configuration file {self._path} is empty."
                )
            if not isinstance(data, dict):
                raise ValueError(
                    "Root of YAML must be a mapping of aliases -> "
                    "params dicts."
                )

            self._config = data
            self._validate()

        return self._config

    def _validate(self) -> None:
        for alias, params in self._config.items():
            if not isinstance(params, dict):
                raise ValueError(
                    f"Alias '{alias}' must map to a dict of parameters."
                )

            if "type" not in params:
                raise KeyError(
                    f"Missing required field 'type' for alias:{alias}"
                )

            db_type = params.get("type")
            connector_cls = get_connector_class(db_type)
            required = connector_cls.required_fields()
            missing_fields = [
                key for key in required.keys() if key not in params
            ]
            if missing_fields:
                raise KeyError(
                    f"Missing required fields for alias:{alias} "
                    f"db_type:{db_type}: "
                    f"{sorted(missing_fields)}"
                )
