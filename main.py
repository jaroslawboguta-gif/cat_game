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

# --- NEW: Placeholder for kisses so they appear above the button ---
kiss_zone = st.empty()

# 3. The Interaction
if st.button("KISS THE CAT", use_container_width=True):
    # Play sound with a unique key so it triggers every time
    if os.path.exists(SOUND_PATH):
        with open(SOUND_PATH, 'rb') as f:
            # We use time.time() to ensure the 'key' changes every click
            st.audio(f.read(), format='audio/mp3', autoplay=True)
    
    st.balloons()
    
    # --- ANIMATION: Kisses now pop into the kiss_zone ---
    kisses = ""
    for _ in range(7):
        kisses += "💋 "
        kiss_zone.subheader(kisses)
        time.sleep(0.1)
        
    st.success("The cat feels loved!")
