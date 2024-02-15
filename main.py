import streamlit as st
from config import AUTHOR
from get_data import load_data
import pandas as pd
import numpy as np


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
    st.sidebar.title("Filtering data")
    columns = data.columns.tolist()
    data_selected_columns = st.sidebar.multiselect('Select columns', columns)

    if len(data_selected_columns) > 0:
        st.subheader('Selected columns')
        st.write(data[data_selected_columns])

    # Select time window
    st.sidebar.title("Sorting data")
    data['Date'] = pd.to_datetime(data['Date'], format='mixed', utc=True)

    min_date = data['Date'].min()
    max_date = data['Date'].max()

    min_year = min_date.date().year
    max_year = max_date.date().year

    def get_range(): return np.array(range(min_year, max_year + 1))

    range_years = get_range()
    value = (min_year, max_year)

    st.sidebar.header('Sorting by years')

    year_range_selected = st.sidebar.select_slider(
        'Select range of years', options=range_years, value=value)

    min_year_selected = year_range_selected[0]
    max_year_selected = year_range_selected[1]

    # Display selected columns within the selected time window
    st.subheader('Selected columns within the selected time window')
    st.write("Data selected from year {min_year} to year {max_year}".format(
        min_year=min_year_selected, max_year=max_year_selected))

    filtered_data = data[(data['Date'] >= str(min_year_selected)) &
                         (data['Date'] <= str(max_year_selected))]

    st.write(filtered_data[data_selected_columns])
    # count_filtered_data_header = filtered_data.shape[0]
    # st.write("Total number of rows: ", count_filtered_data_header)


if __name__ == '__main__':
    main()
