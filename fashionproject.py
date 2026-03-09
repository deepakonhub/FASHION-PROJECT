import streamlit as st
from PIL import Image

st.title("AI Fashion Stylist")

st.write("Upload your photo and get outfit recommendations")

uploaded_file = st.file_uploader("Upload your image", type=["jpg","png","jpeg"])

style = st.selectbox(
    "Select your style",
    ("Casual","Formal","Party","Traditional")
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

if st.button("Generate Outfit"):
    st.write("AI is analyzing your style...")
    st.success("Recommended Outfit: White Shirt + Blue Denim Jacket")