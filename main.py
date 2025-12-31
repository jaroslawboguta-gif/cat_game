import streamlit as st
import os
import time

# 1. Setup paths to look in the same folder as this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CAT_PATH = os.path.join(BASE_DIR, "cat.jpg")
SOUND_PATH = os.path.join(BASE_DIR, "kiss.mp3")

# Page configuration for a better mobile look
st.set_page_config(page_title="Cat Kisser", page_icon="💋")

st.title("Cat Kisser 💋")

# 2. Display the Cat
if os.path.exists(CAT_PATH):
    # 'stretch' ensures it fills the phone screen width
    st.image(CAT_PATH, caption="The lonely cat", width='stretch')
else:
    st.error("Error: 'cat.jpg' not found! Please upload it to GitHub.")

# 3. The Interaction
if st.button("KISS THE CAT", use_container_width=True):
    # Handle Sound
    if os.path.exists(SOUND_PATH):
        with open(SOUND_PATH, 'rb') as f:
            st.audio(f.read(), format='audio/mp3', autoplay=True)
    else:
        st.warning("Sound file 'kiss.mp3' not found, but sending love anyway!")

    # Fun Visual Effects
    st.balloons()
    
    # Create a small "popping" animation with emojis
    placeholder = st.empty()
    hearts = ""
    for _ in range(5):
        hearts += "❤️ "
        placeholder.subheader(hearts)
        time.sleep(0.1)
        
    st.success("The cat feels loved!")
