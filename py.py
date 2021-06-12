import requests 
from bs4 import BeautifulSoup as bs
import re
import mysql.connector
db = mysql.connector.connect (host = "10.176.144.15",
                              user = "devmedstore",
                              passwd = "uapL6{9h?",
                              db = "dev",
                              port = 3306)

cursor = db.cursor(buffered=True)
URLAPI = "https://www.1mg.com/pharmacy_api_gateway/v4/drug_skus/by_therapeutic_class_id" 

URL = 'https://www.1mg.com/drugs-therapeutic-classes'
page = requests.get(URL)
soup = bs(page.content, 'html.parser')
temp = []
link = soup.find_all("a")
for i in link:
	if "drugs-therapeutic-classes/" in i.attrs['href']:
		temp.append(i.attrs['href'])
mapping = 1
for j in temp:
	tid = int(re.search(r'\d+', str(j)).group())
	therapeutic_class_id = tid
	print(tid)
	per_page = 40
	page=1
	condition = True
	while condition:

		PARAMS = {'per_page':per_page, 'page':page, 'therapeutic_class_id':therapeutic_class_id}   
		r = requests.get(url = URLAPI, params = PARAMS) 
		data = r.json() 
		t = data['data']['skus']
		
		page = page + 1
		if(len(t)==0):
			condition = False

		for i in t:
			manuName = i['manufacturer_name']
			medName = i['name']
			price = i['price']
			composition = i['short_composition']
			print(medName)
			print(manuName)
			print(composition)
			print(price)
			print('\n')
			sql = "INSERT INTO medicine1mg (product_name,product_company,product_price,composition,mapping) VALUES (%s, %s, %s, %s,%s)"
			cursor.execute(sql,(medName,manuName,float(price),composition,mapping,))

		print(len(t))
		print(page)
	mapping = mapping+1
try:
# Execute the SQL command
# Commit your changes in the database
  db.commit()
except:
# Rollback in case there is any error
  db.rollback()

# disconnect from server
db.close()




