import discord
from discord.ext import commands
import random

# instance of a bot
client = commands.Bot(command_prefix = ".")

# first event
@client.event
async def on_ready():
    print("Bot is ready")

#event when user joins server
@client.event
async def on_member_join(member):
    print(f"{member} has joined the server.")

#event when user leaves server
@client.event
async def on_member_remove(member):
    print(f"{member} has left the server.")

# function/command for bot to reply
@client.command()
async def ping(ctx):
     await ctx.send(f"Pong! {round(client.latency * 1000)}ms")
     
# 8 ball command
@client.command(aliases= ["8ball", "Question", "question", "8Ball"])    # aliases can be used to call function with any of these names
# *, - takes in multiple arguments
async def _8ball(ctx, *, question):
    responses = [
        "It is certain",
        "As I see it, Yes",
        "Ask again later",
        "Dont count on it"
    ]
    await ctx.send("Question: " + question + "\nAnswer: " + random.choice(responses))

client.run('NjA5MDk2NTQwNDU5NjMwNjA0.XUx6BA.KSYnOJM9LnHJOOw1xQFXe_RjdfM')
