import streamlit as st

def render_table(data, columns, actions=None, actions_field=None, checkbox_key=None, key=None):
    # Render a custom table with inline styles
    table_html = "<table style='width: 100%; border-collapse: collapse; margin-top: 5px; border: 1px solid #E0E0E0;'>"
    # Table header
    header = "<tr>"
    if checkbox_key:
        header += "<th style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 14px; background-color: #f1f1f1; font-weight: 500;'>Select</th>"
    for col in columns:
        header += f"<th style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 14px; background-color: #f1f1f1; font-weight: 500;'>{col['name']}</th>"
    if actions or actions_field:
        header += "<th style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 14px; background-color: #f1f1f1; font-weight: 500;'>Actions</th>"
    header += "</tr>"
    table_html += header
    st.markdown(table_html, unsafe_allow_html=True)

    # Table rows
    for idx, item in enumerate(data):
        row = "<tr>"
        if checkbox_key:
            checked = 'checked' if item['id'] in st.session_state.get(checkbox_key, []) else ''
            row += f"<td style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 14px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'><input type='checkbox' {checked} id='{checkbox_key}_{item['id']}'></td>"
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
            if col.get('style'):
                style = col['style'](item) if callable(col['style']) else col['style']
                row += f"<td style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 14px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'}; {style}'>{value}</td>"
            else:
                row += f"<td style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 14px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'>{value}</td>"
        if actions or actions_field:
            row += "<td style='border: 1px solid #E0E0E0; padding: 4px; text-align: left; font-size: 14px; background-color: {'#F5F5F5' if idx % 2 == 0 else '#FFFFFF'};'>"
            current_actions = item.get(actions_field, []) if actions_field else actions
            for action in current_actions:
                row += f"<button style='background: none; border: none; cursor: pointer; font-size: 14px; padding: 2px; margin: 0 2px;' title='{action['title']}'><i class='{action['icon']}'></i></button>"
                if st.button("", key=action['action'], help=action['title']):
                    st.session_state[action['action']] = True
            row += "</td>"
        row += "</tr>"
        st.markdown(row, unsafe_allow_html=True)
    st.markdown("</table>", unsafe_allow_html=True)

    # Add CSV download button with inline styles
    if data:
        csv = "\n".join([",".join([col['name'] for col in columns])] + [",".join([str(item.get(col['field'], 'N/A')) for col in columns]) for item in data])
        st.download_button(
            label="Download as CSV <i class='fas fa-download' style='margin-left: 5px;'></i>",
            data=csv,
            file_name="table.csv",
            mime="text/csv",
            key=key,
            use_container_width=False
        )

def render_summary_card(icon, title, value):
    st.markdown(
        f"<div style='background-color: #F5F5F5; border: 1px solid #E0E0E0; border-radius: 4px; padding: 8px; margin: 4px 0; display: flex; align-items: center; gap: 6px;'>"
        f"<i class='{icon}' style='font-size: 14px; color: #666;'></i>"
        f"<p style='margin: 0; font-size: 14px; color: black;'>{title}: {value}</p>"
        "</div>",
        unsafe_allow_html=True
    )

def render_filter(types, objects, type_key, object_key, type_label="Select Object Type", object_label="Select Object"):
    selected_type = st.selectbox(type_label, types, key=type_key, label_visibility="visible")
    filtered_objects = [obj for obj in objects if selected_type.lower() in obj['activity'].lower()]
    object_ids = [obj['id'] for obj in filtered_objects]
    selected_object_id = st.selectbox(object_label, object_ids, format_func=lambda x: next(obj['activity'] for obj in filtered_objects if obj['id'] == x), key=object_key, label_visibility="visible")
    return selected_type, selected_object_id

def render_document_manager(item_id, documents):
    with st.form(key=f"docs_form_{item_id}"):
        st.markdown("<h3 style='color: black; font-size: 16px;'>Manage Documents</h3>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Upload Document", key=f"upload_{item_id}")
        notes = st.text_area("Notes", key=f"notes_{item_id}")
        submit_doc = st.form_submit_button("Add Document")
        if submit_doc and uploaded_file:
            documents.append({'name': uploaded_file.name, 'notes': notes})
            st.success("Document added successfully!")
            st.rerun()

    if documents:
        st.markdown("<h4 style='color: black; font-size: 14px;'>Uploaded Documents:</h4>", unsafe_allow_html=True)
        for doc in documents:
            col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
            with col1:
                st.markdown(f"<p style='color: black; font-size: 14px;'>{doc['name']}</p>", unsafe_allow_html=True)
            with col2:
                st.markdown(f"<p style='color: black; font-size: 14px;'>Notes: {doc['notes']}</p>", unsafe_allow_html=True)
            with col3:
                if st.button("Edit", key=f"edit_doc_{item_id}_{doc['name']}"):
                    st.session_state[f"edit_doc_{item_id}_{doc['name']}"] = True
            with col4:
                if st.button("Delete", key=f"delete_doc_{item_id}_{doc['name']}"):
                    documents.remove(doc)
                    st.rerun()

            if f"edit_doc_{item_id}_{doc['name']}" in st.session_state and st.session_state[f"edit_doc_{item_id}_{doc['name']}"]:
                with st.form(key=f"edit_doc_form_{item_id}_{doc['name']}"):
                    st.markdown(f"<h3 style='color: black; font-size: 16px;'>Edit Document: {doc['name']}</h3>", unsafe_allow_html=True)
                    new_notes = st.text_area("Notes", value=doc['notes'], key=f"edit_notes_{item_id}_{doc['name']}")
                    edit_submit = st.form_submit_button("Save Changes")
                    if edit_submit:
                        doc['notes'] = new_notes
                        st.success("Document notes updated successfully!")
                        st.session_state[f"edit_doc_{item_id}_{doc['name']}"] = False
                        st.rerun()

def render_checklist(items, object_id, log_action):
    object_checklist = [item for item in items if item['object_id'] == object_id]
    total_steps = len(object_checklist)
    completed_steps = sum(1 for item in object_checklist if item['completed'])
    progress = (completed_steps / total_steps) * 100 if total_steps > 0 else 0

    for i, item in enumerate(object_checklist):
        col1, col2, col3 = st.columns([0.5, 3, 1])
        with col1:
            st.markdown(f"<p style='color: black; font-size: 14px;'>{i+1}.</p>", unsafe_allow_html=True)
        with col2:
            checked = st.checkbox(item['step'], value=bool(item['completed']), key=f"checklist_{item['id']}")
            if checked != bool(item['completed']):
                for chk in items:
                    if chk['id'] == item['id']:
                        chk['completed'] = checked
                        break
                log_action("Update Checklist", item['id'], f"Updated checklist item: {item['step']} to {'Completed' if checked else 'Not Completed'}")
                st.rerun()
        with col3:
            if st.button("", key=f"docs_{item['id']}", help="Manage Documents"):
                st.session_state[f"manage_docs_{item['id']}"] = True
            st.markdown("<i class='far fa-paperclip' style='font-size: 14px; color: black;'></i>", unsafe_allow_html=True)

        if f"manage_docs_{item['id']}" in st.session_state and st.session_state[f"manage_docs_{item['id']}"]:
            render_document_manager(item['id'], item['documents'])

    st.markdown(
        "<div style='background-color: #e0e0e0; height: 15px; width: 50%; border-radius: 5px; margin-top: 10px;'>"
        f"<div style='background-color: #E74C3C; height: 15px; width: {progress}%; border-radius: 5px;'></div>"
        "</div>"
        f"<p style='font-size: 14px; margin-top: 5px; color: black;'>Progress: {progress:.0f}%</p>",
        unsafe_allow_html=True
    )
