from langchain.llms import OpenAI,AzureOpenAI
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.chains.question_answering import load_qa_chain
import streamlit as st

import os
# Setting up the api key
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_TYPE"] = 'azure'
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_BASE"] = os.environ["AZURE_OPENAI_ENDPOINT"]
os.environ["OPENAI_API_KEY"] =  os.environ["AZURE_OPENAI_API_KEY"]


st.title("👨‍💻 Chat with your PDF")

st.write("Please upload your PDF file below.")

filename = st.file_uploader("Upload a PDF")

query = st.text_area("Insert your query")

if st.button("Submit Query", type="primary"):

    # Create an OpenAI object.
    # llm = OpenAI(openai_api_key=API_KEY)
    llm = AzureOpenAI(deployment_name="text-davinci-003")

    loader = UnstructuredPDFLoader(filename)
    print(filename)
    data = loader.load()
    print(data)

    chain = load_qa_chain(llm,chain_type="stuff",verbose=True)

    response = chain.run(data, question=query)
    # Create a Pandas DataFrame agent.
    st.write(response)

