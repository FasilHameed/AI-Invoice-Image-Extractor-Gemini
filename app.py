from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Configure Google API key from environment variables
load_dotenv()
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-pro-vision')

# Function to get Gemini response
def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Function to extract image details
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Set page title and description
st.set_page_config(
    page_title='Invoice AI Assistant',
    page_icon=':money_with_wings:',
    layout='wide',
    initial_sidebar_state='collapsed'
)

# Page title and description
st.title('Welcome to Invoice AI Assistant!')
st.markdown('This app helps you analyze invoices using AI.')

# Input prompt textbox
input_prompt = st.text_input("Input prompt:", key="input")

# Apply CSS style to text input
st.markdown('<style>input[type="text"] {color: black;}</style>', unsafe_allow_html=True)

# File uploader for image selection
uploaded_file = st.file_uploader("Choose an image of the invoice", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Button to trigger invoice analysis
submit = st.button("Analyze Invoice")

# Perform analysis on button click
if submit:
    # Extract image details
    image_data = input_image_details(uploaded_file)
    # Get response from Gemini model
    response = get_gemini_response(input_prompt, image_data, input_prompt)
    # Display response
    st.subheader("The Response For Your Query is")
    st.write(response)

# UI enhancements
st.markdown(
    """
    <style>
        .reportview-container {
            background: linear-gradient(to bottom, #f2f2f2, #ffffff);
        }
        .sidebar .sidebar-content {
            background: linear-gradient(to bottom, #f2f2f2, #ffffff);
        }
        .st-bk {
            background-color: #ffffff;
        }
        .st-c5 {
            color: #1b2d6b;
        }
        .stButton>button {
            background-color: #1b2d6b !important;
            color: white !important;
            font-weight: bold;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #0056b3 !important;
        }
        .stTextInput>div>div>input {
            border-color: #1b2d6b !important;
        }
        .stTextInput>div>div>input:focus {
            box-shadow: 0 0 0 0.2rem rgba(27, 45, 107, 0.25) !important;
            border-color: #1b2d6b !important;
        }
        .stMarkdown a {
            color: #1b2d6b !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)
