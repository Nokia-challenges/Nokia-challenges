url = "http://api.open-notify.org/iss-now.json"
import geopy
import time
import requests
from geopy import distance, Point

def run():
    t = 5

    response = requests.get(url)
    linea = response.json()
    lon1 = linea["iss_position"]["longitude"]
    lat1 = linea["iss_position"]["latitude"]
    time.sleep(t)
    response = requests.get(url)
    linea = response.json()
    lon2 = linea["iss_position"]["longitude"]
    lat2 = linea["iss_position"]["latitude"]

    p1 = Point(lat1, lon1)
    p2 = Point(lat2, lon2)

    dist = distance.distance(p1,p2).km

    v = dist/(t/3600)
    print(v)
    pass


if __name__ == "__main__":
    run()
