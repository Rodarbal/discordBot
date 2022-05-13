import discord, os, asyncio
from discord.ext.commands import Bot
from discord.ext import commands


intents = discord.Intents.default()
bot = commands.Bot(command_prefix='$', intents=intents)
print("Bot Online.")

@bot.command()
async def on_message(message):
  if message.content.startswith('Ping'):
    channel = message.channel
    await channel.send("Pong")

token = os.environ['token']
bot.run(token)

# https://discord.com/api/oauth2/authorize?client_id=974273433846304768&permissions=2214841408&scope=bot