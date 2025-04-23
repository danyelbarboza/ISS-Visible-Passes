import requests
from datetime import datetime, timezone, timedelta
from config import Config

class N2yoAPI:
    def __init__(self):
        self.norad_id = Config().norad_id
        self.latitude = Config().latitude
        self.longitude = Config().longitude
        self.observer_alt = Config().observer_alt
        self.days = Config().days
        self.min_visibility = Config().min_visibility
        self.api_key = Config().api_key
        self.gmt = Config().gmt
    
    def fetch_data(self):
        response = requests.get(f"https://api.n2yo.com/rest/v1/satellite/visualpasses/{self.norad_id}/{self.latitude}/{self.longitude}/{self.observer_alt}/{self.days}/{self.min_visibility}/&apiKey={self.api_key}")
        return response.json()
    
    def display_passes(self):
        passes = self.fetch_data()["passes"]
        for p in passes:
            timestamp = int(p['startUTC'])
            dt_utc = datetime.fromtimestamp(timestamp, tz=timezone.utc)
            dt_local = dt_utc.astimezone(timezone(timedelta(hours=self.gmt)))
            print(f"Start: {dt_local.strftime('%d/%m/%Y %H:%M')}, Duration: {p['duration']}s")

if __name__ == "__main__":
    api = N2yoAPI()
    api.display_passes()

