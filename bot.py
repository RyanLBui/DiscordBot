import discord
from discord.ext import commands

# instance of a bot
client = commands.Bot(command_prefix = ".")

# first event
@client.event
async def on_ready():
    print("Bot is ready")

client.run("NjA5MDk2NTQwNDU5NjMwNjA0.XUxvaQ.YmRAPf_NyRLjANeJnnsdDbanOAk")