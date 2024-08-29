import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def Selam(ctx):
    await ctx.send(f'Hop')
@bot.command()
async def sa(ctx):
    await ctx.send(f'as kanka')
@bot.command()
async def Hangi_Müzikleri_Seversin(ctx):
    await ctx.send(f'Rap dinlerim kanka')
@bot.command()
async def Nasılsın(ctx):
    await ctx.send(f'İyiyim Kankam, Sen?')
@bot.command()
async def EoS(ctx):
    await ctx.send(f'babe you got something on your nose...')
@bot.command()
async def En_Sevdiğin_Şarkıcı(ctx):
    await ctx.send(f'Hidra,Allame,Joker,Şehinşah ve dahası')
@bot.command()
async def En_Sevdiğin_Futbolcu(ctx):
    await ctx.send(f'LM10,MR11,LS9')
bot.run("TOKEN BURAYA")
