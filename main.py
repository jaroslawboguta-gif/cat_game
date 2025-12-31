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

# 3. The Interaction
if st.button("KISS THE CAT"):
    # Play sound if it exists
    if os.path.exists(SOUND_PATH):
        with open(SOUND_PATH, 'rb') as f:
            st.audio(f.read(), format='audio/mp3', autoplay=True)
    
    # 🎈 The Balloon effect
    st.balloons()
    
    # 💋 The Kiss Emoji Animation
    placeholder = st.empty()
    kisses = ""
    for _ in range(7):
        kisses += "💋 "
        placeholder.subheader(kisses)
        time.sleep(0.1) # This creates the "popping" delay
        
    st.success("The cat feels loved!")
