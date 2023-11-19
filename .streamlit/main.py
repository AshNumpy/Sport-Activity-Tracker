import streamlit as st
from streamlit_option_menu import option_menu
import datetime
import pandas as pd

# PAGE CONFIGURATION
st.set_page_config(
    page_title="My Sport Activity",
    page_icon="🦈",
    layout="wide"
)

# DATASET READ
df = pd.read_parquet("./exported-files/agirlik_takibi.parquet")


# SIDEBAR
with st.sidebar:
    st.title("🐁 GYM Faresi")
    
    navbar_select = option_menu(
        "",
        ['Home', 'Dashboard', 'Database', 'Contact'], 
        icons=['house-check', 'speedometer2', 'database', 'chat-left-dots'],
        menu_icon="cast",
        default_index=0,
        orientation="vertically"
    )


st.title(f"{navbar_select}")

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
            placeholder="Input a weight (kg)"
        )

    with filter3:
        max_tekrar_temp = 5

        max_tekrar = st.number_input(
            "Maximum Rep",
            min_value=1,
            max_value=15,
            value=None,
            label_visibility="collapsed",
            placeholder="Input a rep number"
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


# PAGEINATION
if navbar_select == "Home":
    st.write("Homepage")


if navbar_select == "Dashboard":
    with st.container():
        tight_col, wide_col = st.columns((1,3))

        with tight_col:
            st.header("KPI-1")
            st.write("""
            Fusce eget gravida lacus. Maecenas a libero eu diam rutrum rutrum. Mauris ultrices turpis ut orci commodo, eget rhoncus eros sodales.
            """)

        with wide_col:
            st.write("""
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur eget vestibulum arcu. Vivamus eget fermentum ex. Aenean gravida dictum facilisis. Curabitur feugiat elementum risus a aliquet. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus maximus ligula vitae lacus interdum, eget interdum magna ultricies. Vivamus eu metus mauris. Cras ac convallis nisl. Etiam finibus elementum egestas. Praesent dignissim ligula vitae felis maximus, sed commodo lorem maximus. Vivamus non felis dignissim, vestibulum nibh in, pretium velit. Cras efficitur tristique magna, ac interdum nisl faucibus vel. Aliquam eros ante, sollicitudin a ultricies vitae, interdum eget dolor. Phasellus varius mauris vel porttitor euismod. Suspendisse mollis purus tempor felis interdum, vehicula maximus nibh efficitur.
            """)


if navbar_select == "Database":
    from myPages import dataset
    
    with st.container():
        dataset.display_database(df,hareket_ismi)


if navbar_select == "Contact":
    st.write("contact page")