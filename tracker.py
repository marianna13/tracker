import requests
import random


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
            self.url+"item",
            headers={
                "accept": "application/json",
                "Content-Type": "application/json"
            },
            params={
                'id': item,
                'status': status
            }
        )
        return res.status_code == 200

    def get_item(self, item):
        res = requests.get(
            self.url+"item",
            params={
                'id': item
            }
        )
        return res.status_code == 200

    def get_all_items(self):
        res = requests.get(
            self.url+"items",
        )
        return res.json()
    
    def get_random_item(self):
        '''
        Get random item with status "not processed"
        '''
        not_processed = [item for item in self.get_all_items() if item['status'] == 'not processed']
        return random.choice(not_processed)

    def delete(self, item):
        res = requests.delete(
            self.url+"item",
            headers={
                "accept": "application/json",
                "Content-Type": "application/json"
            },
            params={
                'id': item
            }
        )
        # print(res)
        return res.status_code == 204
