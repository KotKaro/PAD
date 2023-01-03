import time

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stats")
st.markdown("# Stats")
st.sidebar.header("Stats")

data = st.file_uploader("Upload your data sets", type=['csv'])
if data is not None:
    df = pd.read_csv(data)
    with st.spinner('Loading...'):
        time.sleep(1)
    st.dataframe(df.head(10))

    area_chart = 'Area chart'
    bar_chart = 'Bar chart'
    diagram = st.selectbox("Select diagram to display", options=[area_chart, bar_chart])
    diagram_x = st.selectbox("Select property for X", options=df.columns)
    diagram_y = st.selectbox("Select property for Y", options=df.columns)
    if diagram == area_chart:
        st.area_chart(df, y=diagram_y, x=diagram_x)
    elif diagram == bar_chart:
        st.bar_chart(df, y=diagram_y, x=diagram_x)
