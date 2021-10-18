import discord
from discord.ext import commands

class Credits(commands.Cog):
  def __innit__(self,client):
      self.bot = client
      self._last_member = None

  @commands.command()
  async def credits(self,ctx):
    embed=discord.Embed(title="<:info:898166671066402826> Credits")
    embed.add_field(name="<:owner:891265219664437309> Owner :", value="NotAlexy_kyu#4003", inline=False)
    embed.add_field(name="<:developer:891263247452372993> Developer :", value="-------", inline=False)
    embed.add_field(name="<:manager:899209735914536961> Manager",value="mordekaiser0720#0720",inline = False)
    embed.add_field(name="<:Helper:898168928562475038> Helpers :",value="ᗰᗩKI#3109 and LancepticMC#6379",inline = False)
    embed.add_field(name="<:discordpy:898169620261924884> Made in :", value="Python and discord.py", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}")
    await ctx.send(embed=embed)


def setup(client):
  client.add_cog(Credits(client))
