import discord
from discord.ext import commands

from bot import requests


class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx, address):
        """Returns information about the requested server"""
        server = await requests.get_server(address)
        await ctx.send("ip: " + server["ip"] + ", ping: " + str(server["debug"]["ping"]))


def setup(bot):
    bot.add_cog(Server(bot))
