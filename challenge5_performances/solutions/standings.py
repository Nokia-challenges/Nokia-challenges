from dataclasses import dataclass
import os
from typing import List, Union

from report import Report

SEASON = "2021-2022"


@dataclass
class League:
    id: int
    name: str


class Standings(Report):
    """
    Model to create standings Excel file from pandas dataframe
    """

    def __init__(self, path: Union[str, os.PathLike], leagues: List[League]):
        super().__init__(path)
        pass
