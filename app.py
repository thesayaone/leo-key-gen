import streamlit as st
import datetime
import random
import string
import time

# --- HACKER TERMINAL STYLING (CSS) --- [cite: 2026-02-21]
st.markdown("""
    <style>
    .stApp {
        background-color: #000000;
    }
    .terminal-text {
        color: #00FF41;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 5px #00FF41;
    }
    h1, h2, h3, p, label {
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    .stButton>button {
        background-color: #000;
        color: #00FF41;
        border: 2px solid #00FF41;
        border-radius: 5px;
        box-shadow: 0 0 10px #00FF41;
    }
    .stTextInput>div>div>input {
        background-color: #111;
        color: #00FF41;
        border: 1px solid #00FF41;
    }
    </style>
    """, unsafe_allow_html=True)

# Master Password Logic
MASTER_PASSWORD = "28052025" 

def generate_leo_key(days_to_add):
    """
    Implements the 15-character secret logic:
    Prefix (0-4): LeO06 [cite: 2026-02-04]
    Month (5-6), Year (9-10), Day (13-14) [cite: 2026-02-24]
    """
    expiry_date = datetime.datetime.now() + datetime.timedelta(days=days_to_add)
    prefix = "LeO06" [cite: 2026-02-04]
    
    mm = expiry_date.strftime("%m")
    yy = expiry_date.strftime("%y")
    dd = expiry_date.strftime("%d")
    
    # Random Fillers to maintain 15-character length [cite: 2026-02-24]
    f1 = ''.join(random.choices(string.digits, k=2)) # Filler for index 7-8
    f2 = ''.join(random.choices(string.digits, k=2)) # Filler for index 11-12
    
    # Final Structure: LeO06 (5) + MM (2) + F1 (2) + YY (2) + F2 (2) + DD (2) = 15 [cite: 2026-02-24]
    return f"{prefix}{mm}{f1}{yy}{f2}{dd}", expiry_date.strftime('%d-%m-%Y')

# --- AUTHENTICATION LAYER --- [cite: 2026-02-21]
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown('<h1 class="terminal-text">🦁 LEO ALGO - ACCESS RESTRICTED</h1>', unsafe_allow_html=True)
    pwd = st.text_input("ENTER MASTER DECRYPTION KEY", type="password")
    if st.button("AUTHENTICATE"):
        if pwd == MASTER_PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("ACCESS DENIED: INVALID KEY")
else:
    # --- MAIN ENCRYPTION TERMINAL --- [cite: 2026-02-21]
    st.markdown('<h1 class="terminal-text">🦁 LEO ALGO SECURITY TERMINAL</h1>', unsafe_allow_html=True)
    
    option = st.selectbox("SELECT VALIDITY PERIOD", ["1 DAY", "1 WEEK", "1 MONTH", "3 MONTHS"])
    days_map = {"1 DAY": 1, "1 WEEK": 7, "1 MONTH": 30, "3 MONTHS": 90}

    if st.button("EXECUTE KEY GENERATION"):
        terminal_box = st.empty()
        
        # Hacker-style Typing Animation [cite: 2026-02-21]
        logs = [
            "> Initializing Leo Algo Secure Protocol...",
            "> Bypassing AI Protection Headers...",
            "> Injecting Proprietary Date Logic...",
            "> Formatting 15-Character Access Key...",
            "> ENCRYPTION SUCCESSFUL."
        ]
        
        current_log = ""
        for log in logs:
            current_log += log + "\n"
            terminal_box.code(current_log)
            time.sleep(0.4) 
        
        key, exp_date = generate_leo_key(days_map[option]) [cite: 2026-02-24]
        
        st.markdown(f'<p class="terminal-text">ACCESS KEY GENERATED FOR: {option}</p>', unsafe_allow_html=True)
        st.code(key, language="text")
        st.markdown(f'<p class="terminal-text">EXPIRY DATE: {exp_date}</p>', unsafe_allow_html=True)
        
    if st.button("WIPE DATA & LOGOUT"): [cite: 2026-02-21]
        st.session_state.authenticated = False
        st.rerun()
