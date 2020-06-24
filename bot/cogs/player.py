import discord
from discord.ext import commands

from bot import requests

from datetime import date

class Player(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send("**ERROR** You missed a required argument")
        elif isinstance(error, commands.CommandNotFound):
            return await ctx.send("**ERROR** That command does not exist")
        raise error

    @commands.command()
    async def uuid(self, ctx, username):
        """Returns the UUID of a player"""
        uuid = await requests.get_uuid(username)
        embed = discord.Embed(
            title="UUID",
            description=f"{uuid}",
            colour=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def history(self, ctx, username):
        """Returns the name history of a player"""
        uuid = await requests.get_uuid(username)
        history = await requests.get_history(uuid)
        embed = discord.Embed(
            title="Player Name History",
            colour=discord.Color.green()
        )
        embed.add_field(name=history[0]["name"],value="test")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Player(bot))
