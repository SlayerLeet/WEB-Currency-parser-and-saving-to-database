import requests
from bs4 import BeautifulSoup 

def norm():
    url = "https://www.finmarket.ru/currency/"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    
    values = {}

    block = soup.find_all('div', class_="fintool_button")
    
    for val in block:
        title = str(val.find('div', class_ = "title").text) + "/RUB"
        value = str(val.find('div', class_ = "value").text)
        values[title] = value
        
    return values

print(norm())