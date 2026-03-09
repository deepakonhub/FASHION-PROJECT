import random

def generate_outfit(weather, style, colors):

    casual = [
        "Denim jeans with a white t-shirt",
        "Oversized hoodie with sneakers",
        "Cargo pants with a graphic tee"
    ]

    formal = [
        "Blazer with dress pants",
        "Formal shirt with leather shoes",
        "Suit with tie"
    ]

    party = [
        "Black jacket with slim jeans",
        "Shiny shirt with boots",
        "Designer blazer outfit"
    ]

    traditional = [
        "Kurta with pajama",
        "Sherwani with mojris",
        "Ethnic kurta with jacket"
    ]

    style_dict = {
        "Casual": casual,
        "Formal": formal,
        "Party": party,
        "Traditional": traditional
    }

    outfit = random.choice(style_dict[style])

    return f"Based on {weather} and detected colors {colors}, we recommend: {outfit}"
    return text, color