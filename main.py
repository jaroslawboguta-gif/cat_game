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

# Most reliable method: Hidden <audio autoplay> tag (no controls, plays instantly)
def play_background_kiss():
    if os.path.exists(SOUND_PATH):
        with open(SOUND_PATH, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
        
        audio_html = f"""
        <audio autoplay="true" id="kiss-sound">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        <script>
            // Optional: Remove the audio element after it finishes playing to clean up
            const audio = document.getElementById('kiss-sound');
            audio.onended = () => audio.remove();
        </script>
        """
        st.markdown(audio_html, unsafe_allow_html=True)

# 2. Display the Cat
if os.path.exists(CAT_PATH):
    st.image(CAT_PATH, caption="The lonely cat awaits your love 😿", use_container_width=True)
else:
    st.error("cat.jpg not found! Please place it in the same folder as this script.")

# Placeholder for the exploding kiss animation
kiss_zone = st.empty()

# 3. The Interaction
if st.button("KISS THE CAT 💋", use_container_width=True):
    # Play the kiss sound (should work reliably now!)
    play_background_kiss()
    
    # --- EPIC KISS EXPLOSION ---
    all_kisses = ""
    emojis = ["💋", "❤️", "💖", "💕", "😘", "🩷", "💗", "🌸"]
    
    kiss_zone.empty()  # Start fresh
    
    for i in range(30):  # Even more kisses for maximum love overload
        all_kisses += random.choice(emojis) + " "
        kiss_zone.markdown(
            f"<h1 style='text-align: center; font-size: {50 + i*2}px; line-height: 1.2;'>"
            f"{all_kisses}</h1>",
            unsafe_allow_html=True
        )
        time.sleep(0.04)  # Fast and furious
    
    # Let the final explosion linger a bit
    time.sleep(0.8)
    
    # Clean up
    kiss_zone.empty()
    
    # Celebration time!
    st.success("MUAHHHHHHH!!! The cat is drowning in kisses! 😻💕💋")
    st.balloons()

st.caption("Tip: Click the button multiple times — the sound should play every single time now! 🐱💨")
