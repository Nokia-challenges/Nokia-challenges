from standings import League
from pathlib import Path
from typing import List
import timeit


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

path = Path.cwd() / "Standings.xlsx"

if __name__ == "__main__":
    start = timeit.default_timer()
    pass
    print(f"Execution time: {timeit.default_timer() - start}")
