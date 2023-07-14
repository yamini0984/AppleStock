import streamlit as st
import pickle

# Set the page configuration with the title and background image
st.set_page_config(
    page_title="Apple Stock Price Prediction",
    image:"apple1images.jpg",
    layout="wide",
    initial_sidebar_state="expanded"
)
emamodel=pickle.load(open('./model.pkl','rb'))
startDate=st.date_input("Start Date")
endDate=st.date_input("End Date")
if st.button("predict"):
    prediction=emamodel.predict(startDate,endDate)
    st.line_chart(prediction)

