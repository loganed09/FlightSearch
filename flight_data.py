from datetime import datetime, timedelta

class FlightData():
    def __init__(self):
        self.departure_airport_code = 'CMH' 
        self.today = datetime.now()
        self.six_months_out = self.today + timedelta(days=(30*6))
        self.min_return_date = self.today + timedelta(days=14)
        self.max_return_date = self.six_months_out + timedelta(days=14)
        self.departure_city = "Columbus"
        self.date_from = datetime.strftime(self.today, "%d/%m/%Y")
        self.date_to = datetime.strftime(self.six_months_out, "%d/%m/%Y")
        self.return_from = datetime.strftime(self.min_return_date, "%d/%m/%Y")
        self.return_to = datetime.strftime(self.max_return_date, "%d/%m/%Y")
        self.curr = 'USD'

    ##### Create a dictionary for the flight search parameters
    def get_params(self, fly_to):
        return {
            "fly_from": self.departure_airport_code,
            "fly_to": fly_to,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "return_from": self.return_from,
            "return_to": self.return_to,
            "curr": self.curr
        }
    

