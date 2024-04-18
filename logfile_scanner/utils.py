import logging
import os
from pathlib import Path
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


def update_state(state: Dict[str, Any], state_file: str, logfile: str, lines_read: int):
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


def get_config(args_config: str) -> Dict[str, Any]:
    if args_config is not None:
        logging.info(f"reading config from {args_config}")
        config = read_config(config_path=args_config)
    elif os.environ.get("CONFIG_FILE") is not None:
        logging.info(
            f'reading config from CONFIG_FILE environment variable at {os.environ.get("CONFIG_FILE")}'
        )
        config = read_config(config_path=os.environ.get("CONFIG_FILE"))
    else:
        config = dict()
        save_path = Path(__file__).parent / "settings.yml"
        with open(save_path, "w") as file:
            yaml.dump(config, file)
        logging.info(f"created default config and saved it to {save_path}")
    return _fix_config(config)


def _fix_config(config: Dict[str, Any]) -> Dict[str, Any]:
    if config.get("encoding") is None:
        logging.info("adding default encoding to settings file")
        config["encoding"] = "utf-8-sig"
    if config.get("state_file") is None:
        logging.info("adding default state_file to settings file")
        config["state_file"] = str(Path(__file__).parent / "state.yml")
    if config.get("db_path") is None:
        logging.info("adding default database path to settings file")
        config["db_path"] = str(Path(__file__).parent / "freq.db")
    return config
