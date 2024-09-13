import streamlit as st
from elasticsearch import Elasticsearch
from utils.streamlit_utils import display_results

with open('./style.css','r') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
if __name__ == "__main__" : 
    client = Elasticsearch("http://localhost:9200/" )
    st.write('## Insert Your Question Here')
    st.sidebar.write('# Search Features ')
    searchType = st.sidebar.selectbox('Select Search Type:', ['match','fuzzy'])

    with st.form("my_form"):
        query = st.text_input('Enter some text')
        submit = st.form_submit_button("Search")
        if submit :
            display_results(client,query,searchType)