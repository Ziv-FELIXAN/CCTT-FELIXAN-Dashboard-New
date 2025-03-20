import streamlit as st
from members_private import display_members_private

def manage_modules():
    # Module navigation with inline styles
    module_container = st.container()
    with module_container:
        st.markdown("<h3 style='color: black; font-size: 16px;'>Modules:</h3>", unsafe_allow_html=True)
        modules = st.session_state['users'][st.session_state['interface_type']]["modules"]
        module_cols = st.columns(len(modules))
        for i, module in enumerate(modules):
            with module_cols[i]:
                if st.button(module, key=f"module_{i}"):
                    st.session_state['selected_module'] = module
                    st.rerun()

    # Main content area with tabs
    st.session_state['tabs'] = st.tabs(["Overview", "Manage Objects", "Checklist", "Related Assets", "Log"])

    # Display module content based on selection
    if st.session_state['selected_module'] == "Members" and st.session_state['interface_type'] == "Private":
        display_members_private()
    elif st.session_state['selected_module'] == "Dashboard":
        with st.session_state['tabs'][0]:
            st.markdown(
                "<div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px;'>"
                "<h3 style='color: black; font-size: 16px;'>Dashboard Overview</h3>"
                "<p style='color: black; font-size: 14px;'>Welcome to your Dashboard! Here you can see a summary of your activities and status.</p>"
                "</div>",
                unsafe_allow_html=True
            )
        with st.session_state['tabs'][1]:
            st.markdown(
                "<div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px;'>"
                "<h3 style='color: black; font-size: 16px;'>Manage Dashboard Objects</h3>"
                "<p style='color: black; font-size: 14px;'>No objects to manage in the Dashboard.</p>"
                "</div>",
                unsafe_allow_html=True
            )
        with st.session_state['tabs'][2]:
            st.markdown(
                "<div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px;'>"
                "<h3 style='color: black; font-size: 16px;'>Dashboard Checklist</h3>"
                "<p style='color: black; font-size: 14px;'>No checklist items for the Dashboard.</p>"
                "</div>",
                unsafe_allow_html=True
            )
        with st.session_state['tabs'][3]:
            st.markdown(
                "<div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px;'>"
                "<h3 style='color: black; font-size: 16px;'>Related Assets for Dashboard</h3>"
                "<p style='color: black; font-size: 14px;'>No related assets for the Dashboard.</p>"
                "</div>",
                unsafe_allow_html=True
            )
        with st.session_state['tabs'][4]:
            st.markdown(
                "<div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px;'>"
                "<h3 style='color: black; font-size: 16px;'>Activity Log</h3>"
                "<p style='color: black; font-size: 14px;'>No activities logged yet for the Dashboard.</p>"
                "</div>",
                unsafe_allow_html=True
            )
    else:
        with st.session_state['tabs'][0]:
            st.markdown(
                f"<div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px;'>"
                f"<h3 style='color: black; font-size: 16px;'>{st.session_state['selected_module']} Overview</h3>"
                "<p style='color: black; font-size: 14px;'>Content for Overview tab (to be implemented).</p>"
                "</div>",
                unsafe_allow_html=True
            )
        with st.session_state['tabs'][1]:
            st.markdown(
                f"<div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px;'>"
                f"<h3 style='color: black; font-size: 16px;'>Manage {st.session_state['selected_module']} Objects</h3>"
                "<p style='color: black; font-size: 14px;'>Content for Manage Objects tab (to be implemented).</p>"
                "</div>",
                unsafe_allow_html=True
            )
        with st.session_state['tabs'][2]:
            st.markdown(
                f"<div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px;'>"
                f"<h3 style='color: black; font-size: 16px;'>{st.session_state['selected_module']} Checklist</h3>"
                "<p style='color: black; font-size: 14px;'>Content for Checklist tab (to be implemented).</p>"
                "</div>",
                unsafe_allow_html=True
            )
        with st.session_state['tabs'][3]:
            st.markdown(
                f"<div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px;'>"
                f"<h3 style='color: black; font-size: 16px;'>Related Assets for {st.session_state['selected_module']}</h3>"
                "<p style='color: black; font-size: 14px;'>Content for Related Assets tab (to be implemented).</p>"
                "</div>",
                unsafe_allow_html=True
            )
        with st.session_state['tabs'][4]:
            st.markdown(
                "<div style='border: 1px solid #e6e6e6; padding: 10px; border-radius: 5px;'>"
                "<h3 style='color: black; font-size: 16px;'>Activity Log</h3>"
                "<p style='color: black; font-size: 14px;'>No activities logged yet for this module.</p>"
                "</div>",
                unsafe_allow_html=True
            )
