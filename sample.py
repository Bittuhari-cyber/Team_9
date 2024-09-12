import streamlit as st
import tempfile
from PIL import Image
import streamlit.components.v1 as stc
import numpy as np

# HTML Banner
HTML_BANNER = """
<div style="background-color:Orange;padding:10px;border-radius:10px">
<h1 style="color:Black;text-align:center;">Face Recognition</h1>
</div>
"""

# Demo files
DEMO_IMAGE = 'test.png'
DEMO_VIDEO = 'demo.mp4'

# Display banner
stc.html(HTML_BANNER)

# Sidebar UI
st.sidebar.title('Face Recognition')
st.sidebar.text('Params For video')

# Custom CSS for sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 400px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 400px;
        margin-left: -400px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Image upload section
img_file_buffer = st.sidebar.file_uploader("Upload the Test image", type=["jpg", "jpeg", 'png'])
if not img_file_buffer:
    image = np.array(Image.open(DEMO_IMAGE))
else:
    image = np.array(Image.open(img_file_buffer))

st.sidebar.image(image, caption="Uploaded/Test Image", use_column_width=True)

# Name input
name_input = st.sidebar.text_input('Name of the Person', value='Rose')

# Webcam and video input buttons
use_webcam = st.sidebar.button('Use Webcam')
video_file_buffer = st.sidebar.file_uploader("Upload a video", type=["mp4", "mov", 'avi', 'asf', 'm4v'])

# Stop processing button
stop_button = st.sidebar.button('Stop Processing')
if stop_button:
    st.stop()

# Video display
if not video_file_buffer:
    st.sidebar.text('Input Video')
    st.sidebar.video(DEMO_VIDEO)
else:
    tfflie = tempfile.NamedTemporaryFile(delete=False)
    tfflie.write(video_file_buffer.read())
    st.sidebar.video(tfflie.name)

# Display a success message
st.write("Streamlit UI elements loaded successfully!")
