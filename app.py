# =========================================================
# WiseMate – AI Student Lifestyle & Productivity Assistant
# Single-file Streamlit Web App
# Made by Pragya Panwar
# =========================================================

import streamlit as st
import random
import time

# =========================
# Page Setup
# =========================
st.set_page_config(page_title="WiseMate 🌿", layout="centered")

# =========================
# Sidebar Controls
# =========================
st.sidebar.title("⚙️ WiseMate Tools")

dark_mode = st.sidebar.checkbox("🌙 Dark Mode")
name = "Pragya Panwar"

mood = st.sidebar.selectbox(
    "😊 Mood today?",
    ["Happy", "Okay", "Tired", "Stressed"]
)

# Daily Tips
tips = [
    "💡 Study 25 mins then take 5 mins break",
    "💧 Drink more water today",
    "🌙 Sleep 7–8 hours for better focus",
    "📵 Keep phone away while studying",
    "🚶 Take small walks to refresh your mind",
    "📝 Plan tomorrow tonight"
]
st.sidebar.markdown("### 🌟 Daily Tip")
st.sidebar.info(random.choice(tips))

# =========================
# Study Timer (Non-blocking)
# =========================
st.sidebar.markdown("---")
st.sidebar.subheader("⏳ Study Timer")

minutes = st.sidebar.number_input("Minutes", 1, 120, 25)
if "timer_end" not in st.session_state:
    st.session_state.timer_end = 0

if st.sidebar.button("Start Timer"):
    st.session_state.timer_end = time.time() + minutes * 60

if st.session_state.timer_end > time.time():
    remaining = int(st.session_state.timer_end - time.time())
    m, s = divmod(remaining, 60)
    st.sidebar.info(f"⏳ {m:02d}:{s:02d} remaining")
else:
    if st.session_state.timer_end != 0:
        st.sidebar.success("Time's up! 🎉 Take a break")

# =========================
# Styling (Pastel + Dark)
# =========================
bg = "#0f172a" if dark_mode else "#f6f7fb"
card = "#1e293b" if dark_mode else "white"
text = "white" if dark_mode else "black"

st.markdown(f"""
<style>
.stApp {{
    background:{bg};
    color:{text};
}}
.title {{
    text-align:center;
    font-size:38px;
    font-weight:bold;
    color:#6c63ff;
}}
.subtitle {{
    text-align:center;
    margin-bottom:20px;
}}
.chatbox {{
    background:{card};
    padding:20px;
    border-radius:20px;
    box-shadow:0px 4px 18px rgba(0,0,0,0.12);
}}
.user {{
    background:#c7d2fe;
    padding:12px 16px;
    border-radius:18px 18px 4px 18px;
    margin:8px 0;
    margin-left:auto;
    width:fit-content;
    max-width:75%;
}}
.bot {{
    background:#e9d5ff;
    padding:12px 16px;
    border-radius:18px 18px 18px 4px;
    margin:8px 0;
    width:fit-content;
    max-width:75%;
}}
.footer {{
    text-align:center;
    font-size:12px;
    margin-top:20px;
    color:gray;
}}
</style>
""", unsafe_allow_html=True)

# =========================
# Header + Intro
# =========================
st.markdown("<div class='title'>🌿 WiseMate</div>", unsafe_allow_html=True)
st.markdown(f"""
<div class='subtitle'>
Hi {name}! I’m <b>WiseMate</b>, your personal student lifestyle and productivity assistant.  
I help you manage studies, stress, routines, sleep, and motivation — so you can grow calmly and confidently every day.
</div>
""", unsafe_allow_html=True)

# =========================
# Chat Memory
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# Chat Response Logic
# =========================
def bot_reply(message):
    msg = message.lower()

    # Greetings
    greetings = ["hi", "hello", "hey", "good morning", "good evening"]
    if any(g in msg for g in greetings):
        return random.choice([
            f"Hello {name}! How are you feeling today?",
            f"Hey {name}! Ready to be productive today?",
            "Hi! I'm here to help you focus and relax 🌿"
        ])
# Mood-related responses
    if "tired" in msg or "exhausted" in msg:
        return "Take a short break, drink water, and do some stretching. You’ve got this!"
    if "stressed" in msg or "anxious" in msg:
        return "Breathe slowly for 1 minute and focus on one task at a time. Small steps help."
    if "study" in msg or "focus" in msg:
        return "Try studying in 25-min intervals with 5-min breaks (Pomodoro method)."

    # Jokes & fun
    if "joke" in msg:
        jokes = [
            "Why did the student eat his homework? Because the teacher said it was a piece of cake 😄",
            "Why did the computer go to school? To improve its 'byte' size knowledge 😆"
        ]
        return random.choice(jokes)

    # General fallback
    advice = [
        "💧 Drink water and stay hydrated!",
        "🌙 Sleep well to stay focused.",
        "🚶 Take a short walk to refresh your mind.",
        "📝 Write a small to-do list for clarity.",
        "📵 Keep distractions away while studying."
    ]
    return random.choice(advice)

# =========================
# Chat UI
# =========================
st.markdown("<div class='chatbox'>", unsafe_allow_html=True)
for role, msg in st.session_state.messages:
    cls = "user" if role == "user" else "bot"
    st.markdown(f"<div class='{cls}'>{msg}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# =========================
# Input
# =========================
user_input = st.chat_input("Type your message...")
if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.spinner("WiseMate is typing..."):
        time.sleep(0.5)
        bot = bot_reply(user_input)
    st.session_state.messages.append(("bot", bot))
    st.experimental_rerun()

# =========================
# Download Chat History
# =========================
if st.sidebar.button("💾 Download Chat"):
    text_data = "\n".join([f"{r}: {m}" for r, m in st.session_state.messages])
    st.sidebar.download_button("Download", text_data, "wisemate_chat.txt")

# =========================
# Footer
# =========================
st.markdown("<div class='footer'>Pragya Panwar</div>", unsafe_allow_html=True)