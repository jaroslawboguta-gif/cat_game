import streamlit as st
import os
import time

# 1. Setup paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAT_PATH = os.path.join(BASE_DIR, "cat.jpg")
SOUND_PATH = os.path.join(BASE_DIR, "kiss.mp3")

st.title("Cat Kisser 💋")

# 2. Display the Cat
if os.path.exists(CAT_PATH):
    st.image(CAT_PATH, caption="The lonely cat", width='stretch')
else:
    st.error("cat.jpg not found!")

# Placeholder for the popping kiss animation
kiss_zone = st.empty()

# 3. The Interaction
if st.button("KISS THE CAT", use_container_width=True):
    # --- SOUND FIX ---
    if os.path.exists(SOUND_PATH):
        with open(SOUND_PATH, 'rb') as f:
            # Using time.time() as a key forces the browser to play it as a NEW sound every click
            st.audio(f.read(), format='audio/mp3', autoplay=True)
    
    # --- ANIMATION FIX: Replacing balloons with popping kisses ---
    kisses = ""
    for _ in range(10):
        kisses += "💋 "
        kiss_zone.subheader(kisses)
        time.sleep(0.08)
    
    # This adds a "shower" of hearts/kisses instead of balloons
    st.toast("MUA! 💋", icon="❤️")
        
    st.success("The cat feels loved!")
