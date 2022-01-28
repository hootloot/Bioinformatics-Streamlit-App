import streamlit as st

st.set_page_config(
    page_title='Target Protien Exploratory Data Analysis',
    layout='wide',
    initial_sidebar_state='expanded',

)

def main():
    cs_sidebar()
    cs_body()

    return None

def cs_sidebar():

    st.sidebar.header('How to use this application?')
    st.sidebar.markdown('__Enter your target proiten in the input text book__')
    st.sidebar.write('Check the chembl data base for target protiens you want to search: ')
    st.caption('For example: Cornavirus')

    return None


def cs_body():
    st.text_input('Enter your target protien: ')
    st.info('Example: Cornavirus')
    
