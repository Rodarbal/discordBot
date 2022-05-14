import discord, os, asyncio
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
  print("logged in as {0.user}".format(bot))

@bot.event
async def on_message(message):
  if message.content.startswith("Ping"):
    await message.channel.send("Pong")
  


token = os.environ['token']
bot.run(token)

# https://discord.com/api/oauth2/authorize?client_id=974273433846304768&permissions=2214841408&scope=bot