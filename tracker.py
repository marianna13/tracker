import requests


class Tracker:
    def __init__(self, url):
        self.url = url

    def add(self, item: str, status: str):

        res = requests.post(
            self.url+"item",
            headers={
                "accept": "application/json",
                "Content-Type": "application/json"
            },
            json={
                'id': item,
                'status': status
            }
        )
        return res.status_code == 201

    def update(self, item: str, status: str):
        res = requests.put(
            self.url+f"item/{item}",
            headers={
                "accept": "application/json",
                "Content-Type": "application/json"
            },
            params={
                'status': status
            }
        )
        return res.status_code == 200

    def get_item(self, item):
        res = requests.get(
            self.url+f"items/{item}",
        )
        return res.status_code == 200

    def get_all_items(self):
        res = requests.get(
            self.url+"items",
        )
        return res.json()
