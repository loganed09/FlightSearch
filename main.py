import requests
from datetime import datetime
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()


sheety_flight_data = data_manager.get_data()
pprint(sheety_flight_data)
need_codes = [] 

for _ in range(len(sheety_flight_data)):
    if sheety_flight_data[_]['iataCode'] == '':
        need_codes.append(sheety_flight_data[_])
        flight_search.update_codes(need_codes)
        data_manager.put_data(sheety_flight_data[_]["iataCode"], sheety_flight_data[_]["id"])


for _ in range(len(sheety_flight_data)):
    flight_results = flight_search.search_flight(flight_data.get_params(sheety_flight_data[_]["iataCode"]))
    
    if sheety_flight_data[_]["lowestPrice"] > flight_results["price"]: 
        notification_manager.send_message(flight_results)

