import streamlit as st
import joblib
st.title('Trip_advisor_Hotel_Review-Rating')
test_model = joblib.load('Hotel_Review-Rating')
ip = st.text_input('Enter your review')
op = test_model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
