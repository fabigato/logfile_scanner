import logging
from typing import Any, Dict

import yaml


def read_config(config_path: str) -> Dict[str, Any]:
    with open(config_path, "r") as file:
        return yaml.safe_load(file)


def read_state(state_path: str, log_file: str) -> Dict[str, Any]:
    try:
        state = read_config(state_path)
    except FileNotFoundError:
        logging.warning(f"state file {state_path} not found. Creating default state")
        state = {"last_logfile_read": log_file, "read_from_line": 0}
    return state


def update_state(
    state: Dict[str, Any], state_file: str, logfile: str, lines_read: int
) -> Dict[str, Any]:
    if state["last_logfile_read"] == "":
        state["last_logfile_read"] = logfile
    state["read_from_line"] += lines_read
    with open(state_file, "w") as file:
        yaml.dump(state, file)


def setup_logger(logfile: str):
    logging.basicConfig(
        filename=logfile,
        filemode="a",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.DEBUG,
    )
