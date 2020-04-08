import discord
from discord.ext import commands

from bot import mojang

class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("**ERROR** You missed a required argument")
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("**ERROR** That command does not exist")
        return

    @commands.command()
    async def uuid(self, ctx, username):
        """Returns the UUID of a player"""
        uuid = await mojang.get_uuid(username)
        embed = discord.Embed(
            title="UUID",
            description=f"{uuid}",
            colour=discord.Color.green()
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Minecraft(bot))
