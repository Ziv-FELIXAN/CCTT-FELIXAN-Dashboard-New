import streamlit as st

def apply_styling():
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #E0E0E0;
            color: black;
            border: none;
            padding: 4px 8px;
            font-size: 14px;
            cursor: pointer;
            border-radius: 4px;
        }
        .stButton>button:hover {
            background-color: #D0D0D0;
        }
        .stSelectbox>div>div {
            background-color: #E0E0E0;
            color: black;
            border: none;
            padding: 4px;
            font-size: 14px;
            border-radius: 4px;
        }
        .stTextInput>div>input {
            background-color: #E0E0E0;
            color: black;
            border: none;
            padding: 4px;
            font-size: 14px;
            border-radius: 4px;
        }
        .stCheckbox>div {
            display: flex;
            align-items: center;
        }
        .stCheckbox>div>label {
            margin-left: 4px;
            color: black;
            font-size: 14px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
