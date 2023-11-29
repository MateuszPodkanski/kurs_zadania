import requests
from geopy.geocoders import Nominatim
import json
from datetime import datetime, timedelta
from typing import Optional

class WeatherForecast:
    
    def __init__(self, user_city, user_date):
        self.file = "weather_forecast_2/results.json"
        self.data_from_file : Optional[dict] = self.read_file()
        self.user_city : str = user_city
        self.user_date : datetime = user_date

    
    def get_tomorrow_date_optional(self):
        if self.user_date == "":
            self.user_date = datetime.now().date()
            self.user_date = self.user_date + timedelta(days=1)
            self.user_date = self.user_date.strftime("%Y-%m-%d")
    
    def find_latitude_and_longitude(self):
        geolocator = Nominatim(user_agent="weather_forecast")
        location = geolocator.geocode(self.user_city)
        return location.latitude, location.longitude
    
    def read_file(self):
        try:
            with open(self.file) as file:
                self.data = json.loads(file.read())
                return self.data
        except FileNotFoundError:
            print("Plik 'results.json' nie znaleziony.")
            return {}
    

    @staticmethod
    def parse_response_to_find_rain(response):
        response_dict = json.loads(response.text)
        rain_sum = response_dict.get("daily").get("rain_sum")
        return rain_sum
    
    def search_weather_in_api(self):
        latitude, longitude = self.find_latitude_and_longitude()
    
        url_address = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={self.user_date}&end_date={self.user_date}")
        response = requests.get(url=url_address)
        
        if response.status_code == 200:
            rain_sum = self.parse_response_to_find_rain(response)
            rain_sum = rain_sum[0]
            if rain_sum == None:
                print("We couldn't upload weather information for you")
            elif float(rain_sum) > 0.0:
                verdict = "Będzie padać"
            elif float(rain_sum) == 0.0:
                verdict = "Nie będzie padać"
            else:
                verdict = "Nie wiem"
            return verdict
        else:
            print("We couldn't upload weather information for you")
        

    def __getitem__(self,item):
        searched_city, searched_date = item
        for city_name, city_data in self.data_from_file.items():
            if searched_city == city_name:
              for date, verdict in city_data.items():
                  if searched_date == date:
                      print (f"Dnia {searched_date} w {searched_city} {verdict}")
                      return True
        return False
            
    def __setitem__(self, key, value):
        city, date = key
        if city not in self.data_from_file:
            self.data_from_file[city] = {}
        self.data_from_file[city][date] = value
        self.write_file()        

                    
    def write_file(self):
        with open (self.file,mode = "w") as file:
            file.write(json.dumps(self.data))
    
    def __iter__(self):
        if not self.data_from_file :
            print("Nothing saved")
            return iter ({})
        else:
            return iter(self.data_from_file.items())
    
user_city = input("Please enter the city for which you would like to know the forecast: ").capitalize()
user_date = input("Please enter the date for which you would like to know the forecast: ")
                      
weather_forecast = WeatherForecast(user_city = user_city, user_date = user_date)
weather_forecast.get_tomorrow_date_optional()
weather_forecast.find_latitude_and_longitude()
if weather_forecast[(weather_forecast.user_city),(weather_forecast.user_date)] == False:
   verdict = weather_forecast.search_weather_in_api()
   print(f"Dnia {weather_forecast.user_date} w {user_city} {verdict} ")
   weather_forecast[weather_forecast.user_city, weather_forecast.user_date] = verdict

for info in weather_forecast:
   print(info)