import discord
from discord.ext import commands
from gp import greatPowers
from adm import administrative
from mil import military 
from anyData import aData
from battles import battlesData
import re 

bot = commands.Bot(command_prefix="!ss ", help_command=None)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='!ss help | SW:2a65SWSZAG | PacTi#7453'))

@bot.event
async def on_message(message):
    if message.content.startswith('!ss'):
        await bot.process_commands(message)
        await message.delete() 

@bot.command()
async def gp(ctx, save, playerCount):
    if "gm" in [i.name.lower() for i in ctx.author.roles]:
        await ctx.send(greatPowers(save, playerCount))

@bot.command()
async def adm(ctx, save):
    if "gm" in [i.name.lower() for i in ctx.author.roles]:
        await ctx.send(administrative(save))

@bot.command()
async def mil(ctx, save):
    if "gm" in [i.name.lower() for i in ctx.author.roles]:
        await ctx.send(military(save))

@bot.command()
async def all(ctx, save):
    if "gm" in [i.name.lower() for i in ctx.author.roles]:
        await ctx.send(str(administrative(save))+ str(military(save)))

@bot.command()
async def data(ctx, save, dataId, playerCount):
    if "gm" in [i.name.lower() for i in ctx.author.roles]:
        await ctx.send(aData(save, dataId, playerCount))

@bot.command()
async def battle(ctx, save, playerCount):
    if "gm" in [i.name.lower() for i in ctx.author.roles]:
        await ctx.send(battlesData(save, playerCount))
    
@bot.command()
async def help(ctx):
    await ctx.send("""```Komut: !ss gp [save] [oyuncu sayısı]\nKomut: !ss adm [save]\nKomut: !ss mil [save]\nKomut: !ss all [save]\nKomut: !ss data [save] [dataId] [oyuncu sayısı]\nKomut: !ss battle [save] [oyuncu sayısı]\nBotu sadece (GM) rolüne sahip kişiler kullanabilir.```""")

bot.run('ODE2NjIwNDUyODY4MjU5ODkw.YD9nEA.z-LnaEYWsvMeYDRwiUWQhbe2938')