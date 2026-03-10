def recommend_colors(skin_tone):

    palette = {

        "Fair": [
            "Emerald Green",
            "Royal Blue",
            "Burgundy",
            "Lavender"
        ],

        "Light": [
            "Navy Blue",
            "Olive Green",
            "Soft Pink",
            "Teal"
        ],

        "Medium": [
            "Mustard Yellow",
            "Coral",
            "Turquoise",
            "Forest Green"
        ],

        "Olive": [
            "Cream",
            "Maroon",
            "Rust",
            "Deep Purple"
        ],

        "Brown": [
            "Bright White",
            "Cobalt Blue",
            "Orange",
            "Gold"
        ],

        "Dark": [
            "Bright Yellow",
            "Mint Green",
            "Magenta",
            "Sky Blue"
        ]
    }

    return palette.get(skin_tone, ["Black", "White"])
