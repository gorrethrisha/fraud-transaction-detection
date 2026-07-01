import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("fraud_detection_model.pkl")

# Title
st.title("Fraud Transaction Detection")
st.write("Enter transaction details below to detect whether the transaction is fraudulent or legitimate.")

# User Inputs
customer_id = st.number_input("Customer ID",min_value=0,max_value=4999,value=1000)

terminal_id = st.number_input("Terminal ID",min_value=0,max_value=9999,value=1000)

tx_amount = st.number_input("Transaction Amount",min_value=0.0,max_value=2628.0,value=100.0)

tx_time_seconds = st.number_input("Transaction Time (Seconds)",min_value=31,max_value=15811197,value=100000)

tx_time_days = st.number_input("Transaction Time (Days)",min_value=0,max_value=182,value=30)

# Prediction Button
if st.button("Detect Fraud"):

    input_data = pd.DataFrame({
        "CUSTOMER_ID": [customer_id],
        "TERMINAL_ID": [terminal_id],
        "TX_AMOUNT": [tx_amount],
        "TX_TIME_SECONDS": [tx_time_seconds],
        "TX_TIME_DAYS": [tx_time_days]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")