from time import sleep

import requests
from geopy.distance import great_circle, EARTH_RADIUS

url = "http://api.open-notify.org/iss-now.json"

polling_period = 20


def calculate_speed():
    iss_coord = requests.get(url).json()
    latitude_before = iss_coord["iss_position"]["latitude"]
    longitude_before = iss_coord["iss_position"]["longitude"]
    timestamp_before = iss_coord["timestamp"]
    sleep(polling_period)
    iss_coord = requests.get(url).json()
    latitude = iss_coord["iss_position"]["latitude"]
    longitude = iss_coord["iss_position"]["longitude"]
    timestamp = iss_coord["timestamp"]

    dist = great_circle(
        (latitude_before, longitude_before),
        (latitude, longitude),
        radius=EARTH_RADIUS + 422,
    ).m
    time_delta = timestamp - timestamp_before
    speed = dist / time_delta
    return speed * 3.6


if __name__ == "__main__":
    calculate_speed()
