import streamlit as st

def apply_styling():
    # Add Font Awesome for icons
    st.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        """,
        unsafe_allow_html=True
    )

    # CSS with specific styles
    st.markdown(
        """
        <style>
        /* Keep the green color to confirm CSS is loading */
        * {
            color: green !important;
        }
        /* Specific font size for text in div and p elements */
        div, p {
            font-size: 16px !important; /* Test font size for div and p elements */
        }
        /* Specific styling for tabs */
        div[data-baseweb="tab"] {
            font-size: 14px !important; /* Smaller font for tabs */
            padding: 2px 8px !important; /* Smaller padding for tabs */
            border-radius: 4px !important;
        }
        div[data-baseweb="tab"][aria-selected="true"] {
            background-color: #E74C3C !important; /* Red for active tab */
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
