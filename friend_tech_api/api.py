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
        self.session = AsyncClient(headers=self.headers)

    async def get(self, endpoint: str):
        response = await self.session.get(endpoint)
        return response.json()

    async def post(self, endpoint: str, json=None):
        response = await self.session.post(endpoint, json=json)
        return response.json()


class NonRest:
    def __init__(self, api_base: APIBase):
        self.api_base = api_base

    async def used_code(self, code):
        return await self.api_base.post(f"{API}/used-code", json={"code": code})

    async def holding_activity(self, address):
        return await self.api_base.get(f"{API}/holdings-activity/{address}")

    async def friends_activity(self, address):
        return await self.api_base.get(f"{API}/friends-activity/{address}")

    async def notifications_chatrooms(self, address):
        return await self.api_base.get(f"{API}/notifications/chatRooms/{address}")

    async def search_users(self, username):
        return await self.api_base.get(f"{API}/search/users?={username}")


class Users:
    def __init__(self, api_base: APIBase):
        self.api_base = api_base

    async def users(self, address):
        return await self.api_base.get(f"{API}/users/{address}")

    async def by_id(self, index):
        return await self.api_base.get(f"{API}/users/by-id/{index}")
