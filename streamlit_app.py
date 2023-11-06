import streamlit as st
import random

#Run app
#streamlit run "D:\Desktop\PythonApps\StreamlitTest.py"

# Define a list of compliments
complimentFile = open("D:\\Desktop\\compliments.txt", "r")
compliments = complimentFile.readlines()


# Set the background color to light pink and center the content
st.markdown(
    """
    <style>
    body {
        background-color: #ffc0cb;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        flex-direction: column;
    }
    .stButton button {
        font-size: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create the Streamlit app
st.title("I LOVE YOU")

# Create a button to generate compliments
if st.button("PRESS ME"):
    random_compliment = random.choice(compliments)
    st.write(f"{random_compliment}")

# Run the app with 'streamlit run app.py' in your terminal
