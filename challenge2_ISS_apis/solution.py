import geopy
from geopy import distance

import requests
import time

url = "http://api.open-notify.org/iss-now.json"


def run():
    info1 = requests.get(url).json()
    time.sleep(3.6)
    info2 = requests.get(url).json()

    pos1 = (info1["iss_position"]["latitude"], info1["iss_position"]["longitude"])
    pos2 = (info2["iss_position"]["latitude"], info2["iss_position"]["longitude"])

    dist = distance.great_circle(pos1, pos2).km

    velocity = dist * 1000
    return velocity


if __name__ == "__main__":
    run()
