import asyncio
import httpx
import re
import json
from datetime import datetime

# Валюты
OKX_PAIRS = ["BTC-USDT-SWAP", "ETH-USDT-SWAP", "BNB-USDT-SWAP"]
BINANCE_PAIRS = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
BINANCE_NAMES = ["BTC/USDT", "ETH/USDT", "BNB/USDT"]
MOEX_SECURITIES = ["CETS:USD000UTSTOM", "CETS:EUR_RUB__TOM", "CETS:CNYRUB_TOM"]

#-------------------------------------------------------------------
# OKX
async def fetch_okx(start_id=0):
    async with httpx.AsyncClient(timeout=10) as client:
        tasks = [client.get(f'https://www.okx.com/api/v5/public/mark-price?instId={p}') for p in OKX_PAIRS]
        responses = await asyncio.gather(*tasks)

    results = []
    for i, resp in enumerate(responses):
        data = resp.json()["data"][0]
        name = data["instId"].replace("-", "/")[:8]
        price = round(float(data["markPx"]), 4)
        now = datetime.now().strftime("%d.%m.%Y %H:%M")
        results.append({"id": start_id + i, "exchange": "okx", "name": name, "price": price, "date": now})
    return results

#-------------------------------------------------------------------
# BINANCE
async def fetch_binance(start_id=0):
    async with httpx.AsyncClient(timeout=10) as client:
        tasks = [client.get(f'https://api.binance.com/api/v3/avgPrice?symbol={p}') for p in BINANCE_PAIRS]
        responses = await asyncio.gather(*tasks)

    results = []
    for i, resp in enumerate(responses):
        price = round(float(resp.json()["price"]), 4)
        now = datetime.now().strftime("%d.%m.%Y %H:%M")
        results.append({"id": start_id + i, "exchange": "binance", "name": BINANCE_NAMES[i], "price": price, "date": now})
    return results

#-------------------------------------------------------------------
# MOEX (синхронно, в отдельном потоке)
def fetch_moex(start_id=0):
    url = ("https://iss.moex.com/iss/engines/currency/markets/selt/securities.jsonp?"
           "iss.only=securities,marketdata&"
           "securities=" + ",".join(MOEX_SECURITIES) + "&"
           "lang=ru&iss.meta=off&iss.json=extended&callback=angular.callbacks._gk")
    r = httpx.get(url)
    text = r.text[22:-1].replace("\n", "")
    data = json.loads(text)

    results = []
    id_counter = start_id
    for ss in data[1]["marketdata"]:
        if ss["SECID"] in ["GBPRUB_TOM"]:
            continue
        price = ss["CLOSEPRICE"] if ss["CLOSEPRICE"] is not None else ss["MARKETPRICE2"]
        if isinstance(price, int):
            price = float(round(price, 2))
        now = datetime.now().strftime("%d.%m.%Y %H:%M")
        results.append({"id": id_counter, "exchange": "moex", "name": ss["SECID"][:3]+"/RUB", "price": float(price), "date": now})
        id_counter += 1
    return results

#-------------------------------------------------------------------
# Главная функция — параллельный запуск всех бирж
async def main_parse():
    # MOEX запускаем в отдельном потоке, чтобы не блокировать asyncio
    moex_task = asyncio.to_thread(fetch_moex, 0)
    okx_task = fetch_okx(0)
    binance_task = fetch_binance(len(OKX_PAIRS))

    results = await asyncio.gather(moex_task, okx_task, binance_task)

    # Объединяем результаты
    all_data = []
    for part in results:
        all_data.extend(part)

    # Ставим сквозной id
    for i, item in enumerate(all_data):
        item["id"] = i

    return all_data

#-------------------------------------------------------------------
# Тестовый запуск вне FastAPI
if __name__ == "__main__":
    data = asyncio.run(main_parse())
    for item in data:
        print(item)
