import streamlit as st

import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/best_model.pkl")

st.title("🚢 Titanic Survival Prediction App")

st.write("Enter passenger details to predict survival.")

# Inputs
age = st.slider("Age", 0, 80, 25)
fare = st.slider("Fare", 0.0, 500.0, 50.0)

pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
embarked = st.selectbox("Embarked", ["S", "C", "Q"])

sibsp = st.slider("Siblings/Spouses Aboard", 0, 5, 0)
parch = st.slider("Parents/Children Aboard", 0, 5, 0)

# Create input dataframe
input_data = pd.DataFrame({
    "Age": [age],
    "Fare": [fare],
    "Pclass": [pclass],
    "Sex": [sex],
    "Embarked": [embarked],
    "SibSp": [sibsp],
    "Parch": [parch]
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.success(f"🟢 Survived (Probability: {probability:.2f})")
    else:
        st.error(f"🔴 Did Not Survive (Probability: {probability:.2f})")