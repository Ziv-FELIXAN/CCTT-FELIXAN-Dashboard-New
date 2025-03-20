import streamlit as st

def render_table(data, columns, actions=None, actions_field=None, checkbox_key=None, key=None):
    table_html = "<table style='width: 100%; border-collapse: collapse; margin-top: 5px; border: 1px solid #E0E0E0;'>"
    header = "<tr>"
    if checkbox_key:
        header += "<th style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 13px; background-color: #f1f1f1; font-weight: 500;'>Select</th>"
    for col in columns:
        header += f"<th style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 13px; background-color: #f1f1f1; font-weight: 500;'>{col['name']}</th>"
    if actions or actions_field:
        header += "<th style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 13px; background-color: #f1f1f1; font-weight: 500;'>Actions</th>"
    header += "</tr>"
    table_html += header
    st.markdown(table_html, unsafe_allow_html=True)

    for idx, item in enumerate(data):
        row = "<tr>"
        if checkbox_key:
            checked = 'checked' if item['id'] in st.session_state.get(checkbox_key, []) else ''
            row += f"<td style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'><input type='checkbox' {checked} id='{checkbox_key}_{item['id']}' style='width: 13px; height: 13px;'></td>"
            checked_state = st.checkbox("", value=item['id'] in st.session_state.get(checkbox_key, []), key=f"{checkbox_key}_{item['id']}", label_visibility="hidden")
            if checked_state:
                if checkbox_key not in st.session_state:
                    st.session_state[checkbox_key] = []
                if item['id'] not in st.session_state[checkbox_key]:
                    st.session_state[checkbox_key].append(item['id'])
            else:
                if checkbox_key in st.session_state and item['id'] in st.session_state[checkbox_key]:
                    st.session_state[checkbox_key].remove(item['id'])
        for col in columns:
            value = item.get(col['field'], 'N/A')
            if 'format' in col:
                value = col['format'](item)
            style = col.get('style', '')
            if callable(style):
                style = style(item)
            row += f"<td style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'}; {style}'>{value}</td>"
        if actions or actions_field:
            actions_html = "<td style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 13px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'>"
            if actions_field and item.get(actions_field):
                for action in item[actions_field]:
                    actions_html += f"<button style='background: none; border: none; cursor: pointer; font-size: 13px; padding: 2px; margin: 0 2px;' title='{action['title']}' onclick='document.getElementById(\"{action['action']}\").click();'><i class='{action['icon']}'></i></button>"
            elif actions:
                for action in actions:
                    actions_html += f"<button style='background: none; border: none; cursor: pointer; font-size: 13px; padding: 2px; margin: 0 2px;' title='{action['title']}' onclick='document.getElementById(\"{action['action']}\").click();'><i class='{action['icon']}'></i></button>"
            actions_html += "</td>"
            row += actions_html
        row += "</tr>"
        st.markdown(row, unsafe_allow_html=True)

    table_html += "</table>"
    st.markdown(table_html, unsafe_allow_html=True)

    if key:
        st.download_button(
            label="Download as CSV",
            data=",".join([col['name'] for col in columns]) + "\n" + "\n".join([",".join([str(item.get(col['field'], 'N/A')) for col in columns]) for item in data]),
            file_name="table_data.csv",
            mime="text/csv",
            key=key
        )

def render_summary_card(icon, title, value):
    st.markdown(
        f"<div style='border: 1px solid #E0E0E0; border-radius: 4px; padding: 8px; margin-bottom: 8px; display: inline-block; width: 200px; margin-right: 8px;'>"
        f"<p style='color: black; font-size: 14px; margin: 0;'><i class='{icon}' style='margin-right: 4px;'></i>{title}</p>"
        f"<p style='color: black; font-size: 16px; font-weight: 500; margin: 0;'>{value}</p>"
        "</div>",
        unsafe_allow_html=True
    )

def render_filter(object_types, objects, type_key, object_key):
    selected_type = st.selectbox("Select Object Type", object_types, key=type_key)
    object_ids = [obj['id'] for obj in objects if selected_type.lower() in obj['activity'].lower()]
    selected_object_id = st.selectbox("Select Object", object_ids, key=object_key) if object_ids else None
    return selected_type, selected_object_id

def render_checklist(checklist_items, object_id, log_action):
    items = [item for item in checklist_items if item['object_id'] == object_id]
    for item in items:
        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            st.markdown(f"<p style='color: black; font-size: 14px;'>{item['id']}.</p>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<p style='color: black; font-size: 14px;'>{item['step']}</p>", unsafe_allow_html=True)
        with col3:
            checked = st.checkbox("", value=item['completed'], key=f"checklist_{item['id']}", label_visibility="hidden")
            if checked != item['completed']:
                item['completed'] = checked
                log_action("Update Checklist", item['id'], f"{'Completed' if checked else 'Uncompleted'} step: {item['step']}")
                st.rerun()
        if not item['completed']:
            render_document_manager(item['id'], item['documents'], log_action)

def render_document_manager(checklist_id, documents, log_action):
    st.markdown("<h5 style='color: black; font-size: 14px; margin-top: 8px;'>Documents</h5>", unsafe_allow_html=True)
    uploaded_file = st.file_uploader(f"Upload document for checklist {checklist_id}", key=f"upload_{checklist_id}")
    if uploaded_file:
        documents.append({'name': uploaded_file.name, 'status': 'Pending'})
        log_action("Upload Document", checklist_id, f"Uploaded document: {uploaded_file.name}")
        st.rerun()
    for doc in documents:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"<p style='color: black; font-size: 14px;'>{doc['name']}</p>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<p style='color: {'orange' if doc['status'] == 'Pending' else 'green'}; font-size: 14px;'>{doc['status']}</p>", unsafe_allow_html=True)
