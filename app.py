import streamlit as st
import tensorflow as tf
import keras
import joblib
from PIL import Image
import numpy as np

uploaded = st.file_uploader("Add Image", type=["jpg", "jpeg", "png"])

model = keras.models.load_model("best_model.h5")
class_names = joblib.load("class_names.pkl")

def preprosses(image):
    img = image.resize((128,128))
    img_array = np.array(img, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array


if uploaded:
    
    image = Image.open(uploaded).convert("RGB")
    st.image(image,caption="Uploaded Image", width=300)
    
    if st.button("Detect Disease"):
        with st.spinner("Image Preprocessing"):
            img_array = preprosses(image)
            st.success("Successfully Processed")

        with st.spinner("Detecting Disease"):
            predictions = model.predict(img_array)
            class_index = np.argmax(predictions)
            confidence = np.max(predictions)
            disease = class_names[class_index]
            
            
            st.success(f"**Prediction: {disease}** ({confidence:.1f}% confidence)")
            
    
    
    
    
    

