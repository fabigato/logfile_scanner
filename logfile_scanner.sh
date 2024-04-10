#!/bin/bash
# a simple script to run this project with a single bash command

cd $LOGFILE_SCANNER_PATH
export CONFIG_FILE=vlc_settings.yml
export STATE_FILE=vlc_state.yml
export 	VLC_SETTINGS_FILE=scanner/vlc_settings_local.yml
. ../.venv/bin/activate
python main.py
. deactivate
