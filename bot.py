import requests
import disnake
import os
from disnake.ext import commands
from dotenv import load_dotenv
from disnake import SlashCommand, Option

load_dotenv()

TOKEN = os.environ.get("TOKEN")
server_id = None
bot = commands.Bot(
    command_prefix="/",
    help_command=None,
    intents=disnake.Intents.all(),
    test_guilds=server_id,
)
forbidden_words = []


@bot.command(name="id_server")
async def save_server_id(ctx):
    global server_id
    server_id = ctx.guild.id
    await ctx.send("тепрь на этом сервере будут работать слеш-команды")


@bot.event
async def on_ready():
    print(f"{bot.user} started!")


channel_id = None

@bot.slash_command(name="help")
async def help(ctx):
    await ctx.send("Hello! ")

@bot.slash_command(name="nsfw_channel")
async def save_channel_id(ctx):
    if "admin" in [role.name.lower() for role in ctx.author.roles]:
        global channel_id
        channel_id = ctx.channel.id
        await ctx.send("теперь на этом канале будут работать nsfw команды")
    else:
        await ctx.send("Эта команда доступна только для администраторов.")


@bot.slash_command(name="waifu", description="Отправляет sfw")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/waifu"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="hot_girl", description="Отправляет nsfw-waifu")
async def anime(ctx):
    if ctx.channel.id == channel_id:
        url = "https://api.waifu.pics/nsfw/waifu"
        response = requests.get(url)
        data = response.json()
        await ctx.send(data["url"])
    else:
        await ctx.send("команда доступна только в #nsfw")


@bot.slash_command(name="hot-neko", description="Отправляет nsfw-neko")
async def anime(ctx):
    if ctx.channel.id == channel_id:
        url = "https://api.waifu.pics/nsfw/neko"
        response = requests.get(url)
        data = response.json()
        await ctx.send(data["url"])
    else:
        await ctx.send("команда доступна только в #nsfw")


@bot.slash_command(name="blowjob", description="Отправляет nsfw blowjob")
async def anime(ctx):
    if ctx.channel.id == channel_id:
        url = "https://api.waifu.pics/nsfw/blowjob"
        response = requests.get(url)
        data = response.json()
        await ctx.send(data["url"])
    else:
        await ctx.send("команда доступна только в #nsfw")


@bot.slash_command(name="awoo", description="Отправляет что-то типо неко девочек")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/awoo"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="bite", description="Отправляет кусь")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/bite"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="bully", description="Отправляет аниме буллинг")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/bully"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="cry", description="Отправляет аниме слезки")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/cry"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="cuddle", description="Отправляет тисканья")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/cuddle"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="dance", description="Отправляет dance")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/dance"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="glomp", description="Отправляет обнимашки")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/glomp"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="happy", description="Отправляет happy")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/happy"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="kiss", description="Отправляет чмок")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/kiss"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="lick", description="Отправляет lick")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/lick"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="neko", description="Отправляет neko")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/neko"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="nom", description="Отправляет nom")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/nom"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="pat", description="Отправляет pat")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/pat"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="poke")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/poke"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="slap")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/slap"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="smug")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/smug"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="wave")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/wave"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


@bot.slash_command(name="wink")
async def anime(ctx):
    url = "https://api.waifu.pics/sfw/wink"
    response = requests.get(url)
    data = response.json()
    await ctx.send(data["url"])


bot.run(TOKEN)
