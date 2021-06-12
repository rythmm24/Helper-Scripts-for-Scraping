import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as bs
import ssl

# --- ignore ssl certificate ---
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.medplusmart.com/drugsCategory/medicines'
html = urllib.request.urlopen(url, context=ctx).read() 
page = requests.get(URL)

soup = bs(html, 'html.parser') 
media_list = soup.find_all('div', class_='drugsCategory')

print(media_list)

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
