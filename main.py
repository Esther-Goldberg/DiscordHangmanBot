import discord
import logging
import os

import hangman

from discord.ext import commands
from dotenv import load_dotenv

# set up logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w+')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()

intents = discord.Intents(messages=True, reactions=True, guilds=True)

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} {bot.user.id}')

bot.add_cog(hangman.Hangman(bot))

bot.run(os.environ.get("TOKEN"))
