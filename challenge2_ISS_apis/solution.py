url = "http://api.open-notify.org/iss-now.json"

import requests
import time
import geopy.distance


def run():
    r = requests.get(url).json()
    pos = {r["iss_position"]["latitude"], r["iss_position"]["longitude"]}
    tempo = ["timestamp"]

    time.sleep(5)

    r = requests.get(url).json()
    pos2 = {r["iss_position"]["latitude"], r["iss_position"]["longitude"]}
    tempo = {"timestamp"}

    timediff = tempo - tempo
    RIS = int(geopy.great_circle(pos2, pos))

    velocita = RIS / timediff

    return velocita


if __name__ == "__main__":
    run()
