import streamlit as st
import random

#Run app
#streamlit run "D:\Desktop\PythonApps\StreamlitTest.py"

# Define a list of compliments

compliments = [
    "You light up my life.",
    "You have a smile that could brighten the darkest day.",
    "Your laughter is contagious.",
    "You're the sweetest person I know.",
    "You make my heart skip a beat.",
    "You're the apple of my eye.",
    "Your kindness knows no bounds.",
    "You're as sweet as honey.",
    "You have a heart of gold.",
    "You make the world a better place.",
    "You're a breath of fresh air.",
    "You're a true gem.",
    "Your presence is a gift.",
    "You have a heartwarming personality.",
    "You're a ray of sunshine.",
    "You're the embodiment of joy.",
    "You have an aura of positivity.",
    "Your kindness melts my heart.",
    "You're a beautiful soul.",
    "You're an angel in disguise.",
    "You make me believe in magic.",
    "You're the epitome of charm.",
    "Your smile is a work of art.",
    "You have a heart full of love.",
    "You're a bundle of happiness.",
    "You're the source of my happiness.",
    "Your positivity is inspiring.",
    "You're the epitome of grace.",
    "Your love is a beacon of hope.",
    "You're a true ray of light.",
    "You're as lovely as a sunset.",
    "Your presence is a gift to everyone.",
    "You radiate love and kindness.",
    "You make my heart swell with joy.",
    "You're a constant source of inspiration.",
    "You're the definition of beauty.",
    "You have a heart as big as the ocean.",
    "You make every day brighter.",
    "Your positivity is infectious.",
    "You have a magnetic personality.",
    "You're a delight to be around.",
    "Your laughter is music to my ears.",
    "You're a constant source of happiness.",
    "Your presence warms my heart.",
    "You're a true inspiration.",
    "You light up the room.",
    "Your love knows no bounds.",
    "You have a heartwarming soul.",
    "You're a treasure in my life.",
    "You're as delightful as a summer day.",
    "You make every moment special.",
    "Your positivity is contagious.",
    "You're a wonderful human being.",
    "Your love is a treasure.",
    "You're a constant source of inspiration.",
    "You're a beacon of light in my life.",
    "You make the world a better place.",
    "You have a heart full of compassion.",
    "You're an angel on Earth.",
    "Your warmth is truly comforting.",
    "You're a true blessing to me.",
    "Your presence is a gift to everyone you meet."
]

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
