import requests

def get_weather(city):

    # Step 1: Convert city to latitude & longitude
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_response = requests.get(geo_url).json()

    if "results" not in geo_response:
        return "Unknown", "N/A"

    lat = geo_response["results"][0]["latitude"]
    lon = geo_response["results"][0]["longitude"]

    # Step 2: Get weather data
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    weather_response = requests.get(weather_url).json()

    temperature = weather_response["current_weather"]["temperature"]
    windspeed = weather_response["current_weather"]["windspeed"]
    weathercode = weather_response["current_weather"]["weathercode"]

    return weathercode, temperature