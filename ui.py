import streamlit as st

st.title("👨‍💻 Chat with your CSV")

st.write("Please upload your CSV file below.")

data = st.file_uploader("Upload a CSV")