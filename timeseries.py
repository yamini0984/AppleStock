import streamlit as st
import pickle
emamodel=pickle.load(open('./model.pkl','rb'))
startDate=st.date_input("Start Date")
endDate=st.date_input("End Date")
if st.button("predict"):
    prediction=emamodel.predict(startDate,endDate)
    st.line_chart(prediction)

