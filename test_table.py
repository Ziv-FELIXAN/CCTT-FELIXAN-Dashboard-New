import streamlit as st
import pandas as pd

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

    # Convert test_data to DataFrame
    df = pd.DataFrame(st.session_state['test_data'])
    df['Select'] = [False] * len(df)  # Add a Select column for checkboxes
    df['Actions'] = [''] * len(df)  # Add an Actions column for Edit/Delete icons

    # Display the DataFrame with checkboxes and icons
    edited_df = st.data_editor(
        df,
        column_config={
            "Select": st.column_config.CheckboxColumn("Select", default=False),
            "id": st.column_config.NumberColumn("ID", disabled=True),
            "name": st.column_config.TextColumn("Name", disabled=True),
            "value": st.column_config.TextColumn("Value", disabled=True),
            "status": st.column_config.TextColumn("Status", disabled=True),
            "Actions": st.column_config.Column("Actions", disabled=True)
        },
        hide_index=True,
        use_container_width=True,
        num_rows="fixed"
    )

    # Add Edit and Delete icons in the Actions column
    for idx, item in enumerate(st.session_state['test_data']):
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("✏️", key=f"edit_icon_{item['id']}_{idx}", help="Edit"):
                st.session_state[f"edit_{item['id']}_active"] = True
        with col2:
            if st.button("🗑️", key=f"delete_icon_{item['id']}_{idx}", help="Delete"):
                st.session_state[f"delete_{item['id']}_confirm"] = True

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
