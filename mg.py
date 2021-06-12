import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver import Chrome
import os, time, json
from datetime import datetime


from selenium import webdriver

DRIVER_PATH = './drivers/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.1mg.com/drugs-all-medicines')
div = driver.find_element_by_class_name('style__chips___2T95q')

test = [a.get_attribute('href') for a in div.find_elements_by_tag_name('a')]

for i in test.items():
	current_page_number = 1
	driver.get(i)
	time.sleep(2)
	medicines = []
	page_limit = 200


	while True:
		medicines += self.get_medicines_on_page()
		if page_limit != None and current_page_number >= page_limit:
			break
		try:
			if self.click_on_next_page():
				time.sleep(7)
			else:
				print (f"Early stoppage")
				break
		except Exception as err:
			print (f'Failed to find new page: {err}')
			break

def click_on_next_page(self):
		ul = self._driver.find_element_by_class_name('pagination')
		a_eles = ul.find_elements_by_tag_name('a')
		for a in a_eles:
			if a.text == str(self._current_page_number + 1):
				a.click()
				self._current_page_number += 1
				return True
		return False
def run(self, categories, page_limit=None):
		line = 'X' + '-' * 20 + 'X'
		count = 0
		total_cats = len(categories)
		unnamed = 0
		for category, link in categories.items():
			self._current_page_number = 1
			print (line)
			print (f"Starting Category: {category}; {count + 1} / {total_cats}")
			self.get(link)
			medicines = []

			while True:
				print (f"---- [+] Category {count + 1}; Page Number: {self._current_page_number}")
				medicines += self.get_medicines_on_page()
				if page_limit != None and self._current_page_number >= page_limit:
					break

				try:
					if self.click_on_next_page():
						time.sleep(7)
					else:
						print (f"Early stoppage")
						break
				except Exception as err:
					print (f'Failed to find new page: {err}')
					break
