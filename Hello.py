import streamlit as st

st.header('This is my first web app.')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

code = '''def ML():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")