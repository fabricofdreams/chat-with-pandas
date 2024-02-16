import pandas as pd
import numpy as np
import altair as alt
from config import DATA_URL, AUTHOR
import streamlit as st
from geopy.geocoders import Nominatim


@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL)
    data['Date'] = pd.to_datetime(
        data['Date'], format='mixed', utc=True).dt.date
    return data


def show_data():
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

    columns.pop(columns.index('Date'))

    data_selected_columns = st.sidebar.multiselect(
        'Select columns', columns)

    # Select time window
    st.sidebar.title("Sorting data")

    min_date = data['Date'].min()
    max_date = data['Date'].max()

    min_year = min_date.year
    max_year = max_date.year

    def get_range(): return np.array(range(min_year, max_year + 1))

    range_years = get_range()
    value = (min_year, max_year)

    st.sidebar.header('Sorting by years')

    year_range_selected = st.sidebar.select_slider(
        'Select range of years', options=range_years, value=value)

    min_year_selected = year_range_selected[0]
    max_year_selected = year_range_selected[1]

    min_date_selected = pd.to_datetime(
        str(min_year_selected) + '-01-01').date()
    max_date_selected = pd.to_datetime(
        str(max_year_selected) + '-12-31').date()

    # Display selected columns within the selected time window
    if len(data_selected_columns) > 0 and len(year_range_selected) > 0:
        data_selected_columns = ['Date'] + data_selected_columns
        st.subheader('Filtered and Sorted data')
        st.write("Data selected from year {min_year} to year {max_year}".format(
            min_year=min_year_selected, max_year=max_year_selected))

        filtered_data = data[(data['Date'] >= min_date_selected) &
                             (data['Date'] <= max_date_selected)]

        count_filtered_data_header = str(filtered_data.shape[0])

        st.write("Total number of rows filtered: ", count_filtered_data_header)

        st.write(filtered_data[data_selected_columns])

        # Tuple with selected columns
        selected_columns = tuple(data_selected_columns)

        # Chart area with selected columns
        st.sidebar.title("Graphs")
        feature_selected = st.sidebar.selectbox('Select feature to plot',
                                                options=selected_columns[1:], placeholder='Select a feature')

        # Create a figure
        st.subheader('Graphs')

        sorted_data = filtered_data[data_selected_columns]

        chart = pd.DataFrame(sorted_data)

        st.write("Feature selected: ", feature_selected)

        st.write("Max value: ", chart[feature_selected].max(axis=0))
        st.write("Min value: ", chart[feature_selected].min(axis=0))

        min_value = chart[feature_selected].min(axis=0)
        max_value = chart[feature_selected].max(axis=0)

        fig = (
            alt.Chart(chart)
            .mark_bar()
            .encode(x='Date', y=alt.Y(feature_selected,

                                      axis=alt.Axis(labels=True, labelColor='red', formatType='number'))))

        sorted_graph = st.altair_chart(
            fig, use_container_width=True, theme="streamlit")
        st.caption('This a graph created based on the filtered and sorted data.')

        return sorted_data


def get_country_name(latitude, longitude):
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.reverse((latitude, longitude), exactly_one=True)
    address = location.raw['address']
    country = address.get('country', '')
    return country
