import re
import streamlit as st

# Page Config (unchanged)
st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Original CSS (unchanged)
st.markdown("""
    <style>
        /* Remove all default padding and margins */
        html, body, .main, .block-container {
            margin: 0 !important;
            padding: 0 !important;
            background-color: #0e1117 !important;
        }
        
        /* Remove header and footer */
        header, footer {
            display: none !important;
        }
        
        /* Remove Streamlit's default containers */
        .stApp, .st-emotion-cache-uf99v8, .st-emotion-cache-1wrcr25 {
            background: transparent !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        
        /* Input field styling */
        .stTextInput>div>div>input {
            background: linear-gradient(90deg, #00c9ff, #92fe9d);
            color: black;
            border-radius: 8px;
            padding: 12px;
            border: 2px solid #4a90e2;
        }
        .stTextInput>label {
            color: white !important;
            font-weight: 600 !important;
        }
        
        /* Button styling */
        .stButton>button {
            background: linear-gradient(90deg, #1e90ff, #20b2aa) !important;
            color: white;
            font-weight: 600 !important;
            border: none !important;
            padding: 12px;
            border-radius: 8px;
            width: 50%;
            font-size: 1rem;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease-in-out;
        }
         
        .stButton>button:hover {
            transform: scale(1.02);
        }
        
        /* Password strength bar */
        .password-strength-bar {
            height: 10px;
            border-radius: 6px;
            margin: 1rem 0;
            transition: all 0.3s ease;
        }
        
        /* Text colors */
        h1, h2, h3, h4, h5, h6 {
            color: white !important;
        }
        .stMarkdown p {
            color: rgba(255, 255, 255, 0.85) !important;
        }
        
        /* Remove extra spacing around elements */
        .st-emotion-cache-1kyxreq, .st-emotion-cache-1n76uvr {
            padding: 0 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Main content with glass container
with st.container():
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    
    # App title and description
    st.markdown("""
        <h1 style="margin-bottom: 0.5rem;">🔐 Password Strength Meter</h1>
        <p style="margin-bottom: 1.5rem;">Enter your password below to check its security level. 🔍</p>
    """, unsafe_allow_html=True)

    # Password strength function (unchanged)
    def check_password_strength(password):
        score = 0
        feedback = []

        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ Use at least **8 characters** (12+ recommended).")

        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
        else:
            feedback.append("❌ Use **both uppercase and lowercase letters**.")

        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append("❌ Add **numbers** (0-9).")

        if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password):
            score += 1
        else:
            feedback.append("❌ Add **special characters** (!, @, #, etc).")

        score = max(0, min(score, 4))

        strength_labels = ["🔴 Very Weak", "🟠 Weak", "🟡 Moderate", "🟢 Strong", "💪 Very Strong"]
        strength_colors = ["#ff4d4d", "#ffa94d", "#ffd43b", "#51cf66", "#2f9e44"]

        st.markdown(
            f'<div class="password-strength-bar" style="background: linear-gradient(to right, {strength_colors[score]} {(score/4)*100}%, rgba(255,255,255,0.1) {(score/4)*100}%);"></div>',
            unsafe_allow_html=True
        )
        st.markdown(f"**Password Strength:** {strength_labels[score]}")
        
        if score >= 3:
            st.success("✅ Your password is secure.")
            if score == 4:
                st.balloons()
        else:
            st.error("⚠️ Your password is weak.")
        
        if feedback:
            with st.expander("📌 Suggestions to improve"):
                for point in feedback:
                    st.markdown(point)

    password = st.text_input("Enter your password", type="password", help="Ensure your password is strong 🔐", key="pwd_input")

    # Button to Check Password Strength
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Check Strength", key="check_btn"):
            if password:
                check_password_strength(password)
            else:
                st.warning("⚠️ Please enter a password first!")

    st.markdown('</div>', unsafe_allow_html=True)