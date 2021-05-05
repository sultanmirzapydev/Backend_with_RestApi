import requests
from bs4 import BeautifulSoup as bs4
import re
import itertools
import json

def soupy():
	URL = 'https://unsplash.com/s/photos/dog'

	page = requests.get(URL)

	soup = bs4(page.content, 'html5lib')

	# for name
	uploader_name_tags = soup.select('._3XzpS')[:15]
	uploader_names_list = []
	for name in uploader_name_tags:
		data = name.get_text()
		uploader_names_list.append(data)

	# for images
	main_images = soup.find_all('img', class_='_2UpQX')[:15]
	main_images_list = []
	for singleimage in main_images:
		links = singleimage['src']
		main_images_list.append(links)

	# for profile pics
	profile_pics = soup.find_all('img', class_='_1FdcY')[:15]
	profile_pics_list = []
	for singlepics in profile_pics:
		pic = singlepics['src']
		profile_pics_list.append(pic)

	scrap_data = []

	for (name,image,profilepic) in zip(uploader_names_list,main_images_list, profile_pics_list):
		object = {
		'name':name,
		'image':image,
		'profilepic':profilepic
		}
		scrap_data.append(object)

	return scrap_data;

