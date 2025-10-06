import sqlite3


db = sqlite3.connect(r'data/exchange_rates.db')


c = db.cursor()

c.execute("""CREATE TABLE fiat_currency
          
          
          
          
          """)


db.close()

# crypto_currency