import streamlit as st

st.sidebar.title("Navigation")

page = st.sidebar.selectbox('Choose a section', ['About Us', 'FAQs', 'Submit Feedback'])

if page == 'About Us':
    st.header('About Us')
    # Add your columns here
    col1, col2, col3 = st.columns(3)
    col1.image("https://s3.amazonaws.com/dq-content/901/Charles_Bingley.png")
    col1.st.header("Charles Bingley")
    col2.image("https://s3.amazonaws.com/dq-content/901/Elizabeth_Bennet.png")
    col2.st.header('Elizabeth Bennet')
    col3.image("https://s3.amazonaws.com/dq-content/901/Georgiana_Darcy.png")
    col3.st.header('Georgiana_Darcy.png')
if page == 'FAQs':
    st.header("FAQs")
if page == 'Submit Feedback':
    st.header("Submit Feedback")

