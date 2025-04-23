import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv() 
        self.norad_id = 25544
        self.latitude = float(os.getenv("latitude")) 
        self.longitude = float(os.getenv("longitude")) 
        self.observer_alt = int(os.getenv("observer_alt")) 
        self.days = 10
        self.min_visibility = 10
        self.api_key = os.getenv("API_KEY")
        self.gmt = int(os.getenv("gmt"))