import streamlit as st
import streamlit.components.v1 as components

def custom_button(label, key, action, width="60px", height="20px", font_size="12px", bg_color="#e0e0e0", hover_color="#d0d0d0"):
    # Custom CSS for the button
    button_style = f"""
    <style>
    .custom-button-{key} {{
        height: {height};
        font-size: {font_size};
        padding: 0px 5px;
        border-radius: 0px;
        line-height: {height};
        width: {width};
        text-align: center;
        background-color: {bg_color};
        border: 1px solid #ccc;
        cursor: pointer;
        transition: background-color 0.3s;
        display: inline-block;
        text-decoration: none;
        color: black;
    }}
    .custom-button-{key}:hover {{
        background-color: {hover_color};
    }}
    </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    # Create the button with a unique ID
    button_html = f"<a href='#' class='custom-button-{key}' id='button_{key}'>{label}</a>"
    components.html(
        f"""
        {button_html}
        <script>
        document.getElementById('button_{key}').onclick = function() {{
            document.getElementById('{key}').click();
        }};
        </script>
        """,
        height=int(height.replace("px", "")) + 10,
        width=int(width.replace("px", "")) + 10
    )

    # Hidden Streamlit button to trigger the action
    if st.button("", key=key):
        action()
