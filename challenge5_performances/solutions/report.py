import os
from pathlib import Path
from typing import Union

from openpyxl import Workbook


class Report:
    def __init__(self, path: Union[str, os.PathLike]):
        self.path = Path(path)
        self.wb = Workbook()
