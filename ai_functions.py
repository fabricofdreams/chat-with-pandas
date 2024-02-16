from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
import streamlit as st


def get_response(user_input):
    return "Yes!, I'm ready to chat."


def get_vectorstore_from_url(url):
    # Content in document format
    loader = WebBaseLoader(url)
    document = loader.load()

    # Split document into chunks
    text_splitter = RecursiveCharacterTextSplitter()
    document_chunks = text_splitter.split_documents(document)

    # Create a vectorstore from the chunks
    vectorstore = Chroma.from_documents(document_chunks, OpenAIEmbeddings())

    return vectorstore


def get_context_retriever_chain(vectorstore):
    llm = ChatOpenAI()

    retriever = vectorstore.as_retriever()

    prompt = ChatPromptTemplate.from_messages([
        MessagesPlaceholder(variable_name='chat_history'),
        ("user", "{input}"),
        ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation."),
    ])

    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

    return retriever_chain


def get_conversational_rag_chain(retriever_chain):
    llm = ChatOpenAI()

    prompt = ChatPromptTemplate.from_messages([
        "System", "Answer the user's questions based on the below context:\n\n{context}",
        MessagesPlaceholder(variable_name='chat_history'),
        ("user", "{input}"),
    ])

    stuff_documents_chain = create_stuff_documents_chain(llm, prompt)

    return create_retrieval_chain(retriever_chain, stuff_documents_chain)


def get_response(user_input, chat_history, user_query):
    retriever_chain = get_context_retriever_chain(st.session_state.vectorstore)
    conversation_rag_chain = get_conversational_rag_chain(retriever_chain)
    # chat_history =st.session_state.chat_history
    response = conversation_rag_chain.invoke({
        "chat_history": chat_history,
        "input": user_query,
    })

    return response['answer']
