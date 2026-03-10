def generate_outfit(temp, style, skin_tone):

    outfits = []
    colors = []

    # ---------- STYLE + TEMPERATURE LOGIC ----------

    if style == "Casual":

        if temp > 30:
            outfits = [
                "Cotton T-shirt with shorts",
                "Oversized tee with relaxed jeans",
                "Linen shirt with chinos"
            ]
        elif temp > 20:
            outfits = [
                "Casual shirt with denim",
                "Polo t-shirt with chinos",
                "Henley t-shirt with jeans"
            ]
        else:
            outfits = [
                "Hoodie with jeans",
                "Sweater with denim",
                "Light jacket with chinos"
            ]

    elif style == "Formal":

        if temp > 30:
            outfits = [
                "Lightweight formal shirt with trousers",
                "Linen blazer with chinos"
            ]
        elif temp > 20:
            outfits = [
                "Formal shirt with slim trousers",
                "Blazer with chinos"
            ]
        else:
            outfits = [
                "Wool blazer with trousers",
                "Formal coat with dress pants"
            ]

    elif style == "Streetwear":

        outfits = [
            "Oversized hoodie with cargo pants",
            "Graphic tee with baggy jeans",
            "Street jacket with joggers"
        ]

    elif style == "Minimalist":

        outfits = [
            "Plain white tee with black trousers",
            "Neutral shirt with slim chinos",
            "Monochrome outfit with clean sneakers"
        ]

    elif style == "Party":

        outfits = [
            "Black shirt with slim jeans",
            "Shiny blazer with dark trousers",
            "Stylish turtleneck with leather jacket"
        ]

    elif style == "Traditional":

        outfits = [
            "Kurta with pajama",
            "Kurta with churidar",
            "Nehru jacket with kurta"
        ]

    elif style == "Sporty":

        outfits = [
            "Athletic t-shirt with joggers",
            "Gym tank with training shorts",
            "Sports hoodie with track pants"
        ]

    elif style == "Business Casual":

        outfits = [
            "Oxford shirt with chinos",
            "Polo shirt with formal trousers",
            "Light blazer with chinos"
        ]

    elif style == "Vacation":

        outfits = [
            "Hawaiian shirt with shorts",
            "Linen shirt with beach shorts",
            "Loose shirt with cotton trousers"
        ]

    elif style == "Smart Casual":

        outfits = [
            "Polo t-shirt with slim jeans",
            "Casual blazer with chinos",
            "Shirt with dark denim"
        ]

    # ---------- SKIN TONE COLORS ----------

    if skin_tone == "Fair":
        colors = ["Navy Blue", "Emerald Green", "Burgundy"]

    elif skin_tone == "Medium":
        colors = ["Olive Green", "Mustard", "Rust Orange"]

    else:
        colors = ["White", "Sky Blue", "Bright Yellow"]

    return outfits, colors
