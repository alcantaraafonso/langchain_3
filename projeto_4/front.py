import streamlit as st
import langchain_helper as lch
import textwrap

st.title('Assistante YT')

with st.sidebar:
    st.form(key='my-form')
    yt_url = st.sidebar.text_area(label='URL do Vídeio', max_chars=50)
    query = st.sidebar.text_area(label='me pergunte algo sobre o vídeo', max_chars=50, key='query')

    submit_button = st.form_submit_button(label='Enviar')

    if query and yt_url:
        db = lch.create_vector_from_yt_url(yt_url)
        response, docs = lch.get_response_from_query(db, query)

        st.subheader("resposta: ")
        st.text(textwrap.fill(response["answer"], width=85))