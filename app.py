import streamlit as st
from general_ui import setup_general_ui, setup_version_management
from styling import apply_styling
from module_manager import manage_modules

# Set page layout to wide
st.set_page_config(layout="wide")

# Setup general UI and version management
conn, c, current_version = setup_general_ui()

# Apply minimal styling (Font Awesome only)
apply_styling()

# Add inline styles to test
st.markdown(
    "<h1 style='color: blue; font-size: 24px;'>CTT/FELIXAN System Ver3 - Test Inline Style</h1>",
    unsafe_allow_html=True
)

# Manage modules
manage_modules()

# Footer with inline styles
st.markdown(
    "<div style='background-color: #f1f1f1; padding: 10px; text-align: center; margin-top: 20px;'>"
    "<p style='color: black; font-size: 14px;'>System Status: Online | Version: VER3 | Date: 18/03/2025 | © System copyright Ziv Rotem-Bar 2025</p>"
    "</div>",
    unsafe_allow_html=True
)

# Version management
setup_version_management(conn, c, current_version)
