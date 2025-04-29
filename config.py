import os
from dotenv import load_dotenv
from nominatim_client import NominatimClient


class Config:
    def __init__(self, latitude, longitude):
        load_dotenv() 
        self.norad_id = 25544
        self.latitude = float(latitude)
        self.longitude = float(longitude) 
        self.observer_alt = 0
        self.days = 10
        self.min_visibility = 60
        self.api_key = API_KEY
        self.gmt = -3