from discord.ext import commands
import discord
import random


class Eightball(commands.Cog):
  def __init__(self, client):
      self.bot = client
      self._last_member = None

  @commands.command(aliases=["8ball"])
  async def eightball(self,ctx):
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

def setup(client):
  client.add_cog(Eightball(client))
