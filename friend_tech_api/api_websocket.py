import websockets
import json
from .config import API, AUTHORIZATION_TOKEN


class APIBase:
    def __init__(self) -> None:
        self.session = None

    async def connect(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        }
        self.session = await websockets.connect(f"wss://{API}/?authorization={AUTHORIZATION_TOKEN}", extra_headers=headers)

    async def disconnect(self):
        if self.session:
            await self.session.close()
            self.session = None


class NonRest:
    def __init__(self, api_base: APIBase):
        self.api_base = api_base

    async def receive(self):
        return await self.api_base.session.recv()

    async def close(self):
        await self.api_base.session.close()

    async def ping(self):
        await self.api_base.session.send(json.dumps({"action": "ping"}))

    async def sendMessage(self, text: str, imagePaths: list[str], chatRoomId: str, clientMessageId: str):
        """
        Args:
        - text : The text content of the message to be sent.
        - imagePaths: A list of URLs pointing to images. Though it's not a 
          legitimate request, the function still works with it.
        - chatRoomId: The address indicating the chat room ID.
        - clientMessageId: A random 11-digit string consisting of characters a-z and numbers 0-9, 
          used as an identifier for the message."""
        await self.api_base.session.send(json.dumps({"action": "sendMessage", "text": f'\"{text}\"', "imagePaths": imagePaths, "chatRoomId": chatRoomId, "clientMessageId": clientMessageId}))
