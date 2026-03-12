import streamlit as st
import pandas as pd
import pickle
import os
from sklearn.linear_model import LinearRegression

# Check if model exists
if not os.path.exists("model.pkl"):
    df = pd.read_csv("data/housing.csv")

    X = df[["area","bedrooms","bathrooms","stories","parking"]]
    y = df["price"]

    model = LinearRegression()
    model.fit(X,y)

    pickle.dump(model, open("model.pkl","wb"))

# Load model
model = pickle.load(open("model.pkl","rb"))

st.set_page_config(page_title="House Price Prediction")

st.title("🏠 House Price Prediction")

area = st.number_input("Area",1000,10000,2000)
bedrooms = st.slider("Bedrooms",1,10,3)
bathrooms = st.slider("Bathrooms",1,5,2)
stories = st.slider("Stories",1,4,2)
parking = st.slider("Parking",0,3,1)

input_data = pd.DataFrame({
    "area":[area],
    "bedrooms":[bedrooms],
    "bathrooms":[bathrooms],
    "stories":[stories],
    "parking":[parking]
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Predicted House Price: ₹{int(prediction[0]):,}")
