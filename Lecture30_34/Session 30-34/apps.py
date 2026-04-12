import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# Page configuration - MUST be the first Streamlit command
st.set_page_config(
    page_title="Apna Technology - Complete Suite",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Main container */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Gradient text */
    .gradient-text {
        background: linear-gradient(120deg, #FF6B6B, #4ECDC4, #45B7D1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    
    /* Card styling */
    .custom-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        color: white;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s;
    }
    
    .custom-card:hover {
        transform: translateY(-5px);
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        border: none;
        padding: 0.5rem 2rem;
        font-weight: bold;
        border-radius: 0.5rem;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 0.5s ease-out;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for performance
if 'counter' not in st.session_state:
    st.session_state.counter = 0
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

# Sidebar with enhanced features
with st.sidebar:
    st.markdown("# 🚀 **Apna Technology**")
    st.markdown("---")
    
    # User profile section
    with st.expander("👤 User Profile", expanded=True):
        user_name = st.text_input("Name", placeholder="Enter your name", key="sidebar_name")
        user_email = st.text_input("Email", placeholder="your@email.com", key="sidebar_email")
        if user_name:
            st.success(f"Welcome {user_name}! 🎉")
    
    st.markdown("---")
    
    # Navigation menu
    st.markdown("### 📍 Navigation")
    page = st.radio(
        "",
        ["🏠 Home", "📊 Dashboard", "📝 Forms", "📈 Analytics", "🎮 Games", "💬 Chat", "📁 Resources"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    # Settings
    with st.expander("⚙️ Settings"):
        theme = st.select_slider("Theme", ["Light", "Dark", "Neon"], value="Light")
        notifications = st.toggle("Notifications", value=True)
        auto_save = st.toggle("Auto-save", value=True)
    
    st.markdown("---")
    
    # Progress
    st.markdown("### 📊 Today's Progress")
    progress_val = st.session_state.counter % 100
    st.progress(progress_val / 100)
    st.caption(f"Completed: {progress_val}%")
    
    st.markdown("---")
    
    # Social links
    st.markdown("### 🔗 Connect")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("[📘](https://facebook.com)")
    with col2:
        st.markdown("[🐦](https://twitter.com)")
    with col3:
        st.markdown("[📷](https://instagram.com)")

# Main content based on navigation
if page == "🏠 Home":
    st.markdown("# 🚀 **Apna Technology Platform**")
    st.markdown("### *Empowering Innovation Through Technology*")
    
    # Welcome card
    st.markdown("""
    <div class='custom-card fade-in'>
        <h2>✨ Welcome to Apna Technology!</h2>
        <p>Your one-stop destination for cutting-edge tech solutions, learning resources, and innovative tools.</p>
        <p>🌟 Explore our features and transform your digital experience!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features grid
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <h3>📊 50+</h3>
            <p>Interactive Widgets</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <h3>🚀 1000+</h3>
            <p>Active Users</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <h3>⭐ 4.9/5</h3>
            <p>User Rating</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Original demo components organized
    st.markdown("---")
    st.markdown("## 🎯 **Quick Demo**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Text Elements")
        st.title("Apna Technology(Title)")
        st.header("Apna Technology(Header)")
        st.subheader("Apna Technology(Sub-Header)")
        st.write("Apna Technology(Text)")
        st.markdown("Apna Technology(Markdown)")
        st.caption("Apna Technology(Caption)")
    
    with col2:
        st.markdown("### Media Elements")
        st.image("https://via.placeholder.com/300x200.png?text=Apna+Technology", caption="Sample Image")
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")
        st.video("https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4")

elif page == "📊 Dashboard":
    st.markdown("# 📊 **Live Dashboard**")
    
    # Real-time metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📈 Total Revenue", "$124,567", "🔺 15%")
    with col2:
        st.metric("👥 Active Users", "8,942", "🔺 23%")
    with col3:
        st.metric("🔄 Conversion Rate", "3.2%", "🔻 0.5%")
    with col4:
        st.metric("⭐ Satisfaction", "94%", "🔺 4%")
    
    # Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Sales Trend")
        chart_data = pd.DataFrame(
            np.random.randn(50, 3),
            columns=["Sales", "Marketing", "R&D"]
        )
        st.area_chart(chart_data)
    
    with col2:
        st.markdown("### Performance Metrics")
        bar_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=["Q1", "Q2", "Q3"]
        )
        st.bar_chart(bar_data)
    
    # Data table
    st.markdown("### Real-time Data")
    df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
    st.dataframe(df, use_container_width=True)
    
    # Map
    st.markdown("### Location Heatmap")
    map_data = pd.DataFrame({
        'lat': np.random.uniform(18.5, 19.5, 100),
        'lon': np.random.uniform(73.8, 74.2, 100)
    })
    st.map(map_data)

elif page == "📝 Forms":
    st.markdown("# 📝 **Interactive Forms**")
    
    tab1, tab2, tab3 = st.tabs(["Basic Inputs", "Advanced Form", "Survey"])
    
    with tab1:
        st.markdown("### Basic Input Widgets")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.checkbox('Accept Terms & Conditions')
            clicked = st.button('Click Me!')
            if clicked:
                st.balloons()
                st.success("Button clicked!")
            
            city = st.radio('Select your city', ['Pune', 'Mumbai', 'Delhi', 'Surat'])
            st.write(f"Selected: {city}")
        
        with col2:
            sports = st.multiselect('Favorite Sports', ['Cricket', 'Football', 'Basketball', 'Tennis'])
            rating = st.select_slider('Rate our service', ['Bad', 'Average', 'Good', 'Excellent'])
            marks = st.slider('Your Score', 0, 100, 50)
    
    with tab2:
        st.markdown("### Advanced Registration Form")
        
        with st.form("registration_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            
            with col1:
                name = st.text_input("Full Name")
                email = st.text_input("Email")
                age = st.number_input("Age", 18, 100, 25)
            
            with col2:
                phone = st.text_input("Phone Number")
                dob = st.date_input("Date of Birth")
                color = st.color_picker("Favorite Color")
            
            bio = st.text_area("About Yourself", height=100)
            
            submitted = st.form_submit_button("Register Now")
            
            if submitted:
                if name and email:
                    st.success(f"Welcome {name}! Registration successful!")
                    st.session_state.user_data[name] = {"email": email, "age": age}
                else:
                    st.error("Please fill required fields!")
    
    with tab3:
        st.markdown("### Quick Survey")
        
        satisfaction = st.slider("How satisfied are you?", 0, 100, 75)
        recommend = st.radio("Would you recommend us?", ["Yes", "No", "Maybe"])
        feedback = st.text_area("Your feedback")
        
        if st.button("Submit Feedback"):
            st.success("Thank you for your feedback! 🎉")

elif page == "📈 Analytics":
    st.markdown("# 📈 **Analytics Center**")
    
    # Advanced charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Line Chart")
        line_data = pd.DataFrame(
            np.random.randn(30, 3),
            columns=["Product A", "Product B", "Product C"]
        )
        st.line_chart(line_data)
    
    with col2:
        st.markdown("### Scatter Plot")
        scatter_data = pd.DataFrame(
            np.random.randn(50, 3),
            columns=["X Axis", "Y Axis", "Z Axis"]
        )
        st.scatter_chart(scatter_data)
    
    # Statistical data
    st.markdown("### Statistical Summary")
    table_data = pd.DataFrame(
        np.random.randn(10, 5),
        columns=["Metric 1", "Metric 2", "Metric 3", "Metric 4", "Metric 5"]
    )
    st.table(table_data)
    
    # Additional metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "72 °F", "1.2 °F")
    col2.metric("Humidity", "68%", "-5%")
    col3.metric("Wind Speed", "12 mph", "3 mph")

elif page == "🎮 Games":
    st.markdown("# 🎮 **Interactive Games**")
    
    # Number guessing game
    st.markdown("## 🔢 Number Guessing Game")
    
    if 'target' not in st.session_state:
        st.session_state.target = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
    
    if not st.session_state.game_over:
        guess = st.number_input("Guess a number (1-100)", 1, 100, key="guess")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Check Guess"):
                st.session_state.attempts += 1
                if guess < st.session_state.target:
                    st.warning(f"📈 Too low! Attempt #{st.session_state.attempts}")
                elif guess > st.session_state.target:
                    st.warning(f"📉 Too high! Attempt #{st.session_state.attempts}")
                else:
                    st.success(f"🎉 Correct! You won in {st.session_state.attempts} attempts!")
                    st.balloons()
                    st.session_state.game_over = True
        
        with col2:
            if st.button("New Game"):
                st.session_state.target = random.randint(1, 100)
                st.session_state.attempts = 0
                st.session_state.game_over = False
                st.rerun()
    
    # Counter game
    st.markdown("## 🎯 Click Counter")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("-", key="decrement"):
            st.session_state.counter -= 1
    
    with col2:
        st.markdown(f"<h1 style='text-align: center;'>{st.session_state.counter}</h1>", unsafe_allow_html=True)
    
    with col3:
        if st.button("+", key="increment"):
            st.session_state.counter += 1
    
    if st.button("Reset Counter"):
        st.session_state.counter = 0
        st.success("Counter reset!")

elif page == "💬 Chat":
    st.markdown("# 💬 **Live Chat Support**")
    
    # Chat interface
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    prompt = st.chat_input("Type your message...")
    
    if prompt:
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        # Auto-response
        response = f"Thanks for your message! Our team will respond shortly. (Message: {prompt[:50]}...)"
        st.session_state.chat_history.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.write(response)
    
    # Clear chat button
    if st.button("Clear Chat History"):
        st.session_state.chat_history = []
        st.rerun()

elif page == "📁 Resources":
    st.markdown("# 📁 **Resource Center**")
    
    tab1, tab2 = st.tabs(["Upload Files", "Documentation"])
    
    with tab1:
        st.markdown("### File Uploader")
        uploaded_file = st.file_uploader("Choose a file", type=['csv', 'txt', 'jpg', 'png', 'pdf'])
        
        if uploaded_file is not None:
            st.success(f"✅ {uploaded_file.name} uploaded successfully!")
            st.info(f"File size: {uploaded_file.size} bytes")
            
            if uploaded_file.type == "text/csv":
                df = pd.read_csv(uploaded_file)
                st.dataframe(df)
    
    with tab2:
        st.markdown("### Status Messages")
        st.success("Success message example")
        st.error("Error message example")
        st.warning("Warning message example")
        st.info("Information message example")
        
        # Progress status
        with st.status("Processing..."):
            st.write("Step 1 complete")
            time.sleep(0.5)
            st.write("Step 2 complete")
            time.sleep(0.5)
            st.write("All steps complete!")

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**📧 Contact:** support@apnatechnology.com")
with col2:
    st.markdown("**📞 Phone:** +1 234 567 8900")
with col3:
    st.markdown("**📍 Location:** Tech Park, India")

st.markdown("""
<div style='text-align: center; padding: 1rem; background: linear-gradient(120deg, #667eea 0%, #764ba2 100%); border-radius: 0.5rem; color: white; margin-top: 1rem;'>
    <p>© 2024 Apna Technology. All rights reserved. | Built with ❤️ using Streamlit</p>
    <p>Version 2.0 | Last updated: December 2024</p>
</div>
""", unsafe_allow_html=True)

# Instructions to run
st.sidebar.markdown("---")
st.sidebar.info("""
# How to run this app:
```bash
# streamlit run apps.py
```
""")
