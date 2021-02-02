from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from letter_categories import letter_categories

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
url = 'http://progressivelabs.com/home.php'
r = requests.get(url, headers=headers)
html_content = r.text
soup = BeautifulSoup(html_content, 'lxml')

links = soup.find_all('a')
urls = []
base = 'http://progressivelabs.com/'

for link in links:
    fullLink = link.get('href')
    urls.append(urljoin(base, fullLink))

for link in range(urls.index('http://progressivelabs.com/home.php?letter=A')):
    urls.pop(0)

trash = urls.index('http://progressivelabs.com/cart.php')
for link in range(trash, len(urls)):
    urls.pop(trash)

for u in range(len(urls)):
    letter_categories(urls[u])

