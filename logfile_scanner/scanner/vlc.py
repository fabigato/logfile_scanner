import logging
import os
import re
import urllib.parse
from typing import List

import pickledb

from logfile_scanner.scanner.base import Scanner
from logfile_scanner.utils import read_config


class VLCScanner(Scanner):
    def __init__(self, db_path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db_path = db_path

    def _process(self, lines: List[str]):
        db = pickledb.load(self.db_path, False)
        for line in lines:
            match = re.fullmatch(r"main debug: `(.*)\' successfully opened\n", line)
            if match:
                str_from, str_to = match.regs[1]
                file = os.path.basename(
                    urllib.parse.unquote(line[str_from:str_to], encoding=self.encoding)
                )
                logging.info(f"found {file}")
                count = db.get(file)
                db.set(file, count + 1)
        db.dump()
