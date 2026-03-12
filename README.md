# House-Price-Prediction
# 🏠 House Price Prediction using Machine Learning

This project predicts house prices using Machine Learning and deploys the model using Streamlit.

## Features
- Machine Learning Regression Model
- Exploratory Data Analysis
- Streamlit Web App
- Interactive Price Prediction

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## Project Structure

house-price-prediction
│
├── app.py
├── train_model.py
├── requirements.txt
├── model.pkl
└── data/housing.csv

## Run Locally

Install dependencies

pip install -r requirements.txt

Train Model

python train_model.py

Run Streamlit App

streamlit run app.py

## Demo

User enters:
- Area
- Bedrooms
- Bathrooms
- Stories
- Parking

App predicts estimated house price.
