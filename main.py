import requests
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint

data_manager = DataManager()
flight_search = FlightSearch()
#flight_data = FlightData()


flight_data = data_manager.get_data()
pprint(flight_data)
need_codes = []

for _ in range(len(flight_data)):
    if flight_data[_]['iataCode'] == '':
        need_codes.append(flight_data[_])
        flight_search.update_codes(need_codes)
        data_manager.put_data(flight_data[_]["iataCode"], flight_data[_]["id"])


