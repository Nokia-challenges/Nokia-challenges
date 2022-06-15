from geopy import distance

import requests
import time

url = "http://api.open-notify.org/iss-now.json"


def run():
    info1 = requests.get(url).json()
    time.sleep(5)
    info2 = requests.get(url).json()

    pos1 = (info1["iss_position"]["latitude"], info1["iss_position"]["longitude"])
    pos2 = (info2["iss_position"]["latitude"], info2["iss_position"]["longitude"])

    timedif = info2["timestamp"] - info1["timestamp"]

    dist = distance.great_circle(pos1, pos2).km * 1000

    velocity = 3.6 * dist / timedif
    print(velocity)

    return velocity


if __name__ == "__main__":
    run()
