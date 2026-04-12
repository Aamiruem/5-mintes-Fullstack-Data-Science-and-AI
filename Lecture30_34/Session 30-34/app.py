import streamlit as st
import pandas as pd
import numpy as np
import time
import plotly.express as px
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Apna Technology - Complete Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown(
    """
    <style>
    /* Main container styling */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Custom card styling */
    .custom-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        color: white;
        margin-bottom: 1rem;
    }
    
    /* Metric styling */
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Header styling */
    h1 {
        background: linear-gradient(120deg, #f093fb 0%, #f5576c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem !important;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        border: none;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: transform 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Success message styling */
    .stAlert {
        border-radius: 0.5rem;
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Sidebar with enhanced features
with st.sidebar:
    st.markdown("## 🚀 **Apna Technology**")
    st.markdown("---")

    # User profile section
    st.markdown("### 👤 User Profile")
    user_name = st.text_input("Your Name", placeholder="Enter your name")
    user_email = st.text_input("Email", placeholder="your@email.com")

    if user_name:
        st.success(f"Welcome back, {user_name}! 🎉")

    st.markdown("---")

    # Theme selector
    theme = st.selectbox("🎨 Select Theme", ["Light", "Dark", "Neon"])

    # Settings
    st.markdown("### ⚙️ Settings")
    notifications = st.checkbox("Enable Notifications", value=True)
    auto_refresh = st.checkbox("Auto Refresh Data", value=False)

    st.markdown("---")

    # Progress tracker
    st.markdown("### 📊 Your Progress")
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    st.markdown("---")

    # Social links
    st.markdown("### 🔗 Connect With Us")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("[📘](https://facebook.com)")
    with col2:
        st.markdown("[🐦](https://twitter.com)")
    with col3:
        st.markdown("[📷](https://instagram.com)")

# Main content area
st.markdown("# 🚀 **Apna Technology Platform**")
st.markdown("#### *Your One-Stop Solution for Tech Excellence*")

# Custom card for welcome message
st.markdown(
    """
<div class='custom-card'>
    <h3 style='margin:0;'>✨ Welcome to the Future of Learning!</h3>
    <p style='margin:0;'>Explore cutting-edge technology tools and resources</p>
</div>
""",
    unsafe_allow_html=True,
)

# Key metrics in columns
st.markdown("### 📈 Live Metrics")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("📊 Active Users", "12,345", "🔺 15%")
with col2:
    st.metric("📚 Courses Completed", "8,942", "🔺 23%")
with col3:
    st.metric("⭐ User Rating", "4.8/5", "🔺 0.2")
with col4:
    st.metric("🎯 Success Rate", "94%", "🔺 5%")

# Tabs for organized content
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📊 Dashboard", "📝 Forms", "📈 Analytics", "🎮 Interactive", "📁 Resources"]
)

with tab1:
    st.markdown("## Dashboard Overview")

    # Charts in columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Revenue Growth")
        chart_data = pd.DataFrame(
            {
                "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                "Revenue": np.random.randint(100, 500, 6),
                "Expenses": np.random.randint(50, 300, 6),
            }
        )
        st.line_chart(chart_data.set_index("Month"))

    with col2:
        st.markdown("### User Distribution")
        pie_data = pd.DataFrame(
            {
                "Category": ["Students", "Professionals", "Enterprises"],
                "Count": [450, 300, 150],
            }
        )
        fig = px.pie(
            pie_data, values="Count", names="Category", title="User Demographics"
        )
        st.plotly_chart(fig, use_container_width=True)

    # Real-time data table
    st.markdown("### Real-time Data Stream")
    realtime_df = pd.DataFrame(
        np.random.randn(10, 4), columns=["Sales", "Users", "Engagement", "Conversion"]
    )
    st.dataframe(realtime_df, use_container_width=True)

with tab2:
    st.markdown("## 📝 Advanced Form")

    with st.form("advanced_form", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            full_name = st.text_input("Full Name *", placeholder="John Doe")
            email = st.text_input("Email Address *", placeholder="john@example.com")
            phone = st.text_input("Phone Number", placeholder="+1 234 567 8900")
            dob = st.date_input(
                "Date of Birth",
                min_value=datetime(1950, 1, 1),
                max_value=datetime.now(),
            )

        with col2:
            department = st.selectbox(
                "Department", ["IT", "HR", "Finance", "Marketing", "Sales"]
            )
            experience = st.slider("Years of Experience", 0, 40, 5)
            skills = st.multiselect(
                "Skills", ["Python", "Java", "React", "AWS", "Data Science", "AI/ML"]
            )
            salary_range = st.select_slider(
                "Expected Salary Range",
                options=["30k-50k", "50k-70k", "70k-90k", "90k-120k", "120k+"],
            )

        bio = st.text_area(
            "Tell us about yourself",
            height=100,
            placeholder="Share your experience and goals...",
        )

        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            submitted = st.form_submit_button(
                "🚀 Submit Application", use_container_width=True
            )

        if submitted:
            if full_name and email:
                st.success(
                    f"✅ Application submitted successfully! We'll contact you at {email}"
                )
                st.balloons()
            else:
                st.error("❌ Please fill in all required fields!")

with tab3:
    st.markdown("## 📊 Advanced Analytics")

    # Data generation
    np.random.seed(42)
    analytics_data = pd.DataFrame(
        {
            "Date": pd.date_range(start="2024-01-01", periods=30, freq="D"),
            "Website Traffic": np.random.randint(1000, 5000, 30),
            "Conversion Rate": np.random.uniform(0.1, 0.5, 30),
            "Bounce Rate": np.random.uniform(0.2, 0.6, 30),
        }
    )

    col1, col2 = st.columns(2)
    with col1:
        st.area_chart(analytics_data.set_index("Date")["Website Traffic"])
    with col2:
        st.bar_chart(
            analytics_data.set_index("Date")[["Conversion Rate", "Bounce Rate"]]
        )

    # Correlation matrix
    st.markdown("### Feature Correlation")
    corr_data = pd.DataFrame(
        np.random.randn(10, 10), columns=[f"Feature {i}" for i in range(10)]
    )
    st.dataframe(corr_data.corr(), use_container_width=True)

with tab4:
    st.markdown("## 🎮 Interactive Games & Tools")

    # Number guessing game
    st.markdown("### 🔢 Number Guessing Game")
    if "target_number" not in st.session_state:
        st.session_state.target_number = np.random.randint(1, 100)
        st.session_state.attempts = 0

    guess = st.number_input(
        "Guess a number between 1 and 100",
        min_value=1,
        max_value=100,
        key="guess_input",
    )
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔍 Check Guess"):
            st.session_state.attempts += 1
            if guess < st.session_state.target_number:
                st.warning(f"📈 Too low! Attempt #{st.session_state.attempts}")
            elif guess > st.session_state.target_number:
                st.warning(f"📉 Too high! Attempt #{st.session_state.attempts}")
            else:
                st.success(
                    f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts!"
                )
                st.balloons()
                st.session_state.target_number = np.random.randint(1, 100)
                st.session_state.attempts = 0

    with col2:
        if st.button("🔄 New Game"):
            st.session_state.target_number = np.random.randint(1, 100)
            st.session_state.attempts = 0
            st.info("New game started! Guess the number!")

    # Interactive slider with real-time updates
    st.markdown("### 🎚️ Interactive Controls")
    value = st.slider("Adjust the value", 0, 100, 50)
    col1, col2, col3 = st.columns(3)
    col1.metric("Linear Scale", f"{value}%")
    col2.metric("Squared", f"{value**2}")
    col3.metric("Square Root", f"{np.sqrt(value):.2f}")

with tab5:
    st.markdown("## 📁 Resource Library")

    # File uploader with preview
    uploaded_file = st.file_uploader(
        "Upload your document", type=["csv", "txt", "pdf", "jpg", "png"]
    )
    if uploaded_file is not None:
        st.success(f"✅ File '{uploaded_file.name}' uploaded successfully!")
        if uploaded_file.type == "text/csv":
            df_uploaded = pd.read_csv(uploaded_file)
            st.dataframe(df_uploaded.head())

    # Color picker tool
    st.markdown("### 🎨 Color Picker Tool")
    color = st.color_picker("Choose your brand color", "#00f900")
    st.markdown(
        f"<div style='background-color: {color}; padding: 2rem; border-radius: 1rem; text-align: center; color: white;'>Your Selected Color Preview</div>",
        unsafe_allow_html=True,
    )

# Chat interface
st.markdown("---")
st.markdown("## 💬 Live Support Chat")
with st.expander("Open Support Chat"):
    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    prompt = st.chat_input("Type your message here...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Auto response
        with st.chat_message("assistant"):
            response = f"Thank you for your message! Our support team will respond shortly. (You said: {prompt})"
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Footer
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns(3)
with footer_col1:
    st.markdown("**📧 Contact:** support@apnatechnology.com")
with footer_col2:
    st.markdown("**📞 Phone:** +1 234 567 8900")
with footer_col3:
    st.markdown("**📍 Location:** Tech Park, Silicon Valley")

st.markdown(
    """
<div style='text-align: center; padding: 1rem; background: linear-gradient(120deg, #667eea 0%, #764ba2 100%); border-radius: 0.5rem; color: white;'>
    <p>© 2024 Apna Technology. All rights reserved. | Built with ❤️ using Streamlit</p>
</div>
""",
    unsafe_allow_html=True,
)



# streamlit run app.py (terminal command)
