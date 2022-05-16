# scraped version as in like a month the library this bot uses stops working (moved to js)

import discord, os, asyncio, random
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = '.')

@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(bot))
  await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("Duelist"))

@bot.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  await member.ban(reason=reason)

@bot.event
async def on_message(message):
  username = str(message.author).split('#')[0]
  if message.content.startswith("slay"):  
    if username == "Atrazine":
       await message.channel.send("Slay indeed father.")
    else:
      await message.channel.send("Slay indeed.")
  elif message.content.startswith("Hello"):
    await message.channel.send("Hi, {}.".format(username))


bot.run(os.environ['token'])




#plan for bot
#  - moderation
#    - ban command
#    - antiswear and warn
#  - scrap github raw and format in announcing
#    - scrape https://raw.githubusercontent.com/Ducks-Scripts/duelist-game/main/changelog.md?token=GHSAT0AAAAAABUKAM6BLCWQJAKG3GUA5MXMYT7NL6Q
#    - send embed with update as title and changes as dot points
# https://discord.com/api/oauth2/authorize?client_id=974273433846304768&permissions=8&scope=bot