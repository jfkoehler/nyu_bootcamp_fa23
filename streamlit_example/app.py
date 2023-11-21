import streamlit as st 
import numpy as np
import pickle

st.header('A Model for AHD')

st.write('Please enter the Age, Sex, and Slope information below.')

age = st.number_input('Age')
sex = st.number_input('Sex')
slope = st.number_input('Slope')

X = np.array([[age, sex, slope]])

with open('forestmodel.pkl', 'rb') as f:
    model = pickle.load(f)
    
pred = model.predict(X)

st.write(f'The model predicts {pred[0]}')