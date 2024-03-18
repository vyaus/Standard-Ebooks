import sqlite3
import os
import requests
from urllib.parse import urljoin

from random import randint
from time import sleep

# Connect to the SQLite database
# Replace 'your_database.db' with the path to your SQLite database file
conn = sqlite3.connect('standardebooks.db')
cursor = conn.cursor()

# Query to select author, title, and URL from your table
# Replace 'your_table_name' with the name of your table
query = "SELECT author, title, url FROM booklist"
cursor.execute(query)
book_format = ['epub', 'azw3', 'kepub.epub', 'advanced.epub']
# Base URL for downloading the books
base_url = "https://standardebooks.org"
book_id = 1
for row in cursor.fetchall():
	author, title, path_url = row
	# Construct the book URL by replacing slashes with underscores and appending the format
	book_url = '_'.join(path_url.split('/')[2:])
	format = book_format[0]
	download_url = urljoin(base_url, f"{path_url}/downloads/{book_url}.{format}")
	
	# Create the directory if it does not exist
	directory = f"{author}/{title}"
	os.makedirs(directory, exist_ok=True)
	# Create the file name for the downloaded book
	filename = f"{title} - {author}.{format}"
	filepath = os.path.join(directory, filename)
	
	if not os.path.isfile(filepath):
		# Download the book if it does not exist
		response = requests.get(download_url, stream=True)
		if response.status_code == 200:
			# Save the file
			with open(os.path.join(directory, filename), 'wb') as f:
				for chunk in response.iter_content(chunk_size=8192):
					if chunk:
						f.write(chunk)
			print(f"{book_id} Downloaded {filename}")
			sleep(randint(2,5))
		else:
			print(f"Failed to download {filename}. Status code: {response.status_code}")
	book_id += 1

# Close the database connection
conn.close()

