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
        embed = None
        if server["online"]:
            count = server["players"]["online"]
            embed = discord.Embed(
                colour=discord.Color.green(),
                description="""**Server is online**

                **›› IP**
                {ip}

                **›› MOTD**
                {motd}

                **›› Player Count**
                {player_count}

                **›› Version**
                {version}""".format(ip=server["ip"],
                                    motd="\n".join(server["motd"]["clean"]),
                                    player_count=str(count) + "/"+ str(server["players"]["max"]),
                                    version=server["version"])
            )
#            if count > 0 and count <= 10:
#                embed.add_field(name="Players", value="\n".join(server["players"]["list"]))
            embed.set_thumbnail(url=f"https://api.mcsrvstat.us/icon/{address}")
        else:
            embed = discord.Embed(
                description="The server requested is not online or does not exist.",
                colour=discord.Color.red()
            )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Server(bot))
