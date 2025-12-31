import streamlit as st
import os
import time

# 1. Setup paths to look in the same folder as this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Note: removed "static" from both paths below
CAT_PATH = os.path.join(BASE_DIR, "cat.jpg")
SOUND_PATH = os.path.join(BASE_DIR, "kiss.mp3")

st.title("Cat Kisser 💋")

# 2. Display the Cat
if os.path.exists(CAT_PATH):
    st.image(CAT_PATH, caption="The lonely cat", width='stretch')
else:
    st.error(f"Could not find cat.jpg at {CAT_PATH}. Check your GitHub files!")

# 3. The Interaction
if st.button("KISS THE CAT"):
    if os.path.exists(SOUND_PATH):
        with open(SOUND_PATH, 'rb') as f:
            st.audio(f.read(), format='audio/mp3', autoplay=True)
    
    st.balloons()
    st.success("The cat feels loved!")
