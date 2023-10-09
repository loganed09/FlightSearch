from datetime import datetime, timedelta

class FlightData():
    def __init__(self):
        self.departure_airport_code = 'CMH' 
        self.today = datetime.now()
        self.six_months_out = self.today + timedelta(days=(30*6))
        self.departure_city = "Columbus"
        self.date_from = datetime.strftime(self.today, "%d/%m/%Y")
        self.date_to = datetime.strftime(self.six_months_out, "%d/%m/%Y")
        self.curr = 'USD'


    def get_params(self, fly_to):
        return {
            "fly_from": self.departure_airport_code,
            "fly_to": fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "curr": self.curr
        }
    


flight_data = FlightData()

print(flight_data.date_to)