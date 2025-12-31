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

# Improved: Reliable background kiss sound using JavaScript
def play_background_kiss():
    if os.path.exists(SOUND_PATH):
        with open(SOUND_PATH, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
        
        audio_js = f"""
        <script>
        // Remove any existing kiss sound to avoid duplicates
        const existing = document.getElementById('kiss-sound');
        if (existing) existing.remove();
        
        // Create and play new audio
        const audio = new Audio("data:audio/mp3;base64,{b64}");
        audio.id = 'kiss-sound';
        audio.play().catch(e => console.log("Audio play blocked or failed:", e));
        </script>
        """
        st.markdown(audio_js, unsafe_allow_html=True)

# 2. Display the Cat
if os.path.exists(CAT_PATH):
    st.image(CAT_PATH, caption="The lonely cat awaits your love 😿", use_container_width=True)
else:
    st.error("cat.jpg not found! Please place it in the same folder as this script.")

# Placeholder for the exploding kiss animation
kiss_zone = st.empty()

# 3. The Interaction
if st.button("KISS THE CAT 💋", use_container_width=True):
    # Play the kiss sound reliably
    play_background_kiss()
    
    # --- INTENSE KISS EXPLOSION ANIMATION ---
    all_kisses = ""
    emojis = ["💋", "❤️", "💖", "💕", "😘", "🩷", "💗"]
    
    kiss_zone.empty()  # Clear any previous kisses
    
    for i in range(25):  # Increased for more chaos!
        all_kisses += random.choice(emojis) + " "
        # Bigger and more dramatic text
        kiss_zone.markdown(
            f"<h1 style='text-align: center; font-size: {60 + i}px; line-height: 1.2;'>"
            f"{all_kisses}</h1>",
            unsafe_allow_html=True
        )
        time.sleep(0.05)  # Slightly slower for dramatic buildup, adjust as needed
    
    # Brief pause to let the final explosion sit
    time.sleep(0.8)
    
    # Clear the explosion
    kiss_zone.empty()
    
    # Victory message
    st.success("MUAHHHHH! The cat is absolutely smothered in kisses! 😻❤️💋")
    st.balloons()  # Extra celebration!
