import streamlit as st
from streamlit_option_menu import option_menu
import datetime


# PAGE CONFIGURATION
st.set_page_config(
    page_title="My Sport Activity",
    page_icon="🦈",
    layout="wide"
)


# SIDEBAR
with st.sidebar:
    st.header("🐁 GYM Faresi")
    
    navbar_select = option_menu(
        "",
        ['Home', 'Dashboard', 'Raw Dataset', 'Contact'], 
        icons=['house-check', 'speedometer2', 'database', 'chat-left-dots'],
        menu_icon="cast",
        default_index=0,
        orientation="vertically"
    )


st.header(f"{navbar_select}")

# FILTERS
with st.container():
    filter1, filter2, filter3, filter4 = st.columns(4)

    with filter1:
        hareket_ismi = st.selectbox(
            "Movement",
            ("Bench Press", "Overhead Press", "Leg Press"),
            placeholder="Choose a movement",
            label_visibility="collapsed",
            index=None
        )
    
    with filter2:
        max_agirlik_temp = 100

        max_agirlik = st.number_input(
            "Maximum Weight",
            min_value=0,
            max_value=max_agirlik_temp,
            value=None,
            label_visibility="collapsed",
            placeholder="Choose a weight (kg)"
        )

    with filter3:
        max_tekrar_temp = 5

        max_tekrar = st.slider(
            "Maximum Rep",
            min_value=1,
            max_value=15,
            value=5,
            label_visibility="collapsed"
        )

    with filter4:   
        today = datetime.datetime.now()
        min_date = datetime.date(today.year, 1, 1)
        max_date = datetime.date(today.year, 12, 31)

        date = st.date_input(
            "Date Range",
            value=(min_date, today),
            min_value=min_date,
            max_value=max_date,
            format="DD.MM.YYYY",
            label_visibility="collapsed"
        )