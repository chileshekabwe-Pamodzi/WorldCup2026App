# Step 1 Add Your Stream Code Here
import streamlit as st
import joblib
import pandas as pd

st.title("World Cup 2026 Analysis")

# Load dataset
data = pd.read_csv("WorldCup2026_cleaned.csv")
st.write("Sample of cleaned dataset")
st.write(data.head())

# load model
model = joblib.load(open("player_position_model.pkl", "rb"))
st.write("Model load successfully!")