import pandas as pd
import requests_async


URL_BASE = "https://www.thesportsdb.com/api/v1/json/2/lookuptable.php"

dati_utili = (
    "intRank",
    "strTeam",
    "intPlayed",
    "intWin",
    "intLoss",
    "intDraw",
    "intGoalsFor",
    "intGoalsAgainst",
    "intGoalDifference",
    "intPoints",
)
dati_italiano = (
    "rank",
    "squadra",
    "partite giocate",
    "partite vinte",
    "partite perse",
    "partite pareggiate",
    "gol fatti",
    "gol subiti",
    "differenza gol",
    "punti",
)


def compose_url(league_id: str, season: str) -> str:

    return URL_BASE + "?l=" + str(league_id) + "&s=" + season


async def get_league_data(url: str) -> pd.DataFrame:

    squadre = await requests_async.get(url)
    squadre = squadre.json()["table"]

    dict = {
        "rank": [],
        "squadra": [],
        "partite giocate": [],
        "partite vinte": [],
        "partite perse": [],
        "partite pareggiate": [],
        "gol fatti": [],
        "gol subiti": [],
        "differenza gol": [],
        "punti": [],
    }

    for i in range(len(dati_utili)):

        dato_utile = dati_utili[i]
        dato_it = dati_italiano[i]

        for squadra in squadre:
            dict[dato_it].append(squadra[dato_utile])

    #    print(dict)

    giorgio = pd.DataFrame(dict)

    return giorgio
