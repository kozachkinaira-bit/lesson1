import requests

html = requests.get("http://books.toscrape.com/").text

parced_text = html.split('<p class="price_color">')

for text in parced_text:
    if "£" in text:
        price_text = text.split('</p>')
        for price in price_text:
            if "£" in price:
                print(price[1:])





