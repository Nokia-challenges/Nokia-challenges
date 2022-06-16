from pathlib import Path
from typing import List
import timeit

import pandas as pd

import openpyxl as xls


import asyncio


from challenge5_performances.solutions.standings import League
from challenge5_performances.solutions.utils import *

leagues: List[League] = [
    League(id=4328, name="Premier League"),
    League(id=4331, name="Bundesliga"),
    League(id=4332, name="Serie A"),
    League(id=4334, name="Ligue 1"),
    League(id=4335, name="La Liga"),
    League(id=4344, name="Primeira Liga"),
    League(id=4337, name="Eredivisie"),
    League(id=4330, name="Scottish Premier League"),
    League(id=4621, name="Austrian Bundesliga"),
    League(id=4338, name="Belgian First Division A"),
    League(id=4675, name="Swiss Super League"),
    League(id=4340, name="Danish Superliga"),
    League(id=4422, name="Polish Ekstraklasa"),
    League(id=4631, name="Czech First League"),
    League(id=4336, name="Greek Superleague"),
    League(id=4671, name="Serbian Super Liga"),
    League(id=4629, name="Croatian First Football League"),
    League(id=4691, name="Romanian Liga I"),
    League(id=4690, name="Hungarian NB I"),
    League(id=4356, name="Australian A League"),
]


SEASON = "2021-2022"


path = Path.cwd() / "Standings.xlsx"


async def run():
    start = timeit.default_timer()

    dataframes = await asyncio.gather(
        *(get_league_data(compose_url(league.id, SEASON)) for league in leagues)
    )

    with pd.ExcelWriter(path) as writer:

        for i in range(len(leagues)):

            giorgio = dataframes[i]

            giorgio.to_excel(writer, sheet_name=leagues[i].name)

    xls_file = xls.load_workbook(path)

    for antonio in xls_file:
        antonio.delete_cols(idx=1, amount=1)

    xls_file.save(path)

    print(f"Execution time: {timeit.default_timer() - start}")


if __name__ == "__main__":
    asyncio.run(run())
