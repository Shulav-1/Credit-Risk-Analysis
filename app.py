import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("extra_tree_credit_model.pkl")
encoders = {
    "Sex": joblib.load("Sex_encoder.pkl"),
    "Saving accounts": joblib.load("Saving accounts_encoder.pkl"),
    "Checking account": joblib.load("Checking account_encoder.pkl")
}

st.title("Credit Risk Prediction App")
st.write("Enter applicant information to predict if the credit is good or bad")

age = st.number_input("Age", min_value=18, max_value=80, value=30)
sex = st.selectbox("Sex", ["Male", "Female"])
job = st.number_input("Job(0-3)", min_value=0, max_value=3, value=1)
housing = st.selectbox("Housing", ["own", "rent", "free"])  # no encoder
saving_account = st.selectbox("Saving Account", ["little", "moderate", "rich", "quite rich"])
checking_account = st.selectbox("Checking Account", ["little", "moderate", "rich"])
credit_amount = st.number_input("Credit amount", min_value=0, value=100)
duration = st.number_input("Duration (month)", min_value=1, value=12)

# Normalize inputs (make lowercase or strip spaces) if your encoder classes are lowercase
sex_norm = sex.strip().lower()
saving_account_norm = saving_account.strip().lower()
checking_account_norm = checking_account.strip().lower()

# Check what classes your encoders expect:
print("Sex classes:", encoders["Sex"].classes_)
print("Saving accounts classes:", encoders["Saving accounts"].classes_)
print("Checking account classes:", encoders["Checking account"].classes_)

# Make sure normalized input is in encoder classes (handle error gracefully)
if sex_norm not in encoders["Sex"].classes_:
    st.error(f"Invalid Sex value: {sex_norm}")
if saving_account_norm not in encoders["Saving accounts"].classes_:
    st.error(f"Invalid Saving Account value: {saving_account_norm}")
if checking_account_norm not in encoders["Checking account"].classes_:
    st.error(f"Invalid Checking Account value: {checking_account_norm}")

input_df = pd.DataFrame({
    "Age": [age],
    "Sex": [encoders["Sex"].transform([sex_norm])[0]],
    "Job": [job],
    "Saving accounts": [encoders["Saving accounts"].transform([saving_account_norm])[0]],
    "Checking account": [encoders["Checking account"].transform([checking_account_norm])[0]],
    "Credit amount": [credit_amount],
    "Duration": [duration]
})

if st.button("Predict Risk"):
    pred = model.predict(input_df)[0]
    if pred == 1:
        st.success("The predicted risk is : GOOD")
    else:
        st.error("The predicted credit risk is : BAD")
