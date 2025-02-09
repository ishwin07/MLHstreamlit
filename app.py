import streamlit as st
import numpy as np

# Page Configuration
st.set_page_config(page_title="ML Predictions | AgriSpace", layout="centered")
st.title("🌱 Smart Agriculture Predictions")
st.markdown("<h2 style='text-align: center;'>ML Predictions</h2>", unsafe_allow_html=True)

# State Management
if 'modal_open' not in st.session_state:
    st.session_state.modal_open = False

if 'current_prediction_type' not in st.session_state:
    st.session_state.current_prediction_type = ''

# Open Modal
def open_modal(prediction_type):
    st.session_state.current_prediction_type = prediction_type
    st.session_state.modal_open = True

# Close Modal
def close_modal():
    st.session_state.modal_open = False
    st.session_state.current_prediction_type = ''

# Prediction Function
def handle_predict():
    st.success(f"Predicting {st.session_state.current_prediction_type} with input values!")

# Card Layout
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🌾 Crop Recommendation"):
        open_modal('Crop')

with col2:
    if st.button("💧 Fertilizer Recommendation"):
        open_modal('Fertilizer')

with col3:
    if st.button("📈 Yield Prediction"):
        open_modal('Yield')

# Modal-like Input
if st.session_state.modal_open:
    with st.expander(f"Enter {st.session_state.current_prediction_type} Details", expanded=True):
        
        if st.session_state.current_prediction_type == 'Crop':
            crop_n = st.number_input("Enter Nitrogen (N)", min_value=0.0)
            crop_p = st.number_input("Enter Phosphorous (P)", min_value=0.0)
            crop_k = st.number_input("Enter Potassium (K)", min_value=0.0)
            crop_temperature = st.number_input("Enter Temperature (°C)", min_value=0.0, max_value=50.0)
            crop_ph = st.number_input("Enter Soil pH Level", min_value=0.0, max_value=14.0)
            crop_rainfall = st.number_input("Enter Rainfall (mm)", min_value=0.0)
            crop_humidity = st.number_input("Enter Humidity (%)", min_value=0.0, max_value=100.0)

        elif st.session_state.current_prediction_type == 'Fertilizer':
            soil_type = st.selectbox("Select Soil Type", ["Sandy", "Black", "Red", "Clayey", "Loamy"])
            fertilizer_crop_type = st.selectbox("Select Crop Type", [
                "Wheat", "Rice", "Maize", "Cotton", "Sugarcane", "Tobacco", "Paddy", "Barley", 
                "Millets", "Oil Seeds", "Pulses", "Ground Nuts"
            ])
            fertilizer_n = st.number_input("Enter Nitrogen (N)", min_value=0.0)
            fertilizer_p = st.number_input("Enter Phosphorous (P)", min_value=0.0)
            fertilizer_k = st.number_input("Enter Potassium (K)", min_value=0.0)
            fertilizer_temp = st.number_input("Enter Temperature (°C)", min_value=0.0)
            fertilizer_humidity = st.number_input("Enter Humidity (%)", min_value=0.0)
            fertilizer_moisture = st.number_input("Enter Moisture (%)", min_value=0.0)

        elif st.session_state.current_prediction_type == 'Yield':
            yield_state = st.text_input("Enter State Name")

            # Dropdown for selecting Crop Type
            crop_options = [
                'Arecanut', 'Arhar/Tur', 'Castor seed', 'Coconut', 'Cotton(lint)',
                'Dry chillies', 'Gram', 'Jute', 'Linseed', 'Maize', 'Mesta',
                'Niger seed', 'Onion', 'Other Rabi pulses', 'Potato',
                'Rapeseed & Mustard', 'Rice', 'Sesamum', 'Small millets',
                'Sugarcane', 'Sweet potato', 'Tapioca', 'Tobacco', 'Turmeric',
                'Wheat', 'Bajra', 'Black pepper', 'Cardamom', 'Coriander',
                'Garlic', 'Ginger', 'Groundnut', 'Horse-gram', 'Jowar', 'Ragi',
                'Cashewnut', 'Banana', 'Soyabean', 'Barley', 'Khesari', 'Masoor',
                'Moong(Green Gram)', 'Other Kharif pulses', 'Safflower',
                'Sannhamp', 'Sunflower', 'Urad', 'Peas & beans (Pulses)',
                'Other oilseeds', 'Other Cereals', 'Cowpea(Lobia)',
                'Oilseeds total', 'Guar seed', 'Other Summer Pulses', 'Moth'
            ]

            yield_crop = st.selectbox("Select Crop Type", crop_options)  # Dropdown added

            yield_area = st.number_input("Enter Area in Hectares", min_value=0.0)
            yield_n = st.number_input("Enter Nitrogen (N)", min_value=0.0)
            yield_p = st.number_input("Enter Phosphorous (P)", min_value=0.0)
            yield_k = st.number_input("Enter Potassium (K)", min_value=0.0)
            yield_ph = st.number_input("Enter Soil pH Level", min_value=0.0, max_value=14.0)
            yield_temperature = st.number_input("Enter Temperature (°C)", min_value=0.0, max_value=50.0)

        # Predict Button
        if st.button("Predict"):
            handle_predict()
            close_modal()

        # Close Modal Button
        if st.button("Close"):
            close_modal()
