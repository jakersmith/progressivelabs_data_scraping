

def item_info(hyperlink):
    # Import statements, just in case
    from bs4 import BeautifulSoup
    import requests
    import csv

    base = 'http://progressivelabs.com/'
    headers2 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
    url = hyperlink
    r2 = requests.get(url, headers=headers2)
    html_content2 = r2.text
    soup2 = BeautifulSoup(html_content2, 'html.parser')


    # Removes everything EXCEPT the name of the product
    title_full = soup2.title.text
    title = title_full.split('::')[-1]



    # This removes the <div> tags from the str
    div = str(soup2.find("div", {"id": "productdescr"}))
    div = div[27:]
    div = div[:-6:]

    company = 'Progressive Labs'


    # This block writes the TITLE and DESCRIPTION to the CSV
    with open('ProgressiveLabsProducts.csv', 'a', encoding="utf-8", newline='') as f:
        thewriter = csv.writer(f)

        thewriter.writerow([title, div, company])
        f.flush()
    f.close()
