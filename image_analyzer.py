from PIL import Image
import numpy as np

def analyze_image(image):
    """
    Simple image analyzer that estimates brightness
    and returns skin tone category.
    """

    # Convert image to numpy array
    img = np.array(image)

    # Calculate average brightness
    brightness = img.mean()

    # Determine tone category
    if brightness < 85:
        return "Dark"
    elif brightness < 170:
        return "Neutral"
    else:
        return "Light"
