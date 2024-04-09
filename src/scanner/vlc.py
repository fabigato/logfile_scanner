from typing import List

from base import Scanner


class VLCScanner(Scanner):
    def _process(self, lines: List[str]):
        raise NotImplementedError()
