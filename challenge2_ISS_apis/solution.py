import requests
import time

from geopy.distance import great_circle

url = "http://api.open-notify.org/iss-now.json"


def run():
    u = requests.get(url).json()

    lat1 = u["iss_position"]["latitude"]
    lon1 = u["iss_position"]["longitude"]
    time1 = u["timestamp"]

    time.sleep(5)

    u = requests.get(url).json()

    lat2 = u["iss_position"]["latitude"]
    lon2 = u["iss_position"]["longitude"]
    time2 = u["timestamp"]

    pos1 = (lat1, lon1)
    pos2 = (lat2, lon2)
    timediff=time2-time1

    dist = great_circle(pos1, pos2).km * 1000
    speed=(dist/timediff)*3.6

    print(speed)
    return speed


if __name__ == "__main__":
    run()
