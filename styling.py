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
            color: red !important; /* Change all text to red to test */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
