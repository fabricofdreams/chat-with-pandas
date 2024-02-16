import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
from ai_functions import *
import pandas as pd


def chat_with_pd(user_csv):
    # Session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content='Hi! How can I help you?')
        ]
    # if "vectorstore" not in st.session_state:
    #     st.session_state.vectorstore = get_vectorstore_from_url(website_url)

    # User input
    user_query = st.chat_input('Type your message here...')

    if user_query is not None and user_query != '':
      # Agent
        llm = ChatOpenAI(temperature=0.2, model="gpt-3.5-turbo-0613")
        agent = create_pandas_dataframe_agent(
            llm, user_csv, verbose=True, agent_type=AgentType.OPENAI_FUNCTIONS)

        response = agent.run(user_query)
        st.session_state.chat_history.append(HumanMessage(content=user_query))
        st.session_state.chat_history.append(AIMessage(content=response))

    # Conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message('AI'):
                st.write(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message('Human'):
                st.write(message.content)
