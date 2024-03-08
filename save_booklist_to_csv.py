import csv
import requests
from bs4 import BeautifulSoup

def get_booklist():
	base_url = "https://standardebooks.org/ebooks?page={}&per-page=48"
	booklist = []
	for page_number in range(1, 21):
		url = base_url.format(page_number)
		response = requests.get(url)
		if response.status_code == 200:
			soup = BeautifulSoup(response.text, 'html.parser')
			
			for li in soup.find_all('li', {'typeof': 'schema:Book'}):
				url = li.find('p').find('a')['href']
				book_title = li.find('p').find('span').text
				author_p = li.find_all('p')[1]
				if author_p and author_p.find('span'):
					book_author = author_p.find('span').text
				else:
					book_author = "anonymous"
				row = [book_author, book_title, url]
				booklist.append(row)
				print(row)
			print(len(booklist))
		else:
			print(f"Failed to fetch page {page_number}")
	return booklist

filename = 'standardebooks.csv'
delimiter = '|'
booklist = get_booklist()
with open(filename, 'w', newline='') as csvfile:
	writer = csv.writer(csvfile, delimiter=delimiter)
	# write to csv file in reverse order
	writer.writerows(booklist[::-1])
