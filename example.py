from friend_tech_api.client import FriendTechClient, FriendTechWebsocketClient
import asyncio


async def receive_messages(client_websocket):
    while True:
        message = await client_websocket.non_rest.receive()
        print(f"{message}")


async def main():
    client = FriendTechClient()
    example_user = await client.users.by_id(100000)
    print(example_user)

    client_websocket = FriendTechWebsocketClient()
    await client_websocket.initialize()
    asyncio.create_task(receive_messages(client_websocket))
    await client_websocket.non_rest.ping()
    await client_websocket.non_rest.sendMessage("A", [], "0x750add0f18b005c20cdf76236bb0f15429c7aa9a", "0xf00dbabes")

    await asyncio.sleep(60 * 60 * 24)

asyncio.run(main())
