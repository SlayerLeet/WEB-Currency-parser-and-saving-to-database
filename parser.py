import requests
from json import loads
from datetime import datetime

# Ссылки на валюты:
btc_url = 'https://www.okx.com/api/v5/public/mark-price?instId=BTC-USDT-SWAP'
eth_url = 'https://www.okx.com/api/v5/public/mark-price?instId=ETH-USDT-SWAP'
bnb_url = 'https://www.okx.com/api/v5/public/mark-price?instId=BNB-USDT-SWAP'

# Базовые данные:
result_dict = {}

# Парсинг с okx:
def okx_parse():
    for url in [btc_url, eth_url, bnb_url]:
        req = requests.get(url).text
        
        raw_data = loads(req).get("data")
        data = raw_data[0]
        
        raw_name = data.get('instId')
        raw_name1 = raw_name.split('-')
        name = raw_name1[0] + '/' + raw_name1[1]
        price = data.get('markPx')
        now = datetime.now()
        formatted_string_ru = now.strftime("%d.%m.%Y %H:%M")
        result_dict[name] = {"price" : price, "date" : formatted_string_ru}
        
    return result_dict
    
print(result_dict)


# Валюты которые парсю

# BTC-USDT-SWAP
# ETH-USDT-SWAP
# BNB-USDT-SWAP