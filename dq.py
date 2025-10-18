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

def general_faqs():
    st.header("FAQs")
    bean_source_expander = st.expander("Where do you source your coffee beans?")
    with bean_source_expander:
        st.write('Our coffee beans are ethically sourced from family-owned farms and cooperatives across various coffee-growing regions, ensuring quality and sustainability in every cup.')
    roast_expander = st.expander('How do you roast your beans?')
    with roast_expander:
        st.write("We employ a combination of traditional and modern roasting techniques, meticulously adjusting the roast profile for each batch to bring out the unique flavors and aromas of the beans.")

def recipe_faqs():
    recommended = st.expander('What is your recommended recipe for a classic cold brew coffee?', )
    with recommended:
        st.write('For a smooth and robust cold brew, mix coarsely ground coffee beans with cold water in a 1:8 ratio, steep for 12-18 hours, and then filter. Serve over ice and customize with milk or sweeteners to taste.')
    signature = st.expander('Do you have a signature coffee-based dessert recipe?')
    with signature:
        st.write('Yes, our signature dessert is the \'GlobalJava Mocha Brownies.\' Blend melted dark chocolate with your favorite GlobalJava espresso shot, add to your brownie mix, and bake. These rich, coffee-infused brownies are a coffee lover\'s delight and perfect for any occasion.')

if page == 'FAQs':
    st.header('FAQs')
    tab1, tab2 = st.tabs(['General', 'Recipes'])
    with tab1:
        general_faqs()    
    with tab2:
        recipe_faqs()

if page == 'Submit Feedback':
    st.header('Submit Feedback')
    st.write("Did you enjoy your coffee?")
    yes_button_clicked = st.button("Yes!")
    no_button_clicked = st.button("No!")

    if yes_button_clicked:
        st.write("Glad you enjoyed it!")
    elif no_button_clicked:
        st.write("We're sorry to hear that. We'll strive to improve.")

    coffee_rating = st.slider("On a scale of 1 to 10, how would you rate our coffee today?", 1, 10, 5)

    service_type = st.selectbox("What type of service did you experience?", ["In-store", "Online", "Phone"])

    st.write(f"You rated our coffee a {coffee_rating} and experienced {service_type} service.")

    st.write("We value your feedback. Please tell us more about your experience.")
    name = st.text_input("Name")
    message = st.text_area("Feedback")
    st.write(f"Thank you {name} for your feedback: {message}")



