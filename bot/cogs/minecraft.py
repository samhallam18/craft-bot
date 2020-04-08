import discord
from discord.ext import commands

from

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uuid(self, ctx, username):
        uuid = mojang.uuid(username)
        await ctx.send(uuid)


def setup(bot):
    bot.add_cog(Minecraft(bot))
