from httpx import AsyncClient
from .config import API, AUTHORIZATION_TOKEN


class APIBase:
    def __init__(self) -> None:
        self.headers = {
            "Authorization": AUTHORIZATION_TOKEN,
            'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'Accept': '*/*',
            'Sec-Ch-Ua-Mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Origin': 'https://www.friend.tech',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.friend.tech/',
            'Accept-Language': 'ja,en-US;q=0.9,en;q=0.8',
        }
        self._session = AsyncClient(headers=self.headers)

    async def get(self, endpoint: str):
        response = await self._session.get("https://" + API + endpoint)
        return response.json()

    async def post(self, endpoint: str, json=None):
        response = await self._session.post("https://" + API + endpoint, json=json)
        return response.json()


class NonRest:
    def __init__(self, api_base: APIBase):
        self.api_base = api_base

    async def access_token(self, code, state):
        return await self.api_base.post(f"/twitter/oauth/access_token", json={"code": code, "state": state})

    # Vulnerable
    async def used_code(self, code):
        return await self.api_base.post(f"/used-code", json={"code": code})

    async def gating_state(self, address):
        return await self.api_base.get(f"/gating-state/{address}")

    async def holding_activity(self, address):
        return await self.api_base.get(f"/holdings-activity/{address}")

    async def friends_activity(self, address):
        return await self.api_base.get(f"/friends-activity/{address}")

    # Vulnerable
    async def notifications_chatrooms(self, address):
        return await self.api_base.get(f"/notifications/chatRooms/{address}")

    async def search_users(self, username):
        return await self.api_base.get(f"/search/users?={username}")

    # Your keys
    async def holdings_activity(self, address):
        return await self.api_base.get(f"/holdings-activity/{address}")

    # Friends
    async def friends_activity(self, address):
        return await self.api_base.get(f"/friends-activity/{address}")

    # Global
    async def global_activity(self):
        return await self.api_base.get(f"/global-activity")


class Users:
    def __init__(self, api_base: APIBase):
        self.api_base = api_base
        self.token = self._Token(self.api_base)

    async def users(self, address):
        return await self.api_base.get(f"/users/{address}")

    async def by_id(self, index):
        return await self.api_base.get(f"/users/by-id/{index}")

    # Traders
    async def token_holdings(self, address):
        return await self.api_base.get(f"/users/{address}/token-holdings")

    # Activity
    async def trade_activity(self, address):
        return await self.api_base.get(f"/users/{address}/trade-activity")

    class _Token:
        def __init__(self, api_base: APIBase):
            self.api_base = api_base

        # Holders
        async def holders(self, address):
            return await self.api_base.get(f"/users/{address}/token/holders")

        # Holding
        async def trade_activity(self, address):
            return await self.api_base.get(f"/users/{address}/token/trade-activity")
