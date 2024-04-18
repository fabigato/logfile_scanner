# logfile_scanner
a script for generic logfile scanning. It scans, finds what you want and does what you want with it

use poetry build to create both a wheel and sdist packages.
Example command to install the wheel:
````commandline
python3.10 -m pip install --force-reinstall logfile_scanner-0.1.0-py3-none-any.whl
````

Example command to run the installed package as a python3.10 module:
```commandline
python3.10 -m logfile_scanner.main -c /path/to/vlc_settings.yml -l /path/to/debug.txt -f /home/username/.local/lib/python3.10/site-packages/logfile_scanner/devenv_files/vlc_logs_test
```
