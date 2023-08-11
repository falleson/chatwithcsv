from langchain.llms import OpenAI,AzureOpenAI
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.chains.question_answering import load_qa_chain
import streamlit as st
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.agents import create_sql_agent
from langchain.sql_database import SQLDatabase
import pandas as pd
import json
import os
# Setting up the api key
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_TYPE"] = 'azure'
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_BASE"] = os.environ["AZURE_OPENAI_ENDPOINT"]
os.environ["OPENAI_API_KEY"] =  os.environ["AZURE_OPENAI_API_KEY"]


def decode_response(response: str) -> dict:
    """This function converts the string response from the model to a dictionary object.

    Args:
        response (str): response from the model

    Returns:
        dict: dictionary with response data
    """
    return json.loads(response)


def write_response(response_dict: dict):
    
    """
    Write a response from an agent to a Streamlit app.

    Args:
        response_dict: The response from the agent.

    Returns:
        None.
    """

    # Check if the response is an answer.
    if "output" in response_dict:
        st.write(response_dict["output"])

    # Check if the response is a bar chart.
    if "bar" in response_dict:
        data = response_dict["bar"]
        df = pd.DataFrame(data)
        df.set_index("columns", inplace=True)
        st.bar_chart(df)

    # Check if the response is a line chart.
    if "line" in response_dict:
        data = response_dict["line"]
        df = pd.DataFrame(data)
        df.set_index("columns", inplace=True)
        st.line_chart(df)

    # Check if the response is a table.
    if "table" in response_dict:
        data = response_dict["table"]
        df = pd.DataFrame(data["data"], columns=data["columns"])
        st.table(df)


st.title("👨‍💻 Chat with your Database")
question = st.text_area("what is query")
if st.button("Submit Query", type="primary"):

    # Create an OpenAI object.
    # llm = OpenAI(openai_api_key=API_KEY)
    llm = AzureOpenAI(deployment_name="text-davinci-003")
    db_conn = 'postgresql://user:Rpc4d:Q2c4j@talkwithdata.postgres.database.azure.com:5432/cntalkwithdata'
    db = SQLDatabase.from_uri(db_conn)   
    # create sql database toolkit
    toolkit = SQLDatabaseToolkit(db=db,llm=llm)

    agent = create_sql_agent(llm=llm,toolkit=toolkit,
                         agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                         verbose=True,
                         agent_executor_kwargs={'return_intermediate_steps': True}
                         )
    prompt = ("""
    For the following query, if it requires drawing a table, reply as follows:
    {"table": {"columns": ["column1", "column2", ...], "data": [[value1, value2, ...], [value1, value2, ...], ...]}}

    If the query requires creating a bar chart, reply as follows:
    {"bar": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}
    
    If the query requires creating a line chart, reply as follows:
    {"line": {"columns": ["A", "B", "C", ...], "data": [25, 24, 10, ...]}}
""" + question)
    # prompt = query.format(question=question)
    result = agent(question)
    print(result)
    # Create a Pandas DataFrame agent.
    # response = decode_response(result)
    st.write(result)


