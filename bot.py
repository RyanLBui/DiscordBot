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

#command error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid Command\nUse .help or .listcommands to see list of commands.")

# list all commands 
commandsList = "List of Commands:\n.ping\n.8ball (ask question)\n.Question (ask question)\n.clear (number of messages to clear)"

# function/command test bot reply
@client.command()
async def ping(ctx):
     await ctx.send(f"Pong? {round(client.latency * 1000)}ms")
     
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

#command to clear certain ammount of messages
@client.command()
async def clear(ctx, amount = 2):
    # pass in amount of messages to purge/delete from channel, if no amount given delete default number
    await ctx.channel.purge(limit = amount)

@client.command()
async def listcommands(ctx):
    await ctx.send(commandsList)


# get discord token from token.txt
getToken = open("token.txt", "r")
token = getToken.read()

client.run(token)
