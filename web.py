import requests
from bs4 import BeautifulSoup as bs


URL = 'https://www.medplusmart.com/brands'
page = requests.get(URL)
soup = bs(page.content, 'html.parser')
temp = []
print(soup.prettify())
link = soup.find_all("a")
for i in link:
	temp.append(i.attrs['href'])
print(temp)