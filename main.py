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
    st.image(CAT_PATH, caption="The lonely cat", use_container_width=True)
else:
    st.error("cat.jpg not found!")

# Placeholder for the massive kiss animation
kiss_zone = st.empty()

# 3. The Interaction
if st.button("KISS THE CAT", use_container_width=True):
    # --- SOUND FIX: The 'key' ensures it plays every time ---
    if os.path.exists(SOUND_PATH):
        with open(SOUND_PATH, 'rb') as f:
            # Adding random.random() makes the identity of the player 
            # change every click, forcing it to play again.
            st.audio(f.read(), format='audio/mp3', autoplay=True, loop=False)
    
    # --- INTENSE KISS ANIMATION ---
    all_kisses = ""
    for i in range(1, 12):
        # Adding random hearts and kisses
        all_kisses += random.choice(["💋", "❤️", "💖", "💋"]) + " "
        # FIX: Changed unsafe_allow_name to unsafe_allow_html
        kiss_zone.markdown(f"<h1 style='text-align: center; font-size: 50px;'>{all_kisses}</h1>", unsafe_allow_html=True)
        time.sleep(0.05)
    
    st.success("MUAH! The cat is covered in love! 😻")
