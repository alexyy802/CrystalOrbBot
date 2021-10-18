import discord
from discord.ext import commands

class Guide(commands.Cog):
  def __init__(self, client):
      self.bot = client
      self._last_member = None
  
  @commands.command()
  async def guide(self,ctx):
    embed=discord.Embed(title="<a:guide:898488667004354560> Bar Bot Guide")
    embed.add_field(name="Ordering", value="To order a drink you must run the command **b!order <urdrink>**")
    embed.add_field(name="Economy :",value="\nWork\n To work use `b!work` \nBeg\n To beg use the command `b!beg` \nBeer\n To start filling up ur **Beer Storage** Use `b!beer`")
    embed.set_footer(text="Still need help? join our support server!")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Guide(client))
