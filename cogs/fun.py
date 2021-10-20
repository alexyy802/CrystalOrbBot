import discord
from discord.ext import commands
import random

class Funcogs(commands.Cog):
  def __init__(self,client):
    self.bot = client
    self._last_member = None

  @commands.command()
  async def cointoss(self,ctx):
      determine_flip = [1, 0]

      if random.choice(determine_flip) == 1:
        embed = discord.Embed(title="Coinflip <a:cointoss:898167957379760158>",description=f"{ctx.author.mention} Flipped a coin, we got **Heads**!",color=0xff00c8)
        await ctx.send(embed=embed)

      else:
        embed = discord.Embed(title="Coinflip <a:cointoss:898167957379760158>", description=f"{ctx.author.mention} Flipped a coin, we got **Tails**!",color=0xff00c8)
        await ctx.send(embed=embed)
  
  @commands.command(aliases=["8ball"])
  async def eightball(self,ctx,arg):
    responses = [
    "yes",
    "maybe",
    "I dont get payed enough to do this sure go nuts",
    "ask me later bud",
    "I am not quiet sure about that",
    "Sure i guess",
    "nope heck naaah",
    "ofc :D",
    "yesnt uwu",
    "Heck no",
    ]
    e=discord.Embed(title="<:z8ball:898165143874195486> 8ball Has Spoken <:z8ball:898165143874195486>",description=f"Answer : `{random.choice(responses)}`")
    await ctx.reply(embed=e)

  @commands.command()
  async def ping(self,ctx):
      embed=discord.Embed(title=f"Pong! <a:CH_Latency:898428199183212624>", description=f"My Ping is `{round(self.bot.latency * 1000)}`ms")
      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Funcogs(client))
