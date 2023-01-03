import streamlit as st


def run():
    st.set_page_config(page_title="Main page")
    st.sidebar.success("Select a page above.")


if __name__ == "__main__":
    run()
