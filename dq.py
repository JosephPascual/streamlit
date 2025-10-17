import streamlit as st

st.sidebar.title("Navigation")

page = st.sidebar.selectbox('Choose a section', ['About Us', 'FAQs', 'Submit Feedback'])

if page == 'About Us':
    st.header('About Us')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('https://s3-us-east-2.amazonaws.com/dq-authoring-tmp-data/901-1114/Elizabeth_Bennet.png')
        st.header('Elizabeth Bennet')
        st.write('Founder and CEO, Elizabeth is passionate about bringing customers flavorful and delicious coffee.')
    
    with col2:
        st.image('https://s3-us-east-2.amazonaws.com/dq-authoring-tmp-data/901-1114/Charles_Bingley.png')
        st.header('Charles Bingley')
        st.write('Marketing Director and Social Media Expert, Charles helps the world know about our great new flavors!')
    
    with col3:
        st.image('https://s3-us-east-2.amazonaws.com/dq-authoring-tmp-data/901-1114/Georgiana_Darcy.png')
        st.header('Georgiana Darcy')
        st.write('Georgiana is the creative genius behind the scenes!')

if page == 'FAQs':
        st.header("FAQs")
if page == 'Submit Feedback':
    st.header("Submit Feedback")



