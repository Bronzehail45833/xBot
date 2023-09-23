import discord
from discord.ext import commands
from GetGamertag import Checker

Token = ''
Channel_id = 

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'successfully logged in as {bot.user}')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Gamertags"))

@bot.command()
async def check(ctx, gamertag=None):
    gt_Checker = Checker(gamertag)
    gt_Checker.GetData(gamertag)
    if gamertag is None:
        await ctx.send("Please supply a gamertag to be checked. \nUsage: check gamertag")
        return
    
    await ctx.send(f'The gamertag {gamertag} {gt_Checker.GetAvailabiltity(gamertag)}!')

bot.run(Token)
