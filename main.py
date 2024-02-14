import streamlit as st
from config import AUTHOR
from get_data import load_data


def main():
    st.title("Earthquakes Data Analysis")
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.sidebar.text('Loading data...')
    # Load 10,000 rows of data into the dataframe.
    data = load_data(3)
    # Notify the reader that the data was successfully loaded.
    data_load_state.text("Dataset is loaded!")

    st.sidebar.title('About')
    st.sidebar.info(f'This app is created by {AUTHOR}')

    st.subheader('Raw data')
    st.dataframe(data)

    st.sidebar.title('Variables')

    # Select columns to display
    columns = data.columns.tolist()
    selected_columns = st.sidebar.multiselect('Select columns', columns)
    if len(selected_columns) > 0:
        st.subheader('Selected columns')
        st.write(data[selected_columns])


if __name__ == '__main__':
    main()
