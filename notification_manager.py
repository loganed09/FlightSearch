import requests
import os
from twilio.rest import Client

class NotificationManager():
    def __init__(self):
        self.TWILIO_SID = os.environ.get("TWILIO_SID")
        self.TWILIO_AUTH = os.environ.get("TWILIO_AUTH")
        self.client = Client(self.TWILIO_SID, self.TWILIO_AUTH)

    def send_message(self, search_results):
        body = f"Found a deal! You are going to {search_results['arrival_city']} from {search_results['departure_city']} for ${search_results['price']} on {search_results['outbound_date']}!"
        print(body)

        #### TWILIO PART #####
        message = self.client.messages.create(
            from_='+18773536998',
            to='18283718274',
            body=body
        )

        print(message.status)