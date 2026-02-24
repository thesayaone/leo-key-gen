import streamlit as st
import datetime
import random
import string
import time

# --- ब्रांडिंग और सेटअप ---
st.set_page_config(page_title="Leo Algo Security", page_icon="🦁")

# मास्टर पासवर्ड
MASTER_PASSWORD = "28052025" 

def generate_leo_key(days_to_add):
    """15-character key logic [cite: 2026-02-24]"""
    expiry_date = datetime.datetime.now() + datetime.timedelta(days=days_to_add)
    prefix = "LeO06" # [cite: 2026-02-04]
    
    # MM, YY, DD extraction [cite: 2026-02-24]
    mm = expiry_date.strftime("%m")
    yy = expiry_date.strftime("%y")
    dd = expiry_date.strftime("%d")
    
    # रैंडम फिलर्स ताकि लंबाई 15 हो जाए [cite: 2026-02-24]
    f1 = ''.join(random.choices(string.digits, k=2))
    f2 = ''.join(random.choices(string.digits, k=2))
    
    # फाइनल फॉर्मेट [cite: 2026-02-24]
    return f"{prefix}{mm}{f1}{yy}{f2}{dd}", expiry_date.strftime('%d-%m-%Y')

# --- लॉगिन सिस्टम ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("🦁 Leo Algo Security Login")
    # पासवर्ड इनपुट [cite: 2026-02-21]
    pwd = st.text_input("मास्टर पासवर्ड डालें", type="password")
    if st.button("Login"):
        if pwd == MASTER_PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("गलत पासवर्ड! एक्सेस नहीं मिला।")
else:
    # --- मेन इंटरफेस ---
    st.title("🦁 Leo Algo & Indicators")
    st.write("सुरक्षित एक्सेस की (Access Key) जनरेट करें।")

    option = st.selectbox("वैलिडिटी चुनें", ["1 DAY", "1 WEEK", "1 MONTH", "3 MONTHS"])
    
    days_map = {"1 DAY": 1, "1 WEEK": 7, "1 MONTH": 30, "3 MONTHS": 90}

    if st.button("Generate Key"):
        # लोडिंग एनीमेशन [cite: 2026-02-21]
        with st.spinner('डेटाबेस से कनेक्ट हो रहा है...'):
            time.sleep(1.5)
        
        key, exp_date = generate_leo_key(days_map[option])
        
        st.success(f"{option} के लिए की (Key) तैयार है!")
        # की दिखाने के लिए बॉक्स
        st.code(key, language="text")
        st.info(f"एक्सपायरी डेट: {exp_date}")
        
    if st.button("Logout (Wipe Data)"):
        st.session_state.authenticated = False
        st.rerun()
