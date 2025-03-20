import streamlit as st
from datetime import datetime
from templates import render_table, render_summary_card, render_filter, render_checklist, render_document_manager

def display_members_private():
    # Initialize session state for members, activities, checklist, contracts, assets, and log
    if 'members' not in st.session_state:
        st.session_state['members'] = [{
            'id': 1,
            'user_type': 'Private',
            'name': 'John Doe',
            'join_date': '2024-01-15',
            'status': 'Active',
            'verification': 'Complete',
            'security': 'High',
            'premium': 'Yes',
            'email': 'john.doe@example.com',
            'phone': '+1234567890'
        }]

    if 'activities' not in st.session_state:
        st.session_state['activities'] = [
            {'id': 1, 'user_id': 1, 'activity': 'Loan Application Submitted', 'date': '2025-03-01', 'amount': None, 'is_active': True},
            {'id': 2, 'user_id': 1, 'activity': 'Carat Transaction', 'date': '2025-03-02', 'amount': '$50,000', 'is_active': True}
        ]

    if 'checklist' not in st.session_state:
        st.session_state['checklist'] = [
            {'id': 1, 'user_id': 1, 'object_id': 1, 'step': 'Submit Application', 'completed': True, 'documents': []},
            {'id': 2, 'user_id': 1, 'object_id': 1, 'step': 'Verify Identity', 'completed': False, 'documents': []},
            {'id': 3, 'user_id': 1, 'object_id': 1, 'step': 'Review Terms', 'completed': False, 'documents': []},
            {'id': 4, 'user_id': 1, 'object_id': 1, 'step': 'Sign Agreement', 'completed': False, 'documents': []}
        ]

    if 'contracts' not in st.session_state:
        st.session_state['contracts'] = [
            {'id': 1, 'user_id': 1, 'contract_id': 'Contract #123', 'description': 'Loan Agreement', 'date': '2025-03-01', 'amount': '$10,000', 'status': 'Active'}
        ]

    if 'assets' not in st.session_state:
        st.session_state['assets'] = [
            {'id': 1, 'user_id': 1, 'asset_id': 'Asset #456', 'description': 'Car', 'value': '$20,000', 'status': 'Active'}
        ]

    if 'action_log' not in st.session_state:
        st.session_state['action_log'] = []

    if 'action_counter' not in st.session_state:
        st.session_state['action_counter'] = 0

    if 'notify_user' not in st.session_state:
        st.session_state['notify_user'] = False  # Default: no notifications

    # Get user and filter activities
    user = st.session_state['members'][0]
    user_id = user['id']
    activities = [activity for activity in st.session_state['activities'] if activity['user_id'] == user_id and activity['is_active']]
    non_active_activities = [activity for activity in st.session_state['activities'] if activity['user_id'] == user_id and not activity['is_active']]
    checklist_items = [item for item in st.session_state['checklist'] if item['user_id'] == user_id]
    contracts = [contract for contract in st.session_state['contracts'] if contract['user_id'] == user_id]
    assets = [asset for asset in st.session_state['assets'] if asset['user_id'] == user_id]

    # Function to log actions
    def log_action(action_type, object_id, details):
        st.session_state['action_counter'] += 1
        action_id = st.session_state['action_counter']
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            'action_id': action_id,
            'action_type': action_type,
            'object_id': object_id,
            'details': details,
            'timestamp': timestamp
        }
        st.session_state['action_log'].insert(0, log_entry)  # Add to the top of the log

    # Overview tab
    with st.session_state['tabs'][0]:
        st.markdown(
            "<div style='border: 1px solid #E0E0E0; border-radius: 4px; padding: 8px; margin-bottom: 8px;'>"
            "<h3 style='margin-top: 0;'>Members - Private Individuals</h3>",
            unsafe_allow_html=True
        )

        # Summary cards
        st.markdown("<div style='border: 1px solid #E0E0E0; border-radius: 4px; padding: 8px; margin-bottom: 8px;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='font-size: 14px; font-weight: 500; margin-top: 0;'>Activity Summary</h4>", unsafe_allow_html=True)
        render_summary_card("far fa-tasks", "Active Projects", len(activities))
        render_summary_card("far fa-exclamation-circle", "Projects Needing Action", sum(1 for item in checklist_items if not item['completed']))
        render_summary_card("far fa-archive", "Non-Active Projects", len(non_active_activities))
        render_summary_card("far fa-file-alt", "Documents Pending Approval", sum(len(item['documents']) for item in checklist_items))
        st.markdown("</div>", unsafe_allow_html=True)

    # Manage Objects tab
    with st.session_state['tabs'][1]:
        st.markdown(
            "<div style='border: 1px solid #E0E0E0; border-radius: 4px; padding: 8px; margin-bottom: 8px;'>"
            "<h3 style='margin-top: 0;'>Manage Members Activities</h3>",
            unsafe_allow_html=True
        )

        # Display active activities table
        st.markdown("<h4 style='font-size: 14px; font-weight: 500; margin-top: 0;'>Active Activities</h4>", unsafe_allow_html=True)
        columns = [
            {"name": "Object ID", "field": "id"},
            {"name": "Activity", "field": "activity"},
            {"name": "Date", "field": "date"},
            {"name": "Amount", "field": "amount"}
        ]
        # Define actions dynamically for each activity
        for activity in activities:
            activity['actions'] = [
                {"icon": "far fa-edit", "action": f"edit_{activity['id']}", "title": "Edit Activity"},
                {"icon": "far fa-trash-alt", "action": f"delete_{activity['id']}", "title": "Move to Non-Active"}
            ]
        render_table(activities, columns, actions_field="actions", checkbox_key="selected_activities", key="download_active_activities")

        # Handle actions
        for activity in activities:
            edit_key = f"edit_{activity['id']}"
            delete_key = f"delete_{activity['id']}"
            # Edit activity
            if st.session_state.get(edit_key):
                with st.form(key=f"edit_activity_form_{activity['id']}"):
                    st.subheader(f"Edit Activity: {activity['activity']}")
                    new_activity_type = st.text_input("Activity Type", value=activity['activity'])
                    new_activity_date = st.text_input("Date (YYYY-MM-DD)", value=activity['date'])
                    new_activity_amount = st.text_input("Amount (optional)", value=activity['amount'] if activity['amount'] else "")
                    edit_submit = st.form
