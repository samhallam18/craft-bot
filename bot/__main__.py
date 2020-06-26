import logging
import os

import discord
from discord.ext import commands

from bot import constants

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('mc '),
    activity=discord.Game(name="Minecraft"),
    pm_help=True,
    case_insensitive=True
)

@bot.event
async def on_ready():
    embed = discord.Embed(
        description=f"{bot.user.name} is now online",
        colour=discord.Color.green()
    )
    channel = bot.get_channel(constants.LOG_CHANNEL)
    await channel.send(embed=embed)

bot.load_extension('bot.cogs.player')
bot.load_extension('bot.cogs.server')
bot.load_extension('bot.cogs.events')

if __name__ == "__main__":
    bot.run(os.environ.get("BOT_TOKEN"))
