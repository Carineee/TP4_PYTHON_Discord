import discord
from discord import Client

client = discord.Client()

@client.event
async def on_ready():
    print("Le bot est prêt !")


@client.event
async def on_message(message):
    if message.content.lower() == "welcome":
        await message.channel.send("how are you")


@client.event
async def on_message(message):
    if message.content.startwith("!del"):

        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number +1).flatten()

        for each_message in messages:
            await each_message.delete()

client.run('OTY1ODg3NjM3NTc3Njc4OTI4.Yl5u9g.UU6TXm49G8namNTjele6sDB-ssg')