import streamlit as st
from array import array
import numpy as np
import sklearn
import pickle


st.title("Online Payment Fraud Prediction")
st.image("Ub21142758_g.jpg")
st.write("PaySim simulates mobile money transactions based on a sample of real transactions extracted from one month of financial logs from a mobile money service implemented in an African country. ")
type_display=("CASH_IN","CASH_OUT","DEBIT","PAYMENT","TRANSFER")
type_options=list(range(len(type_display)))
type=st.radio("Type of transaction",type_options,format_func=lambda x:type_display[x])
amount=st.number_input(label="Amount of transaction",max_value=10000000)
oldbalanceorg=st.number_input(label="Balance before the transaction",max_value=3250000)
newbalanceorg=st.number_input(label="Balance after the transaction",max_value=3250000)
inputs = np.array([[type,amount,oldbalanceorg,newbalanceorg]])

with open("modellr.pkl","rb") as f:
    model = pickle.load(f)

prediction = model.predict(inputs)

if st.button("Predict"):
    if prediction == 1:
       st.markdown("Your transaction is fraud")
    else:
       st.markdown("Your transaction is not fraud")
       st.balloons()
st.caption("by akshata pednekar")









































