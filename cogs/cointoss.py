import discord
from discord.ext import commands
import random

class Cointoss(commands.Cog):
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


def setup(client):
  client.add_cog(Cointoss(client))
