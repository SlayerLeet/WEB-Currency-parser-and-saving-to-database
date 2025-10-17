import sqlite3
import time
from parser_binance import cripta
from parser_moex import moex

# Создание базы данных
def create_db():
    db = sqlite3.connect(r'data/exchange_rates.db')
    c = db.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS fiat_currency
    (
        title text,
        price real,
        date text
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS crypto_currency
        (
        title text,
        price real,
        date text
    )""")

    db.commit()
    db.close()
    
    
# Добавлние курса валют с биржи moex
def moex_db():
    db = sqlite3.connect(r'data/exchange_rates.db')
    c = db.cursor()
    
    values = moex()
    
    for name, value in values.items():
        price = value.get("price")
        date = value.get("date")
        c.execute('INSERT INTO fiat_currency (title, price, date) VALUES (?, ?, ?)', (name, price, date))
    
    db.commit()
    db.close()
    
    
# Добавлние курса валют с биржи binance
def binance_db():  
    db = sqlite3.connect(r'data/exchange_rates.db')
    c = db.cursor()
    
    values = cripta()
    
    for name, value in values.items():
        price = value.get("price")
        date = value.get("date")
        c.execute('INSERT INTO crypto_currency (title, price, date) VALUES (?, ?, ?)', (name, price, date))
    
    db.commit()
    db.close()
    
    
# Отприсовка данных которые содержаться в db
def draw():
    db = sqlite3.connect(r'data/exchange_rates.db')
    c = db.cursor()

    c.execute("SELECT * FROM fiat_currency")  
    print(c.fetchall())  
    print()
    print()
    c.execute("SELECT * FROM crypto_currency")  
    print(c.fetchall())  
    print()
    print()
    print()
    print()
    print()

    db.commit()
    db.close()    
      
      
# Главный цикл
def main():
    create_db()
    while True:
        moex_db()
        binance_db()
        draw()
        # Частота обновления информации в секунду
        time.sleep(5)
main()


