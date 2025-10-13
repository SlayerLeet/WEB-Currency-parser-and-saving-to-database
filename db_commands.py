import sqlite3


db = sqlite3.connect(r'data/exchange_rates.db')


c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS fiat_currency
(
    title text,
    price real,
    date date
)
""")


c.execute("""CREATE TABLE IF NOT EXISTS crypto_currency
    (
    title text,
    price real,
    date date
)
""")


db.commit()

db.close()

# crypto_currency