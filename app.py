import streamlit as st
from general_ui import setup_general_ui, setup_version_management
from styling import apply_styling
from test_table import display_test_table

st.set_page_config(layout="wide")

conn, c, current_version = setup_general_ui()

apply_styling()

display_test_table()

st.markdown(
    f"<div style='background-color: #f1f1f1; padding: 10px; text-align: center; margin-top: 20px;'>"
    f"<p style='color: black; font-size: 14px;'>System Status: Online | Version: {current_version} | Date: 18/03/2025 | © System copyright Ziv Rotem-Bar 2025</p>"
    "</div>",
    unsafe_allow_html=True
)

setup_version_management(conn, c, current_version)
