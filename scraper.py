import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver import Chrome
import os, time, json
from datetime import datetime
import mysql.connector
db = mysql.connector.connect (host = "10.176.144.15",
                              user = "devmedstore",
                              passwd = "uapL6{9h?",
                              db = "dev",
                              port = 3306)


driver_path='./drivers/chromedriver'
cursor = db.cursor(buffered=True)

driver = Chrome(driver_path)

url = "https://www.medplusmart.com/pharmaHome"
driver.get(url)
div = driver.find_element_by_class_name('drugsCategory')

new_dic = [a.get_attribute('href') for a in div.find_elements_by_tag_name('a')]
count = 117
for i in new_dic[125:]:
	print(i)
	driver.get(i)
	time.sleep(2)
	condition = True
	while(condition):
		try:
			time.sleep(2)
			list1 = driver.find_elements_by_tag_name("tr")
			list2 = driver.find_elements_by_class_name("searchResultProductName")
			list1.pop(0)
			list1.pop(-1)
			list1.pop(-1)
		except: 
			continue
		for k,l in zip(list1,list2):
			#TabName = k.find_element_by_class_name("searchResultProductName")
			#print(TabName)
			try:
				tempList = [ele.text for ele in k.find_elements_by_class_name("hidden-xs")]

				MedName = l.text
				Manu = tempList[1]
				Comp = tempList[0]
				Comp = Comp.replace('Comp: ','')
				Mrp = tempList[3]

				print(MedName)
				print(Manu)
				print(Comp)
				print(Mrp)
				print(count)
				print("\n")
				sql = "INSERT INTO medicine_medplus (product_name,product_company,product_price,composition,mapping) VALUES (%s, %s, %s, %s,%s)"
				cursor.execute(sql,(MedName,Manu,Mrp,Comp,count))
			except:
				continue
		try:
			temp = driver.find_element_by_class_name("pagination")
			tem1 = temp.find_elements_by_tag_name("a")
			if(tem1[-2].get_attribute("onclick")):
				tem1[-2].click()
				time.sleep(5)
			else:
				condition = False
		except:
			condition = False

	try:
  		db.commit()
	except:
  		db.rollback()
	count = count + 1
db.close()


	



