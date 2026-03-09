from PIL import Image
import numpy as np


def preprocess_image(image):
    """
    Convert image to numpy array and resize for analysis
    """

    # Resize image to standard size
    image = image.resize((224, 224))

    # Convert to numpy array
    img_array = np.array(image)

    return img_array


def analyze_image(image):
    """
    Analyze image features for fashion recommendation
    """

    img_array = preprocess_image(image)

    # Calculate brightness
    brightness = np.mean(img_array)

    if brightness < 80:
        lighting = "dark"
    elif brightness < 170:
        lighting = "normal"
    else:
        lighting = "bright"

    # Find dominant color
    pixels = img_array.reshape(-1, 3)
    avg_color = pixels.mean(axis=0)

    r, g, b = avg_color

    if r > g and r > b:
        dominant_color = "red tone"
    elif g > r and g > b:
        dominant_color = "green tone"
    elif b > r and b > g:
        dominant_color = "blue tone"
    else:
        dominant_color = "neutral"

    result = {
        "lighting": lighting,
        "brightness": float(brightness),
        "dominant_color": dominant_color
    }

    return result