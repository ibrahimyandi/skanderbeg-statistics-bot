import discord
from discord.ext import commands
from gp import greatPowers
from adm import administrative
from mil import military 
from anyData import aData
from battles import battlesData
from navals import navalData
from score import scored
from aScore import aScored
import re 
import time
from PIL import Image

bot = commands.Bot(command_prefix="!ss ", help_command=None)
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='!ss help | SW:2a65SWSZAG | PacTi#7453'))

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
        await ctx.send(str(greatPowers(save,8))+str(administrative(save)))
        await ctx.send(str(military(save))+str(battlesData(save,3)))
        await ctx.send(str(navalData(save,3)))    
        await ctx.send(str(scored(save)))
        
@bot.command()
async def data(ctx, save, dataId, playerCount):
    if "gm" in [i.name.lower() for i in ctx.author.roles]:
        await ctx.send(aData(save, dataId, playerCount))

@bot.command()
async def battle(ctx, save, playerCount):
    if "gm" in [i.name.lower() for i in ctx.author.roles]:
        await ctx.send(battlesData(save, playerCount))

@bot.command()
async def naval(ctx, save, playerCount):
    if "gm" in [i.name.lower() for i in ctx.author.roles]:
        await ctx.send(navalData(save, playerCount))

@bot.command()
async def aScore(ctx, save):
    if "gm" in [i.name.lower() for i in ctx.author.roles]:
        await ctx.send(AScored(save))

@bot.command()
async def score(ctx, save):
    if "gm" in [i.name.lower() for i in ctx.author.roles]:
        await ctx.send(scored(save))

@bot.command()
async def map(ctx, player_country_list):
    if "gm" in [i.name.lower() for i in ctx.author.roles]:
        class Country:
            def __init__(self, name, color=(0,0,0), isVassal = False):
                self.name = name
                self.file_name = ''
                self.color = color
                self.vassals = []
                self.isVassal = isVassal
                self.overlord = None

            def addVassal(self, vassal):
                if vassal is not None:
                    self.vassals.append(vassal)
                    vassal.overlord = self
                    vassal.isVassal = True

            def getFileName(self):
                if self.file_name == '':
                    weirdoDict = listWeirdos()
                    if self.name in weirdoDict:
                        self.file_name = weirdoDict[self.name]
                    else:
                        self.file_name = self.name

            def findColor(self):
                self.getFileName()
                countryFile = open("countries/"+self.file_name+'.txt', encoding="utf8", errors='ignore')
                for line in countryFile:
                    if "color" in line:
                        line = line.split('{')
                        line = line[1].split('}')
                        line = line[0].strip()
                        line = line.split()
                        break
                self.color = (int(line[0]), int(line[1]), int(line[2]))
        dcList = []
        def seperator():
            CountryName = ""
            for i in player_country_list:
                if i != ",":
                    CountryName += i
                else:
                    dcList.append(CountryName)
                    CountryName = ""


        def collectCountries():
            seperator()
            countryList = []
            overlord = None
            for line in dcList:
                line = line.strip()
                if '-' not in line:
                    newCountry = Country(line)
                    overlord = newCountry
                    countryList.append(newCountry)
                elif '-' in line:
                    name = line[1:]
                    newVassal = Country(name)
                    overlord.addVassal(newVassal)
                    countryList.append(newVassal)
            
            for country in countryList:
                country.findColor() 
            ocean = Country('ocean', (68, 107, 163))
            uncolonized = Country('uncolonized', (150, 150, 150))
            wasteland = Country('wasteland', (94, 94, 94))
            for feature in [ocean, uncolonized, wasteland]:
                countryList.append(feature)
            return countryList


        def listWeirdos():
            weirdoDict = {'game_name':'file_name'}
            with open('weird_names.txt', 'r') as weirdoFile:
                for line in weirdoFile:
                    equivalency = line.split(' = ')
                    equivalency[1] = equivalency[1].strip()
                    weirdoDict[equivalency[0]] = equivalency[1]
            return weirdoDict


        def getColorList(countryList):
            colorDict = {}
            for country in countryList:
                if country.isVassal:
                    colorDict[country.color] = country.overlord.color
                else:
                    colorDict[country.color] = country.color
            return colorDict


        def changeColors(inputImage):
            im = Image.open(inputImage)
            colorDict = getColorList(collectCountries())
            newImData = []
            for color in im.getdata():
                if color in colorDict:
                    newImData.append(colorDict[color])
                else:
                    newImData.append((150,150,150))
            newIm = Image.new(im.mode,im.size)
            newIm.putdata(newImData)
            return newIm


        def main():
            inputImage, outputImage = "1444_map_null.png","1444_map.png"
            changeColors(inputImage).save(outputImage)


        if __name__ == "__main__":
            main()
        with open("1444_map.png", "rb") as fh:
            f = discord.File(fh, filename="player_map/1444_map.png")
        await ctx.send(file=f)

@bot.command()
async def help(ctx):
    await ctx.send("""```Bot hakkında bilgi edinmek için Discord: https://discord.gg/ZrU9xvyN2A adresini ziyaret ediniz. ```""")

bot.run('#####')
