# Querying csv data using SQL

This project uses Streamlit, a Python library for creating web applications, to perform data analysis on customer data. The analysis includes displaying column names and types, exploring the first 10 rows of the dataset, showing summary statistics, and allowing users to execute custom SQL queries on an in-memory SQLite database.

## How to Use

1. **Upload CSV File:**
   - Click the "Upload CSV file" button to upload your customer data in CSV format.

2. **Exploratory Data Analysis (EDA):**
   - View column names and types.
   - Explore the first 10 rows of the dataset.
   - Check summary statistics.

3. **Custom Queries:**
   - Enter custom SQL queries in the provided text area.
   - Execute the queries to see the results.

4. **Closing the App:**
   - The app automatically closes the SQLite connection upon completion.

## Dependencies

Make sure you have the required dependencies installed. You can install them using the following:

```bash
pip install streamlit pandas sqlite3
```

## How to Run

1. Save the provided code in a Python file (e.g., `customer_data_analysis.py`).
2. Open a terminal and navigate to the file's directory.
3. Run the following command:

```bash
streamlit run customer_data_analysis.py
```

4. The app will open in your default web browser.

## Contributing

Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests. Your feedback is highly appreciated.
