from utils import read_config, update_state
from os import environ


config_file = environ.get("CONFIG_FILE", "settings.yml")
state_file = environ.get("STATE_FILE", "settings.yml")

if __name__ == "__main__":
    config = read_config(config_file)
    state = read_config(state_file)

    # TODO logic

    update_state(state, state_file, config["logfile"], )
