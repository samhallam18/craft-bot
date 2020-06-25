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
            description="""**›› UUID**
            {uuid}""".format(uuid=uuid)
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def history(self, ctx, username):
        """Returns the name history of a player"""
        uuid = await requests.get_uuid(username)
        history = await requests.get_history(uuid)
        history[0]["changedToAt"] = "Initial Name"
        for i in range(1, len(history)):
            history[i]["changedToAt"] = str(date.fromtimestamp(history[i]["changedToAt"]/1000))
        desc = "**Player Name History**\n\n"
        for i in range(len(history)):
            desc += f"**›› {history[i]['name']}**\n{history[i]['changedToAt']}\n"
        embed = discord.Embed(
            description=desc
        )
        embed.set_footer(text="Date Changed Format: yyyy-mm-dd")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Player(bot))
