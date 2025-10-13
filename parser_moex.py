import json
import requests
import re
from datetime import datetime

def moex():
    url = ("https://iss.moex.com/iss/engines/currency/markets/selt/securities.jsonp?"
        "iss.only=securities,marketdata&"
        "securities=CETS:USD000UTSTOM,CETS:EUR_RUB__TOM,CETS:CNYRUB_TOM,CETS:GBPRUB_TOM&"
        "lang=ru&iss.meta=off&iss.json=extended&callback=angular.callbacks._gk")
    data = requests.get(url)


    text = data.text[22:len(data.text)-1:]
    text = re.sub(r'\n', "", text)
    json_string = json.loads(text)

    
    moex_dict = {}
    for ss in json_string[1]['marketdata']:
        if ss['SECID'] != "GBPRUB_TOM":
            name = ss['SECID'][:3] + '/RUB'
            now = datetime.now()
            formatted_string_ru = now.strftime("%d.%m.%Y %H:%M")
            if str(ss['CLOSEPRICE']) == "None":
                price = ss['MARKETPRICE2']
            else:
                price = ss['CLOSEPRICE']
        else:
            continue
        moex_dict[name] = {"price" : price, "date" : formatted_string_ru}

        
    return moex_dict
print(moex())