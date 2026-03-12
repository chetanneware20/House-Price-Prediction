import streamlit as st
import pandas as pd
import pickle
import os
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="House Price Prediction")

st.title("🏠 House Price Prediction App")
st.write("Simple Machine Learning model to predict house price")

# Sample dataset (no csv needed)
data = {
    "area":[2000,1500,3000,2500,1800,3500],
    "bedrooms":[3,2,4,3,3,5],
    "bathrooms":[2,1,3,2,2,4],
    "stories":[2,1,2,2,1,3],
    "parking":[1,1,2,2,1,2],
    "price":[5000000,3200000,8500000,6700000,4200000,12000000]
}

df = pd.DataFrame(data)

X = df[["area","bedrooms","bathrooms","stories","parking"]]
y = df["price"]

# Train model if not exists
if not os.path.exists("model.pkl"):
    model = LinearRegression()
    model.fit(X,y)
    pickle.dump(model,open("model.pkl","wb"))

# Load model
model = pickle.load(open("model.pkl","rb"))

st.header("Enter House Details")

area = st.number_input("Area (sq ft)",1000,5000,2000)
bedrooms = st.slider("Bedrooms",1,5,3)
bathrooms = st.slider("Bathrooms",1,4,2)
stories = st.slider("Stories",1,3,2)
parking = st.slider("Parking",0,2,1)

input_data = pd.DataFrame({
    "area":[area],
    "bedrooms":[bedrooms],
    "bathrooms":[bathrooms],
    "stories":[stories],
    "parking":[parking]
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated House Price: ₹{int(prediction[0]):,}")
