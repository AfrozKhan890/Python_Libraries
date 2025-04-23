import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Growth Mindset Project", 
    page_icon="★",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .header-text {
            color: #4a4a4a;
            text-align: center;
        }
        .quote-box {
            background-color: #e3f2fd;
            border-radius: 10px;
            padding: 15px;
            color:#0D98BA;
            margin: 10px 0;
        }
        .challenge-box {
            background-color: #fff8e1;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            color: #666;
            font-size: 0.9em;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("🌟 Growth Mindset Challenge")
st.markdown("""
    <div class="header-text">
        <h3>Welcome to Your Growth Journey!</h3>
        <p>Embrace challenges, learn from mistakes, and unlock your full potential with this AI-powered app</p>
    </div>
""", unsafe_allow_html=True)

# Quote Section with improved layout
with st.container():
    st.header("💡 Today's Growth Mindset Quote")
    with st.expander("Show/Hide Quote"):
        st.markdown("""
            <div class="quote-box">
                <blockquote>
                    "Success is not final, failure is not fatal: it is the courage to continue that counts."
                </blockquote>
            </div>
        """, unsafe_allow_html=True)

# Challenge Section with date tracking
with st.container():
    st.header("⌛ Daily Challenge Tracker")
    today = datetime.now().strftime("%B %d, %Y")
    st.subheader(f"Today is: {today}")
    
    with st.form("challenge_form"):
        user_input = st.text_area("Describe a challenge you're facing today:", height=100)
        submitted = st.form_submit_button("Submit Challenge")
        
        if submitted:
            if user_input:
                st.success(f"💪 Challenge recorded! Remember: \"{user_input}\". Keep pushing forward! 🚀")
                st.balloons()
            else:
                st.warning("Please describe your challenge to get started!")

# Reflection Section with prompt questions
with st.container():
    st.header("📝 Reflection Journal")
    reflection = st.text_area(
        "What did you learn today?\n\nConsider:\n- What went well?\n- What could be improved?\n- What will you do differently tomorrow?",
        height=150
    )
    
    if reflection:
        st.success("🌟 Great insights! Reflection is key to growth.")
        st.write("Your reflection:", reflection)

# Achievement Section with celebration
with st.container():
    st.header("🏆 Achievement Celebrations")
    achievement = st.text_input("Share something you accomplished recently (big or small):")
    
    if achievement:
        st.success(f"🎉 Amazing work on: {achievement}")
        st.image("https://media.giphy.com/media/XreQmk7ETCak0/giphy.gif", width=200)

# Footer
st.markdown("---")
st.markdown("""
    <div class="footer">
        <p>Keep believing in yourself. Growth is a journey, not a destination! ⭐</p>
        <p><strong>Created by Afroz Khan</strong> </p>
    </div>
""", unsafe_allow_html=True)