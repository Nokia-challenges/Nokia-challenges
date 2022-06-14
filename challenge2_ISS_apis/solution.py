import geopy
import requests
import time

from geopy.distance import great_circle

url = "http://api.open-notify.org/iss-now.json"


def run():
    u = requests.get(url).json()

    lat1 = u["iss_position"]["latitude"]
    lon1 = u["iss_position"]["longitude"]

    time.sleep(3.6)

    u = requests.get(url).json()

    lat2 = u["iss_position"]["latitude"]
    lon2 = u["iss_position"]["longitude"]

    pos1 = (lat1, lon1)
    pos2 = (lat2, lon2)

    ris = great_circle(pos1, pos2).km * 1000
    return ris


if __name__ == "__main__":
    run()
