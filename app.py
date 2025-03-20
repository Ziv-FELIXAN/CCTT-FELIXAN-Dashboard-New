import streamlit as st
from general_ui import setup_general_ui, setup_version_management
from styling import apply_styling
from module_manager import manage_modules

# Set page layout to wide (must be the first Streamlit command)
st.set_page_config(layout="wide")

# Setup general UI and version management
conn, c, current_version = setup_general_ui()

# Apply styling and add a test message to confirm it's called
apply_styling()
st.write("Styling applied successfully!")  # Test message to confirm apply_styling() is called

# Manage modules
manage_modules()

# Footer
st.markdown(
    f"<div style='background-color: #f1f1f1; padding: 10px; text-align: center; margin-top: 20px;'>"
    f"<p>System Status: Online | Version: {current_version} | Date: 18/03/2025 | © System copyright Ziv Rotem-Bar 2025</p>"
    "</div>",
    unsafe_allow_html=True
)

# Version management
setup_version_management(conn, c, current_version)
