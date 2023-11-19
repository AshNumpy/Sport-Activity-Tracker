import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="My Sport Activity",
    page_icon="🦈",
    layout="wide"
)

with st.container():
    logo, navbar = st.columns((1,5))

    with logo:
        st.markdown("""
        <h1 class="logo-header">
            🦈 Ramaz
        </h1>
        """, unsafe_allow_html=True)

    with navbar:
        st.write("")
        navabr = option_menu(
            "",
            ['Home', 'Dashboard', 'Contact'], 
            icons=['house-check', 'speedometer2', 'chat-left-dots'],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal"
        )
