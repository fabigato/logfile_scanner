import argparse
import logging

from logfile_scanner.scanner.vlc import VLCScanner
from logfile_scanner.utils import get_config, read_state, setup_logger, update_state


def parse_args():
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
        epilog="Text at the bottom of help",
    )
    parser.add_argument("-c", "--configfile", dest="config_file")
    parser.add_argument("-f", "--file", dest="input_file", required=True)
    parser.add_argument("-l", "--logoutputfile", dest="log_output_file")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.log_output_file is not None:
        setup_logger(args.log_output_file)
    config = get_config(args.config_file)
    logging.info(f'reading state from {config["state_file"]}')
    state = read_state(state_path=config["state_file"], log_file=args.input_file)
    if (
        args.input_file != state["last_logfile_read"]
        or state["last_logfile_read"] == ""
    ):
        logging.info("reading log file from line 0")
        read_from = 0
    else:
        logging.info(f'reading log file from line {state["read_from_line"]}')
        read_from = state["read_from_line"]

    scanner = VLCScanner(
        db_path=config["db_path"],
        log_file=args.input_file,
        read_from=read_from,
        encoding=config["encoding"],
    )
    lines_read = scanner.scan()

    logging.info(f"{lines_read} lines read. Updating state file")
    update_state(
        state=state,
        state_file=config["state_file"],
        logfile=args.input_file,
        lines_read=lines_read,
    )


if __name__ == "__main__":
    main()
