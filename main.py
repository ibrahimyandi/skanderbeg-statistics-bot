import discord
from discord.ext import commands
from gp import greatPowers
import re 

bot = commands.Bot(command_prefix="!ss ", help_command=None)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("hazırım")
    await bot.change_presence(activity=discord.Game(name='!ss help | git.io/JqkZM'))

@bot.event
async def on_message(message):
    if message.content.startswith('!ss'):
        await bot.process_commands(message)
        await message.delete() 

@bot.command()
async def gp(ctx, save, playerCount):
    await ctx.send(greatPowers(save, playerCount))

@bot.command()
async def help(ctx):
    await ctx.send("""```Command: !ss gp [save] [player count]\nDescription: Player shows great power ranking.```""")

bot.run('ODE2NjIwNDUyODY4MjU5ODkw.YD9nEA.z-LnaEYWsvMeYDRwiUWQhbe2938')