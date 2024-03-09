import asyncio
import json
import logging

from okx.wsapi import wsutils
from okx.wsapi.Factory import WebSocketFactory

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("WsPrivate")


class PrivateAsyncClient:
    def __init__(self, apikey, apisecret, passphrase, url, use_server_time):
        self.url = url
        self.subscriptions = set()
        self.callback = None
        self.loop = asyncio.get_event_loop()
        self.factory = WebSocketFactory(url)
        self.apikey = apikey
        self.apisecret = apisecret
        self.passphrase = passphrase
        self.use_server_time = use_server_time

    async def connect(self):
        self.websocket = await self.factory.connect()

    async def consume(self):
        async for message in self.websocket:
            # logger.info("Received message: {%s}", message)
            if self.callback:
                self.callback(message)

    async def subscribe(self, params: list, callback):
        self.callback = callback

        logRes = await self.login()
        await asyncio.sleep(5)
        if logRes:
            payload = json.dumps({
                "op": "subscribe",
                "args": params
            })
            await self.websocket.send(payload)
        await self.consume()

    async def login(self):
        loginPayload = wsutils.init_login_params(
            apikey=self.apikey,
            apisecret=self.apisecret,
            passphrase=self.passphrase,
            use_server_time=self.use_server_time
        )
        await self.websocket.send(loginPayload)
        return True

    async def unsubscribe(self, params: list, callback):
        self.callback = callback
        payload = json.dumps({
            "op": "unsubscribe",
            "args": params
        })
        logger.info(f"unsubscribe: {payload}")
        await self.websocket.send(payload)
        # for param in params:
        #     self.subscriptions.discard(param)

    async def stop(self):
        await self.factory.close()
        self.loop.stop()

    async def start(self):
        logger.info("Connecting to WebSocket...")
        await self.connect()
        # self.loop.create_task(self.consume())

    def stop_sync(self):
        self.loop.run_until_complete(self.stop())
