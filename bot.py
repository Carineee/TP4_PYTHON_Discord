import discord
from discord.ext import commands


bot = commands.Bot(command_prefix= "!",)


@bot.event
async def on_ready():
     print("Le bot est prêt !")
   
@bot.command()
async def exemple(ctx):
    await ctx.send("hello")


#@bot.command(name='del')
#async def delete(ctx, number_of_message: int):
 #message = await ctx.channel.history(limit=number_of_message + 1).flatten()

 #for each_message in messages:
  #  await each_message.delete() 



bot.run("OTY1ODg3NjM3NTc3Njc4OTI4.Yl5u9g.UU6TXm49G8namNTjele6sDB-ssg")