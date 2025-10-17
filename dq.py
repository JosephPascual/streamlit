import streamlit as st

st.sidebar.title("Navigation")

page = st.sidebar.selectbox('Choose a section', ['About Us', 'FAQs', 'Submit Feedback'])

if page == 'About Us':
    st.header('About Us')
    # Add your columns here
    col1, col2, col3 = st.columns(3)
    col1.image("https://s3.amazonaws.com/dq-content/901/Charles_Bingley.png")
    col1.header("Charles Bingley")
    col2.image("https://s3.amazonaws.com/dq-content/901/Elizabeth_Bennet.png")
    col2.header('Elizabeth Bennet')
    col3.image("https://s3.amazonaws.com/dq-content/901/Georgiana_Darcy.png")
    col3.header('Georgiana_Darcy.png')
    st.write('test')
if page == 'FAQs':
    st.header("FAQs")
if page == 'Submit Feedback':
    st.header("Submit Feedback")



