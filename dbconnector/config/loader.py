# Python imports
import os

# Third-party imports
import yaml

# Project-specific imports


_CONFIG_CACHE = None


def load_config(path="db_connections.yaml"):
    global _CONFIG_CACHE
    if _CONFIG_CACHE is None:
        if not os.path.exists(path):
            raise FileNotFoundError(
                f"No se encuentra el archivo de configuración: {path}"
            )

        with open(path, "r") as file:
            _CONFIG_CACHE = yaml.safe_load(file)

    return _CONFIG_CACHE
