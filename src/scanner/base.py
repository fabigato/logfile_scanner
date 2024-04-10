from typing import List


class Scanner:
    def __init__(self, log_file: str, read_from: int, encoding: str):
        self.log_file = log_file
        self.read_from = read_from
        self.encoding = encoding

    def scan(self) -> int:
        """
        reads the log file and does all the processing
        :return: number of lines read
        """
        with open(self.log_file, "r", encoding=self.encoding) as file:
            lines = file.readlines()[self.read_from :]
        self._process(lines=lines)
        return len(lines)

    def _process(self, lines: List[str]):
        raise NotImplementedError()
