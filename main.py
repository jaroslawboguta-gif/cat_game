import streamlit as st
import os
import time
import random
import base64

# 1. Setup paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAT_PATH = os.path.join(BASE_DIR, "cat.jpg")
SOUND_PATH = os.path.join(BASE_DIR, "kiss.mp3")

st.set_page_config(page_title="Cat Kisser", page_icon="💋")
st.title("Cat Kisser 💋")

# Function to play sound in the background without a visible bar
def play_background_kiss():
    if os.path.exists(SOUND_PATH):
        with open(SOUND_PATH, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            # This hidden HTML snippet plays the sound and then removes itself
            md = f"""
                <audio autoplay>
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(md, unsafe_allow_html=True)

# 2. Display the Cat
if os.path.exists(CAT_PATH):
    st.image(CAT_PATH, caption="The lonely cat", use_container_width=True)
else:
    st.error("cat.jpg not found!")

# Placeholder for the massive kiss animation
kiss_zone = st.empty()

# 3. The Interaction
if st.button("KISS THE CAT", use_container_width=True):
    # --- SOUND FIX: Hidden background play ---
    play_background_kiss()
    
    # --- INTENSE KISS ANIMATION ---
    all_kisses = ""
    # More kisses (increased to 20 for a bigger explosion)
    for i in range(1, 20):
        all_kisses += random.choice(["💋", "❤️", "💖", "💋", "💕"]) + " "
        # We display them in the kiss_zone
        kiss_zone.markdown(f"<h1 style='text-align: center; font-size: 55px;'>{all_kisses}</h1>", unsafe_allow_html=True)
        time.sleep(0.04) # Faster pop for better feel
    
    st.success("MUAH! The cat is covered in love! 😻")
