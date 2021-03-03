import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="!ss ")
bot.remove_command('help')
@bot.event
async def on_ready():
    print("hazırım")

@bot.command()
async def statistics(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def help(msg):
    await msg.send("Command: !ss statistics [key] [id]")

bot.run('ODE2NjIwNDUyODY4MjU5ODkw.YD9nEA.z-LnaEYWsvMeYDRwiUWQhbe2938')