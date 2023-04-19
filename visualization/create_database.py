import sqlite3
import pandas as pd

csv_file = 'data.csv'
db_file = 'data.db'

# Read the data from the CSV file
df = pd.read_csv(csv_file, parse_dates=['Date'])

# Convert the 'Date' column to a date-only format (without time component)
df['Date'] = df['Date'].dt.date

# Create a connection to the SQLite database
conn = sqlite3.connect(db_file)

# Write the DataFrame to the SQLite database
df.to_sql('data', conn, if_exists='replace', index=False)

# Close the connection to the SQLite database
conn.close()
