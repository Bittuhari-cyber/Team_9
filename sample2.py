import streamlit as st

# HTML Banner
HTML_BANNER = """
<div style="background-color:Orange;padding:10px;border-radius:10px">
<h1 style="color:Black;text-align:center;">Face Recognition</h1>
</div>
"""
st.markdown(HTML_BANNER, unsafe_allow_html=True)

# Sidebar UI
st.sidebar.title('Face Recognition')
st.sidebar.text('Params For video')

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

# Test Image Upload
img_file_buffer = st.sidebar.file_uploader("Upload the Test image", type=["jpg", "jpeg", 'png'])
if img_file_buffer:
    st.sidebar.image(img_file_buffer, caption="Uploaded Image", use_column_width=True)

# Text Input
name_input = st.sidebar.text_input('Name of the Person', value='Rose')

# Video Input
video_file_buffer = st.sidebar.file_uploader("Upload a video", type=["mp4", "mov", 'avi', 'asf', 'm4v'])

# Buttons
use_webcam = st.sidebar.button('Use Webcam')
stop_button = st.sidebar.button('Stop Processing')

if stop_button:
    st.stop()
