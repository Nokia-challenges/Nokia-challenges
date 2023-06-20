import json, requests, time
from geopy.distance import geodesic as GD

url = "http://api.open-notify.org/iss-now.json"


def run():
    response = requests.get(url)
    json_data = json.loads(response.text)
    latitude = json_data['iss_position']['latitude']
    longitude = json_data['iss_position']['longitude']
    T1 = (latitude, longitude)
    time1 = json_data['timestamp']
    response = requests.get(url)
    time.sleep(5)
    response = requests.get(url)
    json_data = json.loads(response.text)
    latitude2 = json_data['iss_position']['latitude']
    longitude2 = json_data['iss_position']['longitude']
    T2 = (latitude2, longitude2)
    time2 = json_data['timestamp']  

    distance = GD(T1, T2).km
    timed = time2 - time1
    speed = distance/timed * 3600
    return speed


if __name__ == "__main__":
    run()
