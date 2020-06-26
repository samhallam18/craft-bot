import discord
from discord.ext import commands

from bot import constants


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("**ERROR** You missed a required argument")
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("**ERROR** That command does not exist")
        else:
            await ctx.send("**ERROR** An unexpected error occured")
            channel = self.bot.get_channel(constants.LOG_CHANNEL)
            embed = discord.Embed(
                description=f"**›› Error occured: #{ctx.channel.name} in {ctx.guild.name}**\n{error}",
                colour=discord.Colour.red()
            )
            await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Events(bot))
