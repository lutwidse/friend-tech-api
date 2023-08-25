from friend_tech_api.api import APIBase, NonRest, Users
from friend_tech_api.api_websocket import APIBase as APIBaseWebsocket
from friend_tech_api.api_websocket import NonRest as NonRestWebsocket


class FriendTechClient:
    def __init__(self):
        api_base = APIBase()
        self.non_rest = NonRest(api_base)
        self.users = Users(api_base)


class FriendTechWebsocketClient:
    def __init__(self):
        self.api_base = APIBaseWebsocket()
        self.non_rest = None

    async def initialize(self):
        await self.api_base.connect()
        self.non_rest = NonRestWebsocket(self.api_base)

    async def close(self):
        await self.api_base.disconnect()