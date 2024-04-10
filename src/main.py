from os import environ

from scanner.vlc import VLCScanner
from utils import read_config, update_state

config_file = environ.get("CONFIG_FILE", "settings.yml")
state_file = environ.get("STATE_FILE", "settings.yml")

if __name__ == "__main__":
    config = read_config(config_file)
    state = read_config(state_file)
    if (
        config["logfile"] != state["last_logfile_read"]
        or state["last_logfile_read"] == ""
    ):
        read_from = 0
    else:
        read_from = state["read_from_line"]

    scanner = VLCScanner(
        log_file=config["logfile"], read_from=read_from, encoding=config["encoding"]
    )
    lines_read = scanner.scan()

    update_state(state, state_file, config["logfile"], lines_read)
