import os
from dotenv import load_dotenv
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

load_dotenv()

#langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Q&A_chatot_with_LLAMA"

#prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are helpful assistant. please respond to the question asked"),
        ("user","question:{question}")
    ]
)
#OLLAMA MOdel

def generate_response(question,temprature,max_tokens):
    llm=Ollama(model="llama3.2:1b")
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer
    
#title of the app
st.title("Langchain Q&A Chatbot with LLAMA")
#sidebars
st.sidebar.title("Settings")
#sidebar for setting
temprature=st.sidebar.slider("Temprature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Token",min_value=50,max_value=300,value=150)

#interface
st.write("Ask me a question")
user_input= st.text_input("You:")



if user_input:
    response=generate_response(user_input,temprature,max_tokens)
    st.write(response)

else:
    st.write("please provide query")
