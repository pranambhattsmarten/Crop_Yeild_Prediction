import streamlit as st
import pickle
import pandas as pd

st.header('Crop Yield Prediction App')

# Input from users
col1, col2 = st.columns(2)

with col1:
    temp = st.number_input("Enter average temperature in C. during the growing season")

with col2:
    rain = st.number_input("Enter total amount of rainfall received")

soil_quality = st.slider("Soil Quality", 0, 10, 1)

col1, col2 = st.columns(2)

with col1:
    humidity = st.number_input("Enter average relative humidity during the growing season")

with col2:
    fertilizer_use = st.number_input("Enter the amount of fertilizer applied to the crops")

col1, col2 = st.columns(2)

with col1:
    pesticide_use = st.number_input("Enter amount of pesticide used on the crops")

with col2:
    sunlight_hours = st.number_input("Enter total number of sunlight hours the crops received during the growing season")

col1, col2 = st.columns(2)

with col1:
    plant_density = st.number_input("Enter number of plants per hectare")

with col2:
    irrigation = st.number_input("Enter total amount of irrigation water applied to the crops")

col1, col2 = st.columns(2)

with col1:
    crop_type_inp = st.selectbox(
        "What type of crop being grown?",
        ("Corn", "Rice", "Soybean", "Wheat")
    )

with col2:
    farm_area = st.number_input("Enter total area of the farm")

# Define the crop type mapping
crop_type_mapping = {
    "Corn": 1,
    "Rice": 2,
    "Soybean": 3,
    "Wheat": 4
}

crop_type_encoded = crop_type_mapping[crop_type_inp]

# Load the model and the scaler
with open('best_model.pkl', 'rb') as file:
    data = pickle.load(file)
    model = data["model"]
    scaler = data["scaler"]

# with open('scaler.pkl', 'rb') as file:
#     scaler = pickle.load(file)

# Function to preprocess the input features
def preprocess_input(temp, rain, soil_quality, fertilizer_use, humidity, pesticide_use, sunlight_hours,
                     plant_density, irrigation, crop_type_encoded, farm_area):
    print("Processing inputs")
    columns = ['temperature', 'rainfall', 'soil_quality', 'fertilizer_use', 'humidity',
       'pesticide_use', 'sunlight_hours', 'plant_density', 'irrigation',
       'crop_type', 'farm_area']
    input_data = pd.DataFrame([[
        temp, rain, soil_quality, fertilizer_use, humidity, pesticide_use, sunlight_hours,
        plant_density, irrigation, crop_type_encoded, farm_area
    ]], columns=columns)
    num_ft =  ['temperature', 'rainfall', 'soil_quality', 'humidity', 'fertilizer_use',
                      'pesticide_use', 'sunlight_hours', 'plant_density', 'irrigation', 'farm_area']
    print("Empty dataframe created:\n {}".format(input_data.loc[:, num_ft]))
    input_data.loc[:, num_ft] = scaler.transform(input_data.loc[:, num_ft])
    print("Dataframe created:\n {}".format(input_data))
    return input_data

# Button to make predictions
if st.button('Predict Crop Yield'):
    input_features = preprocess_input(
        temp, rain, soil_quality, fertilizer_use, humidity, pesticide_use, sunlight_hours,
        plant_density, irrigation, crop_type_encoded, farm_area
    )
    print(input_features)
    prediction = model.predict(input_features)
    st.write("Predicted Crop Yield is: ", prediction[0])