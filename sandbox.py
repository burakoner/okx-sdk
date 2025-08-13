# Copy .pypirc file to home directory. e.g.: C:\Users\{UserName}\.pypirc
# pip install setuptools
# pip install twine
# python -m build

# cd "E:\Github\okx-sdk"
# python setup.py sdist bdist_wheel
# python -m twine upload dist/*

import asyncio
import json
from okx import *
# from okx import OkxRestClient
# from okx import OkxSocketClient

# api = OkxRestClient("2ca75ca7-005f-47e6-84df-1e367eec17c2", "5EE5DFF9DA0EF9E82E402ED1AABEC51F", "bo1144167AZ*")
# result = api.public.get_tickers(instType="SPOT")
# print(result)

# result = api.account.get_account_balance()
# print(result)

def ws_handler(text):
    data = json.loads(text)
    
    if("event" in data):
        if(data["event"] == "subscribe"):
            print("Subscribed")
            return
        if(data["event"] == "unsubscribe"):
            print("Unsubscribed")
            return
    
    if("arg" in data and "channel" in data["arg"]):
        channel = data["arg"]["channel"]
        symbol = data["arg"]["instId"]
        if(channel == "tickers"):
            ticker = data["data"][0]
            print("[TICKER] Symbol:"+ ticker["instId"] +" Open:"+ ticker["open24h"] +" High:"+ ticker["high24h"] +" Low:"+ ticker["low24h"] +" Last:"+ ticker["last"] +" Volume:"+ ticker["vol24h"])
        elif(channel == "trades"):
            trade = data["data"][0]
            print("[TRADE] Symbol:"+ trade["instId"] +" Price:"+ trade["px"] + " Quantity:"+ trade["sz"])
        elif(channel.startswith("candle")):
            candle = data["data"][0]
            print("[CANDLE] Symbol:"+ symbol +" Open:"+ candle[1] +" High:"+ candle[2] +" Low:"+ candle[3] +" Close:"+ candle[4] +" Volume:"+ candle[5])
        else:
            print(f"[UNKNOWN] {text}")

async def tickers():
    ws = OkxSocketClient()
    await ws.public.start()
    await ws.public.subscribe([{'channel': "tickers", 'instId': "BTC-USDT"}], callback=ws_handler)

async def trades():
    ws = OkxSocketClient()
    await ws.public.start()
    await ws.public.subscribe([{'channel': "trades", 'instId': "BTC-USDT"}], callback=ws_handler)

async def multiple():
    ws = OkxSocketClient()
    await ws.public.start()
    await ws.public.subscribe([{'channel': "tickers", 'instId': "BTC-USDT"}, {'channel': "trades", 'instId': "BTC-USDT"}], callback=ws_handler)
    print("Subscribed!................")

async def candles():
    ws = OkxSocketClient("2ca75ca7-005f-47e6-84df-1e367eec17c2", "5EE5DFF9DA0EF9E82E402ED1AABEC51F", "bo1144167AZ*")
    await ws.business.start()
    await ws.business.subscribe([{'channel': "candle1H", 'instId': "BTC-USDT"}], callback=ws_handler)

asyncio.run(multiple())

# from okx.restapi.OrderBookTrading.Trading import TradingClient
# api = TradingClient("2ca75ca7-005f-47e6-84df-1e367eec17c2", "5EE5DFF9DA0EF9E82E402ED1AABEC51F", "bo1144167AZ*")
# result = api.place_order('BTCUSDT', 'buy', 'limit', '10000', '1')
# print(result)
