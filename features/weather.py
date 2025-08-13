import requests
from datetime import datetime
from logs import logger

def get_weather(city_name):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1" #get cords
    geo_res = requests.get(geo_url)
    geo_data = geo_res.json()

    if "results" not in geo_data or not geo_data['results']:
        logger.log('could not find city', 'error')
    
    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]
    location_name = geo_data["results"][0]["name"]
    country = geo_data["results"][0].get("country", "")

    weather_url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current=temperature_2m,windspeed_10m,precipitation"
        f"&timezone=auto"
    )

    weather_res = requests.get(weather_url)
    weather_data = weather_res.json()

    current = weather_data.get("current")
    temperature = current.get("temperature_2m", "N/A")
    windspeed = current.get("windspeed_10m", "N/A")
    precipitation = current.get("precipitation", "N/A")