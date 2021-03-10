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
async def help(ctx):
    await ctx.send("""```Command: !ss gp [save] [oyuncu sayısı]\nDescription: Oyuncuların büyük güç sıralamasını gösterir.\n\nCommand: !ss adm [save]\nDescription: Yönetim istatistiklerini gösterir.\n\nCommand: !ss mil [save]\nDescription: Askeri istatistiklerini gösterir.\n\nCommand: !ss all [save]\nDescription: Askeri ve Yönetim istatistiklerini gösterir.\n\nBotu sadece (GM) rolüne sahip kişiler kullanabilir```""")

bot.run('ODE2NjIwNDUyODY4MjU5ODkw.YD9nEA.z-LnaEYWsvMeYDRwiUWQhbe2938')