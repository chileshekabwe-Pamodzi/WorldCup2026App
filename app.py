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

# Add interactive Features to the prediction
# User input form
st.subheader("Predict Player Position")

age = st.number_input("Age", min_value=15, max_value=40, value=20)
height = st.number_input("Height (cm)", min_value=150, max_value=210, value=180)
weight = st.number_input("Weight (kg)", min_value=50, max_value=100, value=70)
foot = st.selectbox("Preferred Foot", ["Left", "Right"])

if st.button("Predict"):
    # Example: pass inputs to your model
    prediction = model.predict([[age, height, weight, 1 if foot == "Right" else 0]])
    st.write("Predicted Player Position:", prediction[0])

# organise inputs in a side bar
st.sidebar.header("Player Inputs")

age = st.sidebar.number_input("Age", min_value=15, max_value=40, value=20)
height = st.sidebar.number_input("Height (cm)", min_value=150, max_value=210, value=180)
weight = st.sidebar.number_input("Weight (kg)", min_value=50, max_value=100, value=70)
foot = st.sidebar.selectbox("Preferred Foot", ["Left", "Right"])
#Keeps interface clean

# Show predictions with Style
if st.sidebar.button("Predict"):
    prediction = model.predict([[age, height, weight, 1 if foot == "Right" else 0]])
    st.success(f"Predicted Position: {prediction[0]}")
# st.success gives a green hightlight, making results stand out

# Add charts to visualise dataset
import matplotlib.pyplot as plt

st.subheader("Player Age Distribution")
fig, ax = plt.subplots()
ax.hist(data["age"], bins=20, color="skyblue")
st.pyplot(fig)
# Users see a quick chart of the players ages