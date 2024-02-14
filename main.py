import streamlit as st
from config import AUTHOR
from get_data import load_data
import pandas as pd


def main():
    st.title("Earthquakes Data Analysis")
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.sidebar.text('Loading data...')
    # Load data into the dataframe.
    data = load_data()
    # Notify the reader that the data was successfully loaded.
    data_load_state.text("Dataset is loaded!")

    st.sidebar.title('About')
    st.sidebar.info(f'This app is created by {AUTHOR}')

    # Display the raw data
    st.subheader('Raw data')
    data_header = data.head()
    st.write(data_header)

    # Select columns to display
    st.sidebar.title('Variables')
    columns = data.columns.tolist()
    data_selected_columns = st.sidebar.multiselect('Select columns', columns)

    if len(data_selected_columns) > 0:
        st.subheader('Selected columns')
        st.write(data[data_selected_columns])

    # Select time window
    dates = pd.to_datetime(data['date'], format='mixed', utc=True)
    min_year = dates.min().date().year
    max_year = dates.max().date().year
    st.sidebar.title('Time window')

    st.sidebar.write(f'Min year: {min_year}')
    st.sidebar.write(f'Max year: {max_year}')

    year_selected = st.sidebar.slider('Year', min_year, max_year, 2010)

    # Display selected columns within the selected time window
    st.subheader('Selected columns within the selected time window')
    st.write("Data selected from year {year_selected} to year {max_year}".format(
        year_selected=year_selected, max_year=max_year))

    filtered_data = data[data['date'].str.contains(str(year_selected))]

    st.write(filtered_data[data_selected_columns])
    count_filtered_data_header = filtered_data.shape[0]
    st.write("Total number of rows: ", count_filtered_data_header)


if __name__ == '__main__':
    main()
