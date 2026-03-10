import streamlit as st
from PIL import Image
import time

from backend import process_user_request

st.set_page_config(page_title="AI Fashion Stylist", layout="wide")

st.title("👗 AI Fashion Stylist")
st.write("Your personal fashion agent powered by weather and style intelligence")

# ---- USER INPUTS ----

city = st.text_input("Enter your city")

gender = st.selectbox(
    "Select Gender",
    ["Male", "Female", "Unisex"]
)

style = st.selectbox(
    "Select Style",
    [
        "Casual",
        "Formal",
        "Streetwear",
        "Minimalist",
        "Party",
        "Traditional",
        "Sporty",
        "Business Casual",
        "Vacation",
        "Smart Casual"
    ]
)

uploaded_file = st.file_uploader(
    "Upload your image",
    type=["jpg", "jpeg", "png"]
)

# ---- GENERATE BUTTON ----

generate = st.button("✨ Generate Outfit")

# ---- PROCESS ----

if generate:

    if uploaded_file is None or city == "":
        st.warning("Please upload an image and enter your city.")

    else:

        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", width=300)

        # Processing message
        with st.spinner("🧠 Your fashion agent is getting you the best outfit..."):
            time.sleep(2)
            result = process_user_request(image, city, style, gender)

        # ---- WEATHER ----

        st.subheader("🌤 Weather Details")
        st.write("Temperature:", result["temperature"], "°C")
        st.write("Weather Code:", result["weather_code"])

        # ---- OUTFITS ----

        st.subheader("👕 Outfit Recommendations")
        st.success("Here are some outfits perfect for today 👇")

        if "outfits" in result:
            for outfit in result["outfits"]:
                st.write("•", outfit)
        else:
            st.warning("No outfits generated.")

        # ---- COLORS ----

        st.subheader("🎨 Recommended Colors")

        if "colors" in result:
            for color in result["colors"]:
                st.write("•", color)}
