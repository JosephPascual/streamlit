import streamlit as st

st.sidebar.title("Navigation")

page = st.sidebar.selectbox('Choose a section', ['About Us', 'FAQs', 'Submit Feedback'])

if page == 'About Us':
    st.header("About Us")
if page == 'FAQs':
    st.header("FAQs")
if page == 'Submit Feedback':
    st.header("Submit Feedback")
