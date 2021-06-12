from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import os, time, json


URL = 'https://www.1mg.com/drugs-therapeutic-classes'
page = requests.get(URL)
soup = bs(page.content, 'html.parser')
temp = []
link = soup.find_all("a")
for i in link:
	if "drugs-therapeutic-classes/" in i.attrs['href']:
		temp.append(i.attrs['href'])

'''
for url in temp:
	url = "https://www.1mg.com"+ url
	driver.get(url)
	
	condition = True
	while condition:
		time.sleep(5)
		t = driver.find_elements_by_class_name('style__flex-1___A_qoj')
		for i in t:
			temp = i.find_elements_by_tag_name("div")[0].text
			print(temp)
		
		time.sleep(2)
		try:
			driver.find_element_by_xpath("""//*[@id="container"]/div/div/div[2]/ul/li[8]/a""").click()
		except:
			condition = False

	'''
