url = "http://api.open-notify.org/iss-now.json"
import requests, time, json
from geopy import distance


def run():
    response1 = requests.get(url)
    dati1 = response1.json()["iss_position"]
    lat1, lon1 = float(dati1["latitude"]), float(dati1["longitude"])
    print(lat1, lon1)
    time.sleep(6)
    response2 = requests.get(url)
    dati2 = response2.json()["iss_position"]
    lat2, lon2 = float(dati2["latitude"]), float(dati2["longitude"])
    print(lat2, lon2)

    pos1 = (lat1, lon1)
    pos2 = (lat2, lon2)
    dist = distance.distance(pos1, pos2).km
    vel = dist * 600

    return vel


if __name__ == "__main__":
    run()
