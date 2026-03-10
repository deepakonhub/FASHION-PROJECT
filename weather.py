import requests

def get_weather(city):

    # Get latitude & longitude from city
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_data = requests.get(geo_url, verify=False).json()

    if "results" not in geo_data:
        return None, None

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

    # Get weather
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    weather_data = requests.get(weather_url, verify=False).json()

    temperature = weather_data["current_weather"]["temperature"]
    weather_code = weather_data["current_weather"]["weathercode"]

    return temperature, weather_code
