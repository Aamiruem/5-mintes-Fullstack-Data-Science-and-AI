# Import libraries
import streamlit as st        # Streamlit: used to create web apps
import pandas as pd          # Pandas: used for data handling (tables, dataframes)
import numpy as np           # NumPy: used for numerical operations (random data)
import time                  # Time: used to add delay (sleep)

# ------------------- TEXT ELEMENTS -------------------

st.title("Apna Technology(Title)")        # Main title (big text)
st.header("Apna Technology(Header)")     # Header (medium size)
st.subheader("Apna Technology(Sub-Header)")  # Sub-header (smaller)
st.write("Apna Technology(Text)")        # General text display
st.markdown("Apna Technology(Markdown)") # Markdown formatted text
st.caption("Apna Technology(Caption)")   # Small caption text

# ------------------- MEDIA -------------------

st.image("xyz.jpg")     # Display image (must exist in folder)
st.audio("speech.wav")  # Play audio file
# st.audio("speech.mp3")  # Alternative audio (currently commented)
st.video("abc.mkv")     # Play video file

# ------------------- INPUT WIDGETS -------------------

st.checkbox('checkbox')   # Checkbox (True/False)
st.button('Click button') # Button (returns True when clicked)

# Radio button (single option select)
st.radio('Pick your city',['Pune','Mumbai','delhi','Bangalore'])

# Dropdown (single selection)
st.selectbox('Pick your city',['Pune','Mumbai','delhi','surat'])

# Multiple selection list
st.multiselect('Pick favourite sports',['cricket', 'football', 'basketball'])

# Slider with text options
st.select_slider('Give a Remark', ['Bad', 'Good', 'Excellent'])

# Numeric slider
st.slider('Your Marks', 0,100)

# ------------------- TOGGLE -------------------

on = st.toggle("Activate feature")   # Toggle ON/OFF
if on:
    st.write("Feature activated!")   # Executes if toggle is ON

# ------------------- NUMBER INPUT -------------------

number = st.number_input("Insert a number")   # Input number
st.write("The current number is ", number)    # Display number

# ------------------- DATE & TIME -------------------

d = st.date_input("When's your birthday", value=None)  # Date picker
st.write("Your birthday is:", d)

t = st.time_input("Set an alarm for", value=None)      # Time picker
st.write("Alarm is set for", t)

# ------------------- MORE INPUTS -------------------

st.number_input('Enter your marks', 0,100)  # Number input (0–100)
st.text_input('Enter Text')                 # Single-line text input
st.date_input('Exam date')                  # Date input
st.time_input('Exam time')                  # Time input
st.text_area('Description')                 # Multi-line text
st.file_uploader('Upload File')             # Upload file
st.color_picker('Choose a color')           # Pick color

# ------------------- ALERT MESSAGES -------------------

st.success("Success")     # Green success message
st.error("Error")         # Red error message
st.warning("Warning")     # Yellow warning message
st.info("Information")    # Blue info message

# Show exception message
st.exception(RuntimeError("RuntimeError exception"))

# ------------------- SIDEBAR -------------------

st.sidebar.title("Apna Technology")   # Sidebar title
st.sidebar.image("xyz.jpg")           # Sidebar image

# ------------------- DATAFRAME -------------------

# Create random dataframe (50 rows, 20 columns)
df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
# Create a DataFrame with random values
df = pd.DataFrame(  # pd = pandas → DataFrame = table (rows + columns)
    np.random.randn(50, 20),  # np = numpy → random.randn = generate random numbers
    # 50 = number of rows
    # 20 = number of columns
    # randn = values follow normal distribution (mean=0, std=1)
    columns=("col %d" % i for i in range(20)),
    # columns = column names for the table
    # ("col %d" % i ...) → creates names like: col 0, col 1, col 2 ... col 19
    # %d = placeholder for integer
    # i = variable that changes in loop
    # range(20) → generates numbers from 0 to 19
    # for i in range(20) → loop runs 20 times to create 20 column names
)

st.dataframe(df)   # Interactive table (scroll, sort, filter)

# ------------------- STATIC TABLE -------------------

df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)

st.table(df)   # Static table (no interaction)

# ------------------- METRICS -------------------

col1, col2, col3 = st.columns(3)   # Create 3 columns layout

# Display metrics (like dashboard cards)
col1.metric("Temperature", "70 °F", "1.2 °F")  
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# ------------------- CHAT INPUT -------------------

prompt = st.chat_input("Say something")   # Chat input box

if prompt:
    st.write(f"User has sent the following prompt: {prompt}")  # Show message

# ------------------- STATUS / LOADING -------------------

with st.status("Step 1"):   # Status container
    st.write("Step 2")
    time.sleep(1)           # Wait 1 second
    st.write("Step 3")
    time.sleep(1)
    st.write("Step 4")
    time.sleep(1)

st.button("Rerun")   # Button to rerun app

# ------------------- CHARTS -------------------

# Area chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

# Bar chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)

# Line chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

# ------------------- MAP -------------------

# Latitude & Longitude data
df = pd.DataFrame({'lat': [18.5164], 'lon': [73.8561]})

st.map(df)   # Display location on map

# ------------------- SCATTER CHART -------------------

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.scatter_chart(chart_data)

# ------------------- CHAT MESSAGE -------------------

with st.chat_message("user"):
    st.write("Hello ji")   # Show chat message

# ------------------- TERMINAL COMMAND -------------------

# Run this app using terminal:
# streamlit run streams.py
