import discord
from discord.ext import commands


default_intents = discord.Intents.default()
default_intents.members = True

bot = commands.Bot(command_prefix="!")   
client = discord.Client(intents=default_intents)

class MyClient(discord.Client):
    async def on_ready():
     print("Le bot est prêt !")


    async def on_member_join(member):
     general_channel: discord.TextChannel = bot.get_channels(964456995195330583)
        await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")


    async def on_message(message):
     if message.content.lower() == "ping":
        await message.channel.send("pong")

    async def on_message(message):
        if message.content.startswith("!del"):
         number = int(message.content.split()[1])
         messages = await message.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()





bot.run("OTY0NDIzMjg4NDA5NDQ0MzYz.YlkbLg.gncWDpCYrrbhHL5JYr2dMjHVFyI")
