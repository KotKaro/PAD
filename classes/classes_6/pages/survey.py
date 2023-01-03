import streamlit as st

st.set_page_config(page_title="Survey")
st.markdown("# Survey")
st.sidebar.header("Survey")

with st.form("my_form", clear_on_submit=True):
    surname = st.text_input(label="Surname")
    if surname is None or surname is '':
        st.warning('Surname is required')

    firstname = st.text_input(label="Firstname")
    if firstname is None or firstname is '':
        st.warning('Firstname is required')

    submitted = st.form_submit_button("Submit")
    if submitted and surname and firstname:
        st.success('Survey submitted')
