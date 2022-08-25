import streamlit as st
from array import array
import numpy as np
import pickle
import sklearn




st.title("Online Payment Fraud Prediction")
st.image("Ub21142758_g.jpg")
step=st.slider("Time of transaction(1 step = 1 hour)",1,95)
amount=st.number_input(label="Amount of transaction",min_value=0,max_value=10000000)
oldbalanceorg=st.number_input(label="Balance before the transaction",min_value=0,max_value=4000000)
newbalanceorg=st.number_input(label="Balance after the transaction",min_value=0,max_value=4000000)
oldbalancedest=st.number_input(label="Initial balance of recipient before the transaction",min_value=0,max_value=4500000)
newbalancedest=st.number_input(label="New balance of recipient after the transaction",min_value=0,max_value=4500000)

type_display=("CASH_IN","CASH_OUT","DEBIT","PAYMENT","TRANSFER")
type_options=list(range(len(type_display)))
type=st.radio("Type of transaction",type_options,format_func=lambda x:type_display[x])



inputs = np.array([[step,type,amount,oldbalanceorg,newbalanceorg,oldbalancedest,newbalancedest]])

with open("model.pkl","rb") as f:
    model = pickle.load(f)

prediction = model.predict(inputs)

st.button("predict")
if prediction == 1:
    st.write("Your transaction is fraud")
else:
    st.write("You transaction is not fraud")
    










