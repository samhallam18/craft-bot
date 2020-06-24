import httpx


async def get_uuid(username):
    async with httpx.AsyncClient() as client:
        req = await client.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    return req.json()["id"]


async def get_history(uuid):
    async with httpx.AsyncClient() as client:
        req = await client.get(f"https://api.mojang.com/user/profiles/{uuid}/names")
    return req.json()


async def get_server(address):
    async with httpx.AsyncClient() as client:
        req = await client.get(f"https://api.mcsrvstat.us/2/{address}")
    return req.json()
