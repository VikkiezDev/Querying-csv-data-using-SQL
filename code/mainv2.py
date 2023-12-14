import streamlit as st
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt

# Disable the warning about deprecated use of pyplot globally
st.set_option('deprecation.showPyplotGlobalUse', False)

# Set up matplotlib style
plt.style.use('fivethirtyeight')

# Streamlit app starts here
st.title("Customer Data Analysis")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV data
    customer_data = pd.read_csv(uploaded_file)

    # Create an in-memory SQLite database
    conn = sqlite3.connect(":memory:")

    # Add data to the SQLite database
    customer_data.to_sql("customer_data", conn, index=False, if_exists="replace")

    # Display column names and types
    st.subheader("Columns and Types:")
    query_columns = "PRAGMA table_info(customer_data);"
    columns_info = pd.read_sql_query(query_columns, conn)
    st.dataframe(columns_info)

    # Exploratory Data Analysis (EDA)
    st.subheader("Exploratory Data Analysis (EDA):")

    # Display first 10 rows of the dataset
    st.subheader("First 10 Rows:")
    query_first_10_rows = "SELECT * FROM customer_data LIMIT 10;"
    first_10_rows = pd.read_sql_query(query_first_10_rows, conn)
    st.dataframe(first_10_rows)

    # Summary statistics table
    st.subheader("Summary Statistics:")
    query_summary_stats = "SELECT * FROM customer_data;"
    summary_stats = pd.read_sql_query(query_summary_stats, conn)
    st.dataframe(summary_stats.describe())

    # User input for custom queries
    st.subheader("Custom Queries:")
    custom_query = st.text_area("Enter your custom SQL query:")

    # Execute user's SQL query
    try:
        if custom_query:
            result = pd.read_sql_query(custom_query, conn)
            st.subheader("Query Result:")
            st.dataframe(result)
    except Exception as e:
        st.error(f"Error executing query: {e}")


    # Close the SQLite connection
    conn.close()

else:
    st.warning("Please upload a CSV file.")