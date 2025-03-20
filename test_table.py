import streamlit as st

def display_test_table():
    # Initialize session state for test data
    if 'test_data' not in st.session_state:
        st.session_state['test_data'] = [
            {'id': 1, 'name': 'Item 1', 'value': '$100', 'status': 'Active'},
            {'id': 2, 'name': 'Item 2', 'value': '$200', 'status': 'Inactive'},
            {'id': 3, 'name': 'Item 3', 'value': '$300', 'status': 'Active'}
        ]

    # Display table with inline styles
    st.markdown(
        "<h3 style='color: black; font-size: 16px;'>Test Table</h3>",
        unsafe_allow_html=True
    )

    table_html = "<table style='width: 100%; border-collapse: collapse; margin-top: 5px; border: 1px solid #E0E0E0;'>"
    header = "<tr>"
    headers = ["ID", "Name", "Value", "Status", "Actions"]
    for header_name in headers:
        header += f"<th style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 13px; background-color: #f1f1f1; font-weight: 500;'>{header_name}</th>"
    header += "</tr>"
    table_html += header

    for idx, item in enumerate(st.session_state['test_data']):
        row = "<tr>"
        row += f"<td style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'>{item['id']}</td>"
        row += f"<td style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'>{item['name']}</td>"
        row += f"<td style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'>{item['value']}</td>"
        row += f"<td style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'}; color: {'green' if item['status'] == 'Active' else 'red'};'>{item['status']}</td>"
        row += f"<td style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'>"
        row += f"<button style='background: none; border: none; cursor: pointer; font-size: 13px; padding: 2px; margin: 0 2px;' title='Edit'><i class='far fa-edit'></i></button>"
        row += f"<button style='background: none; border: none; cursor: pointer; font-size: 13px; padding: 2px; margin: 0 2px;' title='Delete'><i class='far fa-trash-alt'></i></button>"
        if st.button("", key=f"edit_{item['id']}", help="Edit"):
            st.session_state[f"edit_{item['id']}"] = True
        if st.button("", key=f"delete_{item['id']}", help="Delete"):
            st.session_state['test_data'] = [d for d in st.session_state['test_data'] if d['id'] != item['id']]
            st.rerun()
        row += "</td>"
        row += "</tr>"
        st.markdown(row, unsafe_allow_html=True)

    table_html += "</table>"
    st.markdown(table_html, unsafe_allow_html=True)

    # Edit form
    for item in st.session_state['test_data']:
        if st.session_state.get(f"edit_{item['id']}"):
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
                    st.session_state[f"edit_{item['id']}"] = False
                    st.rerun()
