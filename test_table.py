import streamlit as st
from custom_button import custom_button

def display_test_table():
    if 'test_data' not in st.session_state:
        st.session_state['test_data'] = [
            {'id': 1, 'name': 'Item 1', 'value': '$100', 'status': 'Active'},
            {'id': 2, 'name': 'Item 2', 'value': '$200', 'status': 'Inactive'},
            {'id': 3, 'name': 'Item 3', 'value': '$300', 'status': 'Active'}
        ]

    # Custom CSS for the table
    st.markdown(
        """
        <style>
        .custom-table {
            width: 50%;
            border-collapse: collapse;
            border: 2px solid #E0E0E0;
            font-family: Arial, sans-serif;
        }
        .custom-table th, .custom-table td {
            border: 1px solid #E0E0E0;
            padding: 2px;
            text-align: center;
            font-size: 13px;
        }
        .custom-table th {
            background-color: #f1f1f1;
            font-size: 14px;
            font-weight: bold;
        }
        .custom-table tr:nth-child(even) {
            background-color: #F5F5F5;
        }
        .custom-table tr:nth-child(odd) {
            background-color: #FFFFFF;
        }
        .custom-table .status-active {
            background-color: #00FF00;
            color: black;
        }
        .custom-table .status-inactive {
            background-color: #FF0000;
            color: black;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "<h3 style='color: black; font-size: 16px;'>Test Table</h3>",
        unsafe_allow_html=True
    )

    # Build the table using HTML
    table_html = "<table class='custom-table'>"
    # Header row
    table_html += "<tr>"
    table_html += "<th>Select</th>"
    table_html += "<th>ID</th>"
    table_html += "<th>Name</th>"
    table_html += "<th>Value</th>"
    table_html += "<th>Status</th>"
    table_html += "<th>Edit</th>"
    table_html += "<th>Delete</th>"
    table_html += "</tr>"

    # Data rows
    for idx, item in enumerate(st.session_state['test_data']):
        table_html += "<tr>"
        # Select column
        checked = 'checked' if item['id'] in st.session_state.get('selected_test_items', []) else ''
        table_html += f"<td><input type='checkbox' {checked} id='select_{item['id']}_{idx}' style='width: 13px; height: 13px;'></td>"
        # Data columns
        table_html += f"<td>{item['id']}</td>"
        table_html += f"<td>{item['name']}</td>"
        table_html += f"<td>{item['value']}</td>"
        table_html += f"<td class='status-{'active' if item['status'] == 'Active' else 'inactive'}'>{item['status']}</td>"
        # Edit and Delete buttons using custom_button
        table_html += "<td>"
        custom_button(
            label="Edit",
            key=f"edit_{item['id']}_{idx}",
            action=lambda: st.session_state.update({f"edit_{item['id']}_active": True}),
            width="60px",
            height="20px",
            font_size="12px",
            bg_color="#e0e0e0",
            hover_color="#d0d0d0"
        )
        table_html += "</td>"
        table_html += "<td>"
        custom_button(
            label="Delete",
            key=f"delete_{item['id']}_{idx}",
            action=lambda: st.session_state.update({f"delete_{item['id']}_confirm": True}),
            width="60px",
            height="20px",
            font_size="12px",
            bg_color="#e0e0e0",
            hover_color="#d0d0d0"
        )
        table_html += "</td>"
        table_html += "</tr>"

        if st.session_state.get(f"edit_{item['id']}_active"):
            with st.form(key=f"edit_form_{item['id']}"):
                st.markdown(f"<h3 style='color: black; font-size: 16px;'>Edit Item: {item['name']}</h3>", unsafe_allow_html=True)
                new_name = st.text_input("Name", value=item['name'])
                new_value = st.text_input("Value", value=item['value'])
                new_status = st.selectbox("Status", ["Active", "Inactive"], index=0 if item['status'] == "Active" else 1)
                edit_submit = st.form_submit_button("Save Changes")
                if edit_submit:
                    for d in st.session_state['test_data']:
                        if d['id'] == item['id']:
                            d['name'] = new_name
                            d['value'] = new_value
                            d['status'] = new_status
                            break
                    st.session_state[f"edit_{item['id']}_active"] = False
                    st.rerun()

        if st.session_state.get(f"delete_{item['id']}_confirm"):
            with st.form(key=f"delete_form_{item['id']}"):
                st.markdown(f"<h3 style='color: black; font-size: 16px;'>Delete Item: {item['name']}</h3>", unsafe_allow_html=True)
                st.markdown("<p style='color: black; font-size: 14px;'>Are you sure you want to delete this item? This action cannot be undone.</p>", unsafe_allow_html=True)
                confirm_delete = st.text_input("Type the item name to confirm", placeholder=item['name'])
                delete_submit = st.form_submit_button("Confirm Delete")
                if delete_submit:
                    if confirm_delete == item['name']:
                        st.session_state['test_data'] = [d for d in st.session_state['test_data'] if d['id'] != item['id']]
                        st.session_state[f"delete_{item['id']}_confirm"] = False
                        st.rerun()
                    else:
                        st.error("Item name does not match. Deletion cancelled.")
                        st.session_state[f"delete_{item['id']}_confirm"] = False

    table_html += "</table>"
    st.markdown(table_html, unsafe_allow_html=True)
