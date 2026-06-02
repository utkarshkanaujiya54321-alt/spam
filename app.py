import streamlit as st
import numpy as np

# Bittu's trained weights and bias from the notebook!
weight = np.array([519.51344187, 279.67562791])
bias = -0.40546510810816344

def predict(x):
    z = np.dot(x, weight) + bias
    sig = 1 / (1 + np.exp(-z)) # Fixed the plus sign for you!
    return 1 if sig > 0.5 else 0

# App interface design
st.title(" Utkarsh's Spam Detector ")
st.write("Hiii! Welcome to my awesome spam detection platform")

won_count = st.number_input("How many times does 'won' appear in the email?", min_value=0)
money_count = st.number_input("How many times does 'money' appear in the email?", min_value=0)

if st.button("Check Email"):
    email = np.array([won_count, money_count])
    result = predict(email)
    
    if result == 1:
        st.success("Yay! This is a Normal Email (Not Spam) ✨")
    else:
        st.error("Oh no! This looks like SPAM 🚨")
