import requests
import time
import json
import geopy
from geopy import distance


def run():
    response1=requests.get("http://api.open-notify.org/iss-now.json")
    time.sleep(5)
    response2=requests.get("http://api.open-notify.org/iss-now.json")
    dati1 = response1.json()["iss_position"]
    lat1=float(dati1["latitude"])
    lon1=float(dati1["longitude"])

    dati2 = response2.json()["iss_position"]
    lat2=float(dati2["latitude"])
    lon2=float(dati2["longitude"])

    p1=(lat1,lon1)
    p2=(lat2,lon2)

    dist= distance.distance(p1,p2).km
    speed = (dist/5)*3600
    return speed












if __name__ == "__main__":
    run()
