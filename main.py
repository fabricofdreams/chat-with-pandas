import streamlit as st
from config import AUTHOR
from get_data import load_data
import pandas as pd
import numpy as np
import altair as alt


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

        chart = pd.DataFrame(filtered_data[data_selected_columns])

        fig = (
            alt.Chart(chart)
            .mark_bar()
            .encode(x='Date', y=alt.Y(str(feature_selected)+':Q')))

        st.altair_chart(fig, use_container_width=True)


if __name__ == '__main__':
    main()
