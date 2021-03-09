import discord
from discord.ext import commands
from gp import greatPowers
from adm import administrative
from mil import military 
import re 

bot = commands.Bot(command_prefix="!ss ", help_command=None)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='!ss help | github.com/ibrahimyandi'))

@bot.event
async def on_message(message):
    if message.content.startswith('!ss'):
        await bot.process_commands(message)
        await message.delete() 

@bot.command()
async def gp(ctx, save, playerCount):
    await ctx.send(greatPowers(save, playerCount))

@bot.command()
async def adm(ctx, save):
    await ctx.send(administrative(save))

@bot.command()
async def mil(ctx, save):
    await ctx.send(military(save))

@bot.command()
async def all(ctx, save):
    await ctx.send(str(administrative(save))+ str(military(save)))

@bot.command()
async def help(ctx):
    await ctx.send("""```Command: !ss gp [save] [player count]\nDescription: Player shows great power ranking.\n\nCommand: !ss adm [save]\nDescription: Administrative statistics.\n\nCommand: !ss mil [save]\nDescription: Military statistics.\n\nCommand: !ss all [save]\nDescription: adm + mil statistics.```""")

bot.run('ODE2NjIwNDUyODY4MjU5ODkw.YD9nEA.z-LnaEYWsvMeYDRwiUWQhbe2938')