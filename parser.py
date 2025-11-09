import requests
from json import loads
from datetime import datetime

#------------------------------------------------------------------------------------------------------------------------------------------------
# OKX

# Базовые данные:
result_dict = {}

def okx_parse():
    
    # Ссылки на валюты:
    btc_url = 'https://www.okx.com/api/v5/public/mark-price?instId=BTC-USDT-SWAP'
    eth_url = 'https://www.okx.com/api/v5/public/mark-price?instId=ETH-USDT-SWAP'
    bnb_url = 'https://www.okx.com/api/v5/public/mark-price?instId=BNB-USDT-SWAP'
    
    # Парсинг с okx:
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

# Валюты которые парсю

# BTC-USDT-SWAP
# ETH-USDT-SWAP
# BNB-USDT-SWAP
#------------------------------------------------------------------------------------------------------------------------------------------------

# BINANCE

# Базовые данные:
binance_dict = {}


def binance_parse():
    
    # Ссылки на валюты:
    btc_url = 'https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT'
    eth_url = 'https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT'
    bnb_url = 'https://api.binance.com/api/v3/avgPrice?symbol=BNBUSDT'
    
    # Парсинг с okx:
    for url, name in zip([btc_url, eth_url, bnb_url], ['BTC/USDT','ETH/USDT','BNB/USDT']):
        req = requests.get(url).text
        
        price = loads(req).get("price")

        now = datetime.now()
        formatted_string_ru = now.strftime("%d.%m.%Y %H:%M")
        binance_dict[name] = {"price" : price, "date" : formatted_string_ru}
        
    return binance_dict

print(okx_parse())
print(binance_parse())

# BTC-USDT
# ETH-USDT
# BNB-USDT
#------------------------------------------------------------------------------------------------------------------------------------------------