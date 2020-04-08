import httpx


def get_uuid(username):
    async with httpx.AsyncClient() as client:
        req = await client.get(f"https://api.mojang.com/users/profiles/minecraft/{username}")
    return req.json()
