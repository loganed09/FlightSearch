import requests
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()


sheety_flight_data = data_manager.get_data()
pprint(sheety_flight_data)
need_codes = []

for _ in range(len(sheety_flight_data)):
    if sheety_flight_data[_]['iataCode'] == '':
        need_codes.append(sheety_flight_data[_])
        flight_search.update_codes(need_codes)
        data_manager.put_data(sheety_flight_data[_]["iataCode"], sheety_flight_data[_]["id"])
        #flight_search_data = FlightData(sheety_flight_data[_]["iataCode"])
    flight_search.search_flight(flight_data.get_params(sheety_flight_data[_]["iataCode"]))


