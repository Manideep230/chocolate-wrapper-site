import streamlit as st

# Set page configuration
st.set_page_config(page_title="Customized Chocolate Wrapper", layout="centered")

# Header Section
st.markdown(
    """
    <style>
    .header {
        background-color: #6a0dad;
        color: white;
        text-align: center;
        padding: 1.5rem;
        font-size: 1.8rem;
    }
    </style>
    <div class="header">
        Create Your Customized Chocolate Wrapper
    </div>
    """,
    unsafe_allow_html=True,
)

# Chocolate Description Section
st.markdown(
    """
    <style>
    .wrapper-info {
        text-align: center;
        padding: 1.5rem;
        background-color: #fff;
    }
    .wrapper-info img {
        width: 300px;
        margin-top: 1rem;
        border: 3px solid #6a0dad;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="wrapper-info">
        <h2>Make Your Gift Unique!</h2>
        <p>
            Surprise your loved ones with chocolates wrapped in a personalized photo wrapper. 
            Add your memories to the wrapper and make any occasion unforgettable!
        </p>
        <img src="image.png" alt="Customized Chocolate Wrapper">
    </div>
    """,
    unsafe_allow_html=True,
)

# Google Form Link Section
st.markdown(
    """
    <style>
    .google-form {
        background-color: #fdf5e6;
        padding: 2rem;
        text-align: center;
    }
    .google-form a {
        display: inline-block;
        padding: 10px 20px;
        background-color: #6a0dad;
        color: #fff;
        text-decoration: none;
        font-size: 1.1rem;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .google-form a:hover {
        background-color: #4b087b;
    }
    </style>
    <div class="google-form">
        <h2>Order Your Customized Chocolate Now</h2>
        <p>Click the button below to fill out the form and upload your photos for customization.</p>
        <a href="https://forms.gle/DbWyrcmXRp48MHKH9" target="_blank">
            Fill Out the Form
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Footer Section
st.markdown(
    """
    <style>
    .footer {
        text-align: center;
        padding: 1rem;
        background-color: #6a0dad;
        color: #fff;
        font-size: 0.9rem;
    }
    </style>
    <div class="footer">
        &copy; 2024 Customized Chocolate Creations | All Rights Reserved.
    </div>
    """,
    unsafe_allow_html=True,
)
