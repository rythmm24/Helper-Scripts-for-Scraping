from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import os, time, json

DRIVER_PATH = './drivers/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url = "https://www.medplusmart.com/brands"
driver.get(url)


cat = driver.find_elements_by_class_name('brandlist-inline')

for i in cat:
	t = i.find_elements_by_tag_name('a')
	for j in t:
		link = j.get_property('href')
		print(link)
		try:
			drivern = webdriver.Chrome(executable_path=DRIVER_PATH)
			drivern.get(link)
			time.sleep(5)
			condition = True
			while condition:
				time.sleep(2)
				t = driver.find_elements_by_class_name('cursor')
				for i in t:
					print(i.text)
					print("\n")

				try:
					temp = driver.find_element_by_class_name("pagination")
					i = temp.find_elements_by_tag_name("a")
					if(i[-2].get_attribute("onclick")):
						i[-2].click()
					else:
						condition = False
				except:
					condition = False

		except: 
			print("Error")






'''


condition = True
while condition:
	time.sleep(5)
	t = driver.find_elements_by_class_name('style__flex-1___A_qoj')
	for i in t:
		print(i.find_elements_by_tag_name("div")[3].text)
		print(i.find_elements_by_tag_name("div")[8].text)
	break	
	time.sleep(2)
	try:
		print("reached here")
		temp = driver.find_element_by_xpath("""//*[@id="container"]/div/div/div[2]/ul/li[8]/a""").click()
		print(temp)
	except:
		condition = False'''

