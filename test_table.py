import streamlit as st

def display_test_table():
    if 'test_data' not in st.session_state:
        st.session_state['test_data'] = [
            {'id': 1, 'name': 'Item 1', 'value': '$100', 'status': 'Active'},
            {'id': 2, 'name': 'Item 2', 'value': '$200', 'status': 'Inactive'},
            {'id': 3, 'name': 'Item 3', 'value': '$300', 'status': 'Active'}
        ]

    st.markdown(
        "<h3 style='color: black; font-size: 16px;'>Test Table</h3>",
        unsafe_allow_html=True
    )

    table_html = "<table style='width: 100%; border-collapse: collapse; margin-top: 5px; border: 1px solid #E0E0E0;'>"
    header = "<tr>"
    headers = ["Select", "ID", "Name", "Value", "Status", "Actions"]
    for header_name in headers:
        header += f"<th style='border: 1px solid #E0E0E0; padding: 2px; text-align: left; font-size: 13px; background-color: #f1f1f1; font-weight: 500;'>{header_name}</th>"
    header += "</tr>"
    table_html += header
    st.markdown(table_html, unsafe_allow_html=True)

    for idx, item in enumerate(st.session_state['test_data']):
        row = "<tr>"
        # Checkbox column
        checked = 'checked' if item['id'] in st.session_state.get('selected_test_items', []) else ''
        row += f"<td style='border: 1px solid #E0E0E0; padding: 2px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'>"
        with st.container():
            checked_state = st.checkbox("", value=item['id'] in st.session_state.get('selected_test_items', []), key=f"select_{item['id']}_{idx}", label_visibility="hidden")
            if checked_state:
                if 'selected_test_items' not in st.session_state:
                    st.session_state['selected_test_items'] = []
                if item['id'] not in st.session_state['selected_test_items']:
                    st.session_state['selected_test_items'].append(item['id'])
            else:
                if 'selected_test_items' in st.session_state and item['id'] in st.session_state['selected_test_items']:
                    st.session_state['selected_test_items'].remove(item['id'])
        row += "</td>"
        # Data columns
        row += f"<td style='border: 1px solid #E0E0E0; padding: 2px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'>{item['id']}</td>"
        row += f"<td style='border: 1px solid #E0E0E0; padding: 2px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'>{item['name']}</td>"
        row += f"<td style='border: 1px solid #E0E0E0; padding: 2px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'>{item['value']}</td>"
        row += f"<td style='border: 1px solid #E0E0E0; padding: 2px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'}; color: {'green' if item['status'] == 'Active' else 'red'};'>{item['status']}</td>"
        # Actions column
        row += f"<td style='border: 1px solid #E0E0E0; padding: 2px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'>"
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("✏️", key=f"edit_{item['id']}_{idx}", help="Edit"):
                st.session_state[f"edit_{item['id']}_active"] = True
        with col2:
            if st.button("🗑️", key=f"delete_{item['id']}_{idx}", help="Delete"):
                st.session_state[f"delete_{item['id']}_confirm"] = True
        row += "</td>"
        row += "</tr>"
        st.markdown(row, unsafe_allow_html=True)

        # Edit form
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

        # Delete confirmation
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
