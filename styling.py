import streamlit as st

def apply_styling():
    # Add Font Awesome for icons
    st.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        """,
        unsafe_allow_html=True
    )

    # Use inline HTML styles instead of CSS
    st.markdown(
        """
        <style>
        /* Minimal CSS to ensure Font Awesome works */
        </style>
        """,
        unsafe_allow_html=True
    )
