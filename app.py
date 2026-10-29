
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Food Recognition",
    page_icon="🍽️"
)

st.title("🍽️ Food Recognition & Calorie Estimation")
st.write("Upload a food image to identify the food and estimate its calories.")

# Load trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("food_recognition_model.keras")

model = load_model()

# Food categories
class_names = [
    "pizza",
    "hamburger",
    "sushi",
    "ice_cream",
    "french_fries"
]

# Approximate calorie references
calories = {
    "pizza": "285 kcal per slice",
    "hamburger": "354 kcal per burger",
    "sushi": "200 kcal per typical serving",
    "ice_cream": "207 kcal per 100 g",
    "french_fries": "312 kcal per 100 g"
}

uploaded_file = st.file_uploader(
    "Choose a food image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Recognize Food"):
        resized_image = image.resize((128, 128))

        image_array = np.array(
            resized_image,
            dtype=np.float32
        ) / 255.0

        image_array = np.expand_dims(image_array, axis=0)

        predictions = model.predict(image_array, verbose=0)

        index = int(np.argmax(predictions[0]))
        food = class_names[index]
        confidence = float(predictions[0][index]) * 100

        st.success(f"Predicted Food: {food.replace('_', ' ').title()}")
        st.metric("Prediction Confidence", f"{confidence:.2f}%")
        st.info(f"Estimated Calories: {calories[food]}")

        st.caption(
            "Calories are approximate reference values. "
            "Actual calories depend on portion size and ingredients."
        )
