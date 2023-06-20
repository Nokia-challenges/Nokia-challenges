import requests
import time
from math import radians, cos, sin, asin, sqrt

url = "http://api.open-notify.org/iss-now.json"

def haversine_distance(coo1, coo2):
    lon1, lat1 = map(float, coo1.values())
    lon2, lat2 = map(float, coo2.values())

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat1 - lat1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers.

    return c * r


def run():
    # start = time.time()
    coordinates1 = requests.get(url).json()["iss_position"]

    time.sleep(1)
    # end = time.time()
    coordinates2 = requests.get(url).json()["iss_position"]
    


    distance = haversine_distance(coordinates1, coordinates2)
    # print(distance/(end-start)*3600)
    print(distance*3600)


if __name__ == "__main__":
    run()
