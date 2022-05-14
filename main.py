import discord, os, asyncio
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(bot))

@bot.event
async def on_message(message):
  username = str(message.author).split('#')[0]
  if message.content.startswith("slay"):  
    if username == "Atrazine":
       await message.channel.send("Slay indeed father.")
    else:
      await message.channel.send("Slay indeed.")
  if message.content.startswith("Hello"):
    await message.channel.send("Hi, {}.".format(username))
  


token = os.environ['token']
bot.run(token)

# https://discord.com/api/oauth2/authorize?client_id=974273433846304768&permissions=2214841408&scope=bot