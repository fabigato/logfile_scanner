import argparse
import logging
from os import environ

from scanner.vlc import VLCScanner
from utils import read_config, read_state, setup_logger, update_state

config_file_env = environ.get("CONFIG_FILE", "settings.yml")
state_file_env = environ.get("STATE_FILE", "settings.yml")


def parse_args():
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
        epilog="Text at the bottom of help",
    )
    parser.add_argument("-c", "--configfile", dest="config_file")
    parser.add_argument("-s", "--statefile", dest="state_file")
    parser.add_argument("-l", "--logoutputfile", dest="log_output_file")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    config_file = args.config_file if args.config_file is not None else config_file_env
    state_file = args.state_file if args.state_file is not None else state_file_env
    if args.log_output_file is not None:
        setup_logger(args.log_output_file)
    logging.info(f"reading config from {config_file}")
    config = read_config(config_file)
    logging.info(f"reading state from {state_file}")
    state = read_state(state_path=state_file_env, log_file=config["logfile"])
    if (
        config["logfile"] != state["last_logfile_read"]
        or state["last_logfile_read"] == ""
    ):
        logging.info("reading log file from line 0")
        read_from = 0
    else:
        logging.info(f'reading log file from line {state["read_from_line"]}')
        read_from = state["read_from_line"]

    scanner = VLCScanner(
        log_file=config["logfile"], read_from=read_from, encoding=config["encoding"]
    )
    lines_read = scanner.scan()

    logging.info(f"{lines_read} lines read. Updating state file")
    update_state(state, state_file, config["logfile"], lines_read)


if __name__ == "__main__":
    main()
