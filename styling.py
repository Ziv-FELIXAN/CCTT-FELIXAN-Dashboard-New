import streamlit as st

def apply_styling():
    # Add Font Awesome for icons
    st.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        """,
        unsafe_allow_html=True
    )

    # Very simple CSS to test if styling is applied
    st.markdown(
        """
        <style>
        /* Apply a simple style to all text to test if CSS loads */
        * {
            color: green !important; /* Change all text to green to test */
            font-size: 16px !important; /* Change font size to 16px to test */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
