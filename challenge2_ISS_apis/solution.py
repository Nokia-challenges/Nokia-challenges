import geopy.distance as gp
import requests

import time


url = "http://api.open-notify.org/iss-now.json"


def run():
    idk = requests.get(url).json()

    pos1 = (idk["iss_position"]["latitude"], idk["iss_position"]["longitude"])

    time.sleep(4)

    idk = requests.get(url).json()

    pos2 = (idk["iss_position"]["latitude"], idk["iss_position"]["longitude"])

    ris = int(1000 * gp.great_circle(pos2, pos1).kilometers)

    print(ris)
    return ris


if __name__ == "__main__":
    run()
