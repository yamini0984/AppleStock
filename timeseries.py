import streamlit as st
import pickle

# Set the page configuration with the title and background image
html_temp="""
<div style ="background-color:grey;padding:10px">
<h2 style="color:white;text-align:center;">Apple Stock Price Prediction </h2>
"""
st.markdown(html_temp,unsafe_allow_html=True)

def center_image(image_path):
    st.markdown(
        f'<div style="display: flex; justify-content: center;"><img src="{image_path}" width="100; max-height: 100%;"/></div>',
        unsafe_allow_html=True
    )
    
# Usage
center_image('apple1images.jpg')
image = Image.open("apple1images.jpg")
st.image(image)

emamodel=pickle.load(open('./model.pkl','rb'))
startDate=st.date_input("Start Date")
endDate=st.date_input("End Date")
if st.button("predict"):
    prediction=emamodel.predict(startDate,endDate)
    st.line_chart(prediction)

