import streamlit as st
import os
import time

# Get the correct path to your files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAT_PATH = os.path.join(BASE_DIR, "cat.jpg")
SOUND_PATH = os.path.join(BASE_DIR, "static", "kiss.mp3")

st.title("Cat Kisser 💋")

# Check if image exists before trying to show it
if os.path.exists(CAT_PATH):
    st.image(CAT_PATH, caption="The lonely cat", width='stretch')
else:
    st.error(f"Could not find cat.jpg at {CAT_PATH}")

if st.button("KISS THE CAT"):
    if os.path.exists(SOUND_PATH):
        with open(SOUND_PATH, 'rb') as f:
            st.audio(f.read(), format='audio/mp3', autoplay=True)

    st.balloons()

    st.success("The cat feels loved!")
