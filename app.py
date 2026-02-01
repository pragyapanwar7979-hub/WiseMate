import streamlit as st
import random
import time

# =================================
# PAGE CONFIG
# =================================
st.set_page_config(page_title="WiseMate 🌿", layout="centered")

NAME = "Pragya Panwar"

# =================================
# THEME COLORS
# =================================
if "dark" not in st.session_state:
    st.session_state.dark = False

# =================================
# SIDEBAR
# =================================
st.sidebar.title("⚙️ WiseMate Tools")

st.session_state.dark = st.sidebar.toggle("🌙 Dark Mode")

mood = st.sidebar.selectbox(
    "😊 Your mood today",
    ["Happy", "Okay", "Tired", "Stressed"]
)

# ================= TIMER =================
st.sidebar.markdown("### ⏱️ Study Timer")

minutes = st.sidebar.slider("Minutes", 1, 60, 25)

if st.sidebar.button("Start Timer"):
    with st.sidebar:
        for i in range(minutes * 60, 0, -1):
            mins = i // 60
            secs = i % 60
            st.write(f"⏳ {mins:02d}:{secs:02d}")
            time.sleep(1)
        st.success("🎉 Time up! Take a break!")

# ================= TIPS =================
tips = [
    "Drink water 💧",
    "Stretch your body 🧘",
    "Revise before sleep 📚",
    "Avoid phone while studying 📵",
    "Short walks boost memory 🚶",
]

st.sidebar.info(random.choice(tips))

# =================================
# STYLING
# =================================
bg = "#0f172a" if st.session_state.dark else "#ffffff"
text = "white" if st.session_state.dark else "black"
user_color = "#6366f1"
bot_color = "#9333ea"

st.markdown(f"""
<style>
.stApp {{
    background-color:{bg};
    color:{text};
}}

.user {{
background:{user_color};
color:white;
padding:10px 14px;
border-radius:18px;
margin:6px;
margin-left:auto;
width:fit-content;
}}

.bot {{
background:{bot_color};
color:white;
padding:10px 14px;
border-radius:18px;
margin:6px;
width:fit-content;
}}

.footer {{
text-align:center;
margin-top:30px;
opacity:0.6;
}}
</style>
""", unsafe_allow_html=True)

# =================================
# HEADER
# =================================
st.title("🌿 WiseMate")
st.write("Your personal study & lifestyle buddy")

# =================================
# CHAT MEMORY
# =================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# =================================
# SMART OFFLINE AI
# =================================
def ai_reply(msg):
    msg = msg.lower()

    greetings = [
        "Heyy 😊 How's your day going?",
        "Hi! Ready to study today?",
        "Hello! Need help with something?"
    ]

    stress = [
        "Take a deep breath 🌿 One step at a time.",
        "You’ve handled tougher days. You got this 💪"
    ]

    study = [
        "Try Pomodoro: 25 min focus + 5 min break 📚",
        "Make short notes while studying. Helps memory!"
    ]

    jokes = [
        "Why did the math book look sad? Too many problems 😂",
        "I told my brain to focus… it opened Instagram 🤦‍♂️"
    ]

    water = [
        "Quick reminder — drink some water 💧",
        "Hydration check! Go sip water 😄"
    ]

    thanks = ["Always here for you 😊", "Happy to help 💜"]

    smalltalk = [
        "Nice! Tell me more ✨",
        "Sounds interesting 👀",
        "I'm listening 👂"
    ]

    if any(w in msg for w in ["hi", "hello", "hey"]):
        return random.choice(greetings)

    elif "stress" in msg or "anxious" in msg:
        return random.choice(stress)

    elif "study" in msg or "exam" in msg:
        return random.choice(study)

    elif "joke" in msg:
        return random.choice(jokes)

    elif "water" in msg:
        return random.choice(water)

    elif "thanks" in msg:
        return random.choice(thanks)

    else:
        return random.choice(smalltalk)
# =================================
# CHAT DISPLAY
# =================================
for role, text in st.session_state.messages:
    if role == "user":
        st.markdown(f"<div class='user'>{text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot'>{text}</div>", unsafe_allow_html=True)

user_input = st.chat_input("Type a message...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    reply = ai_reply(user_input)
    st.session_state.messages.append(("bot", reply))
    st.rerun()

# =================================
# FOOTER (ONLY NAME)
# =================================
st.markdown(f"<div class='footer'>{NAME}</div>", unsafe_allow_html=True)