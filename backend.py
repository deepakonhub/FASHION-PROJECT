from weather import get_weather
from vision import analyze_image
from ai_engine import generate_outfit

def process_user_request(image, city, style, gender):

    temperature, weather_code = get_weather(city)

    skin_tone = analyze_image(image)

    outfits, colors = generate_outfit(temperature, style, skin_tone)

    return {
        "temperature": temperature,
        "weather_code": weather_code,
        "outfits": outfits,
        "colors": colors
    }
