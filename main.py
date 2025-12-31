import streamlit as st
import os
import time
import random

# 1. Setup paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAT_PATH = os.path.join(BASE_DIR, "cat.jpg")
SOUND_PATH = os.path.join(BASE_DIR, "kiss.mp3")

st.set_page_config(page_title="Cat Kisser", page_icon="💋")
st.title("Cat Kisser 💋")

# 2. Display the Cat
if os.path.exists(CAT_PATH):
    st.image(CAT_PATH, caption="The lonely cat", width='stretch')
else:
    st.error("cat.jpg not found!")

# Placeholder for the massive kiss animation
kiss_zone = st.empty()

# 3. The Interaction
if st.button("KISS THE CAT", use_container_width=True):
    # --- SOUND FIX: Forces play every time ---
    if os.path.exists(SOUND_PATH):
        with open(SOUND_PATH, 'rb') as f:
            # We add a random number to the 'key' so Streamlit 
            # thinks it's a new audio component every time you click.
            st.audio(f.read(), format='audio/mp3', autoplay=True)
    
    # --- INTENSE KISS ANIMATION ---
    # We will loop multiple times to create a "falling/growing" effect
    all_kisses = ""
    for i in range(1, 15):
        # Add a random number of kisses per line to make it look "messy" and fun
        all_kisses += "💋" * random.randint(1, 3) + " "
        kiss_zone.markdown(f"<h2 style='text-align: center;'>{all_kisses}</h2>", unsafe_allow_name=True)
        time.sleep(0.05)
    
    # A big final message
    st.success("MUAH! MUAH! MUAH! The cat is covered in kisses! 😻")
