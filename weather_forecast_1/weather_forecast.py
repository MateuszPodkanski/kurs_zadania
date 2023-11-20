import requests
from geopy.geocoders import Nominatim
import json
from datetime import datetime, timedelta

def get_tomorrow_date(user_date):
    if user_date == "":
        user_date = datetime.now().date()
        user_date = user_date + timedelta(days=1)
        user_date = user_date.strftime("%Y-%m-%d")
        return user_date
def read_file():
    try:
        with open("C:/Python/kurs/zadania/weather_forecast/results.json") as file:
            data = json.loads(file.read())
            return data
    except FileNotFoundError:
        print("Plik 'results.json' nie znaleziony.")

def find_in_file():
    for city,dates in data.items():
        if user_city == city:
            for date,verdict in dates.items():
                if user_date == date:
                    print (f"Dnia {user_date} w {user_city} {verdict}")
                    return  True
                
                else:
                    return False
        
        else:
            return False

def find_latitude_and_longitude(city):
    geolocator = Nominatim(user_agent="weather_forecast")
    location = geolocator.geocode(city)
    return location.latitude, location.longitude

def parse_response_to_find_rain(response):
    response_dict = json.loads(response.text)
    rain_sum = response_dict.get("daily").get("rain_sum")
    return rain_sum

def search_weather_in_api(date, city):
    latitude, longitude = find_latitude_and_longitude(city)
    
    url_address = (f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={date}&end_date={date}")
    response = requests.get(url=url_address)
        
    if response.status_code == 200:
        rain_sum = parse_response_to_find_rain(response)
        rain_sum = rain_sum[0]
        if rain_sum == None:
            print("We couldn't upload weather information for you")
        elif float(rain_sum) > 0.0:
            verdict = "Będzie padać"
        elif float(rain_sum) == 0.0:
            verdict = "Nie będzie padać"
        else:
            verdict = "Nie wiem"
        return rain_sum, verdict
    else:
        print("We couldn't upload weather information for you")
        

def set_in_file():
    if user_city in data:
            data[user_city][user_date] = verdict
    else:
        data[user_city] = {user_date: verdict}
    return data

             
def write_file():
        with open ("C:/Python/kurs/zadania/weather_forecast/results.json",mode = "w") as file:
            file.write(json.dumps(data))


user_city = input("Please enter the city for which you would like to know the forecast: ").capitalize()
user_date = input("Please enter the date for which you would like to know the forecast: ")

user_date = get_tomorrow_date(user_date)

data = read_file()

if find_in_file() == False:

    rain_sum, verdict = search_weather_in_api(user_date, user_city)
    print (f"Dnia {user_date} w {user_city} {verdict}")
    set_in_file()

write_file()
