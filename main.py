import discord, os
from discord.ext.commands import Bot
from discord.ext import commands


#intents = discord.Intents.default()
#intents.members = True
#intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all()())
print("Bot Online.")

@bot.event()
async def ping(ctx):
    await ctx.send('pong')

#token = os.environ['token']
bot.run("OTc0MjczNDMzODQ2MzA0NzY4.Gy8h8W.NZZ0UQBPPO4odbCFTLM2Cp7-f8WImgUftz7fmk")

# https://discord.com/api/oauth2/authorize?client_id=974273433846304768&permissions=2214841408&scope=bot