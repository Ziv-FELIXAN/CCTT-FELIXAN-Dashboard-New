import streamlit as st

def apply_styling():
    # Add Font Awesome for icons
    st.markdown(
        """
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        """,
        unsafe_allow_html=True
    )

    # Simplified CSS with a clear test style (background color)
    st.markdown(
        """
        <style>
        /* Test style to verify if CSS is loading */
        body {
            background-color: #f0f8ff; /* Light blue background to test if CSS loads */
            font-family: 'Arial', sans-serif;
            font-size: 14px; /* Slightly larger font for testing */
            color: #333;
        }
        /* Basic styling for headers */
        h3 {
            font-size: 16px;
            font-weight: 500;
            margin-bottom: 8px;
        }
        h4 {
            font-size: 14px;
            font-weight: 500;
            margin-bottom: 5px;
        }
        /* Simplified table styling */
        .custom-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 5px;
            border: 1px solid #E0E0E0;
        }
        .custom-table th, .custom-table td {
            border: 1px solid #E0E0E0;
            padding: 4px;
            text-align: left;
            font-size: 14px;
        }
        .custom-table th {
            background-color: #f1f1f1;
            font-weight: 500;
        }
        .custom-table tr:nth-child(even) {
            background-color: #F5F5F5;
        }
        /* Simplified card styling */
        .overview-card {
            background-color: #F5F5F5;
            border: 1px solid #E0E0E0;
            border-radius: 4px;
            padding: 8px;
            margin: 4px 0;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .overview-card i {
            font-size: 14px;
            color: #666;
        }
        .overview-card p {
            margin: 0;
            font-size: 14px;
        }
        /* Simplified button styling */
        .icon-button {
            background: none;
            border: none;
            cursor: pointer;
            font-size: 14px;
            padding: 2px;
            margin: 0 2px;
        }
        /* Checkbox styling */
        input[type="checkbox"] {
            width: 14px;
            height: 14px;
        }
        /* Container styling */
        .module-content {
            border: 1px solid #E0E0E0;
            border-radius: 4px;
            padding: 10px;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
