import pandas as pd 
import streamlit as st

def display_database(df, hareket_ismi):
    database = df.rename({
            "created time": "Date",
            "hareketin_ismi": "Movement Name",
            "max_agirlik": "Maximum Weight",
            "max_tekrar": "Maximum Rep",
            "summary": "Formulation"
        }, axis=1)
    
    threshold = database[database['Movement Name']==hareket_ismi]
    if len(threshold)>1:
        database = threshold

    st.dataframe(
        data=database,
        use_container_width=True,
        hide_index=False
    )