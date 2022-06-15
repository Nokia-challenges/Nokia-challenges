import pandas as pd

URL_BASE = "https://www.thesportsdb.com/api/v1/json/2/lookuptable.php"


def compose_url(league_id: str, season: str) -> str:
    
    url = URL_BASE + "?l=" + league_id + "&s=" + season

    pass


async def get_league_data(url: str) -> pd.DataFrame:
    """
    Get league data asynchronously and return as a pandas dataframe
    """
    pass


async def await_api_response(url: str):
    print(f"Calling API with url {url}")
    return await get_league_data(url)
