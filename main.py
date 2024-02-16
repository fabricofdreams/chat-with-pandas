import streamlit as st
from get_data import show_data
from dotenv import load_dotenv
from chat_with_data import chat_with_pd


def main():

    load_dotenv()

    st.title("Earthquakes Data Analysis")
    # Get, filter and sort data
    data_to_chat_with = show_data()

    if data_to_chat_with is None:
        st.write("No data to chat with")
    else:
        st.write("Data to chat with is ready!")

        # Chat with data
        st.subheader("Chat with the Filtered Data")
        chat_with_pd(data_to_chat_with)


if __name__ == '__main__':
    main()
