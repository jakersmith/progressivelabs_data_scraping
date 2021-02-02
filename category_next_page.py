
def next_page(hyperlink):

    from bs4 import BeautifulSoup
    import requests
    from urllib.parse import urljoin
    import re
    import items

    base = 'http://progressivelabs.com/'
    headers2 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    url = hyperlink
    r2 = requests.get(url, headers=headers2)
    html_content2 = r2.text
    soup2 = BeautifulSoup(html_content2, 'lxml')

    links2 = soup2.find_all('a')
    urls2 = []

    for link in links2:
        fullLink = link.get('href')
        urls2.append(urljoin(base, fullLink))


    trash2 = urls2.index('http://progressivelabs.com/cart.php?mode=checkout')
    for u in range(trash2 + 1):
        urls2.pop(0)

    sub_product = 'productid='
    products = [x for x in urls2 if re.search(sub_product, x)]
    products = list(dict.fromkeys(products))

    for u in range(len(products)):
        items.item_info(products[u])

