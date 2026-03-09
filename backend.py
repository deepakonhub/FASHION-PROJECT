from weather import get_weather

def recommend_outfit(style, gender, temperature):

    if temperature >= 30:
        weather_type = "hot"
    elif temperature >= 20:
        weather_type = "mild"
    else:
        weather_type = "cold"


    outfits = {

        "Casual": {
            "hot": [
                "Cotton T-shirt with shorts",
                "Light polo with chinos",
                "Oversized tee with denim shorts"
            ],
            "mild": [
                "T-shirt with jeans",
                "Henley shirt with chinos",
                "Casual shirt with slim jeans"
            ],
            "cold": [
                "Hoodie with jeans",
                "Sweatshirt with joggers",
                "Denim jacket with T-shirt"
            ],
            "colors": "White, Beige, Light Blue, Olive"
        },

        "Formal": {
            "hot": [
                "Linen shirt with formal trousers",
                "Lightweight blazer with chinos"
            ],
            "mild": [
                "Full sleeve shirt with trousers",
                "Blazer with formal pants"
            ],
            "cold": [
                "Wool blazer with shirt",
                "Formal coat with trousers"
            ],
            "colors": "Navy Blue, Charcoal, Grey, White"
        },

        "Streetwear": {
            "hot": [
                "Oversized graphic tee with cargo shorts",
                "Loose tee with ripped jeans"
            ],
            "mild": [
                "Hoodie with cargo pants",
                "Street jacket with joggers"
            ],
            "cold": [
                "Puffer jacket with cargo pants",
                "Layered hoodie and bomber jacket"
            ],
            "colors": "Black, Neon Green, Red, Dark Grey"
        },

        "Traditional": {
            "hot": [
                "Cotton kurta with pajama",
                "Light kurta with sandals"
            ],
            "mild": [
                "Kurta with churidar",
                "Kurta with Nehru jacket"
            ],
            "cold": [
                "Sherwani or heavy kurta",
                "Layered kurta with shawl"
            ],
            "colors": "Cream, Maroon, Royal Blue, Gold"
        },

        "Sporty": {
            "hot": [
                "Dry-fit T-shirt with shorts",
                "Athletic tank with running shorts"
            ],
            "mild": [
                "Track pants with sports tee",
                "Sports hoodie with joggers"
            ],
            "cold": [
                "Tracksuit with hoodie",
                "Thermal sports jacket"
            ],
            "colors": "Black, Blue, Neon Green"
        }

    }

    style_data = outfits.get(style, outfits["Casual"])

    outfit_list = style_data[weather_type]
    colors = style_data["colors"]

    return outfit_list, colors


def process_user_request(image, city, style, gender):

    weather_code, temperature = get_weather(city)

    outfit_list, colors = recommend_outfit(style, gender, temperature)

    return {
        "temperature": temperature,
        "weather_code": weather_code,
        "outfits": outfit_list,
        "colors": colors
    }