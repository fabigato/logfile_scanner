import yaml
from typing import Dict, Any


def read_config(config_path: str) -> Dict[str, Any]:
    with open(config_path) as file:
        return yaml.safe_load(file)
