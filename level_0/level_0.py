#!/usr/bin/python3
if __name__ == "__main__":
    import requests

    API_ENDPOINT = "http://158.69.76.135/level0.php"
    data = {"id":"1300", "holdthedoor":"Submit+Query"}
    for i in range(0, 1020):
        r = requests.post(url = API_ENDPOINT, data = data)
