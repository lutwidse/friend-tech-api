from friend_tech_api.client import FriendTechClient
import asyncio


async def main():
    client = FriendTechClient()
    example_user = await client.users.by_id(100000)
    print(example_user)

asyncio.run(main())
