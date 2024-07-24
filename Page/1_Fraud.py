import streamlit as st
import joblib
import numpy as np

def check_url(input_string):
    urls_to_check = ["www.amazon.com", "www.flipkart.com", "www.myntra.com", "www.ajio.com"]
    for url in urls_to_check:
        if url in input_string:
            return 1
    return 0

st.title("Fraud Detector")
url = st.text_input("Enter URL")
check = check_url(url)
if check==1:
    st.title("May Not be Fraud")

elif check==0:
    st.title("Fraud")


if check == 1:
    model = joblib.load('model.joblib')
    # [type,amount,oldbalance,newbalance]


    type = st.selectbox("Select Payment Method",('PAYMENT','TRANSFER','DEBIT','CASH_OUT','CASH_IN')) #2,4,1,5
    if type=='PAYMENT':
        type = 2
    elif type=='CASH_OUT':
        type = 1
    elif type=='TRANSFER':
        type = 4
    elif type=='CASH_IN':
        type = 3
    else :
        type = 5

    amount = st.number_input("Insert Amount Available Your Credit Card")
    oldbalance = amount
    purchase_price = st.number_input("Purchase Price")
    newbalance = oldbalance-purchase_price
    x = np.array([[type, amount, oldbalance, newbalance]])
    if st.button("Predict"):
        pri = model.predict(x)
        st.title(pri)
    else :
        pass
