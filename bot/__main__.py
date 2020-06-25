import logging

import discord
from discord.ext import commands

import os


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('mc '),
    pm_help=True,
    case_insensitive=True
)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=f'in {len(bot.guilds)} servers.'))

bot.load_extension('bot.cogs.player')
bot.load_extension('bot.cogs.server')

if __name__ == "__main__":
    bot.run(os.environ.get("BOT_TOKEN"))
