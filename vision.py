import numpy as np

def analyze_image(image):

    img = np.array(image)

    avg_color = img.mean(axis=(0,1))

    brightness = avg_color.mean()

    if brightness > 170:
        return "Fair"

    elif brightness > 120:
        return "Medium"

    else:
        return "Deep"
