import csv
import sqlite3
import os

# Step 1: Connect to SQLite Database
db_filepath = 'standardebooks.db'
connection = sqlite3.connect(db_filepath)
cursor = connection.cursor()

# Step 2: Create Table in SQLite Database
table_name = 'booklist'
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {table_name} (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	author TEXT NOT NULL,
	title TEXT NOT NULL,
	url TEXT NOT NULL
);
""")

# Step 3: Read CSV File and Insert Data into SQLite Table
csv_filepath = 'standardebooks.csv'

with open(csv_filepath, 'r') as csvfile:
	csvreader = csv.reader(csvfile, delimiter='|')
#	next(csvreader) # Skip the header row
	for row in csvreader:
		cursor.execute(f"INSERT INTO {table_name} (author, title, url) VALUES (?, ?, ?)", row)

# Step 4: Close the Connection
connection.commit()
connection.close()

