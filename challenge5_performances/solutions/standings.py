from dataclasses import dataclass


SEASON = "2021-2022"


@dataclass
class League:
    id: int
    name: str
