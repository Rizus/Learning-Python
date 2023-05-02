import requests


def get_location_info():
    return requests.get("https://geoip.svc.nvidia.com/json/"). json()


if __name__ == '__main__':
    print(get_location_info())
