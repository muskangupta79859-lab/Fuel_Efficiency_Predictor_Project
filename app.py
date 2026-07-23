import streamlit as st
import tensorflow as tf
import numpy as np

# Load trained model
model = tf.keras.models.load_model("fuel_efficiency_model.keras")

st.set_page_config(page_title="Fuel Efficiency Prediction", page_icon="🚗")

st.title("🚗 Fuel Efficiency Prediction")
st.write("Enter the vehicle details below to predict MPG.")

cylinders = st.number_input("Cylinders", min_value=3, max_value=12, value=4)
displacement = st.number_input("Displacement", value=120.0)
horsepower = st.number_input("Horsepower", value=90.0)
weight = st.number_input("Weight", value=2500.0)
acceleration = st.number_input("Acceleration", value=15.0)
model_year = st.number_input("Model Year", min_value=70, max_value=82, value=82)
origin = st.selectbox("Origin", [1, 2, 3])

if st.button("Predict Fuel Efficiency"):
    data = np.array([[cylinders,
                      displacement,
                      horsepower,
                      weight,
                      acceleration,
                      model_year,
                      origin]])

    prediction = model.predict(data)

    st.success(f"Predicted Fuel Efficiency: {prediction[0][0]:.2f} MPG")
