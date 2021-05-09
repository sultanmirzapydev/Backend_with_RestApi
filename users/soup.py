import requests 
from bs4 import BeautifulSoup as bs4
import os


def scrap(requests, search_for):
	URL = f'https://unsplash.com/s/photos/{search_for}'
	page = requests.get(URL)


	soup = bs4(page.content, 'html5lib')
	
	img = soup.find_all('img', class_='_2UpQX')[:24]
	
	data = []
	

	for item in img:
		a = item['srcset']
		
		#name,ext = os.path.splitext(a)
		
		#if ext == '.jpg':
		#b = f'https://www.hdwallpapers.in{a}'
		data.append(a)
	return data;
