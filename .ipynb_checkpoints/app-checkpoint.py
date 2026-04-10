import streamlit as st
import pickle

model = pickle.load(open("diabetes_model.pkl", "rb"))

st.title("Diabetes Prediction App")

preg = st.number_input("Pregnancies", 0)
glucose = st.number_input("Glucose", 0)
bp = st.number_input("Blood Pressure", 0)
skin = st.number_input("Skin Thickness", 0)
insulin = st.number_input("Insulin", 0)
bmi = st.number_input("BMI", 0.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0)
age = st.number_input("Age", 0)

if st.button("Predict"):
    result = model.predict([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])

    if result[0] == 1:
        st.error("Patient is Diabetic")
    else:
        st.success("Patient is Not Diabetic")