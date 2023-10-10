import requests
from pprint import pprint

import os

class FlightSearch():
    def __init__(self):
        self.TEQUILA_API_ENDPOINT = os.environ.get("TEQUILA_API_ENDPOINT")
        self.TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")
        self.tequila_headers = {
            "accept": "application/json",
            "apikey": self.TEQUILA_API_KEY
        }

    def update_codes(self, dict_list):
        for _ in range(len(dict_list)):
            response = requests.get(url=f"{self.TEQUILA_API_ENDPOINT}/locations/query?term={dict_list[_]['city']}&locale=en-US&location_types=city&limit=10&active_only=true", headers=self.tequila_headers)
            data = response.json()
            dict_list[_]['iataCode'] = data["locations"][0]["code"]

    def search_flight(self, params):
        response = requests.get(url=f"{self.TEQUILA_API_ENDPOINT}/v2/search", params=params, headers=self.tequila_headers)
        flights = response.json()
        #print(flights)
        for _ in range(len(flights)):
            # departure_city = 
            # arrival_city = flights["data"][_]["cityTo"]
            # price = flights["data"][_]["price"]
            # outbound_date = flights["data"][_]["local_arrival"]
            return {
                "departure_city": flights["data"][_]["cityFrom"],
                "arrival_city": flights["data"][_]["cityTo"],
                "price": flights["data"][_]["price"],
                "outbound_date": flights["data"][_]["local_arrival"].split('T')[0]
            }
            
