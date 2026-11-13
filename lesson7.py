import requests

coin_cap_text = requests.get("https://coinmarketcap.com").text

parse_text = coin_cap_text.split('<span>')

for text in parse_text:
    if text.startswith('$'):
        print(text)

        
#currencies = requests = requests.get("https://api.monobank.ua/bank/currency").json

#print(currencies)