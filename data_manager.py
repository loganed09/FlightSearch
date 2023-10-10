import requests
from datetime import * 
import os

class DataManager:
    def __init__(self):
        self.SHEETY_API = os.environ.get("SHEETY_API")
        self.SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
        self.SHEETY_HEADERS = {
            "Authorization": f"Bearer {self.SHEETY_TOKEN}"
        }

    ##### Retrieves data 
    def get_data(self):
        response = requests.get(url=self.SHEETY_API, headers=self.SHEETY_HEADERS)
        sheet_data = response.json()
        return sheet_data['prices']
    
    #### Adds data to specefic row
    def put_data(self, new_code, id_num):
        new_data = {
            "price": {
                "iataCode": new_code
            }
        }
        response = requests.put(url=f'{self.SHEETY_API}/{id_num}', json=new_data, headers=self.SHEETY_HEADERS)
        print(response.text)