import yaml
from typing import Dict, Any


def read_config(config_path: str) -> Dict[str, Any]:
    with open(config_path) as file:
        return yaml.safe_load(file)


def update_state(state: Dict[str, Any], state_file: str, logfile:str, lines_read: int) -> Dict[str, Any]:
    if state["last_logfile_read"] == "":
        state["last_logfile_read"] = logfile
    state["read_from_line"] += lines_read
    with open(state_file, "w") as file:
        yaml.dump(state, file)
