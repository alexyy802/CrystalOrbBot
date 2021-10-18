import discord
from discord.ext import commands
import datetime,time

class Botinfo(commands.Cog):
  def __init__(self,client):
     self.bot = client
     self._last_member = None

  
  @commands.command(aliases=['bi','stats','status'])
  async def botinfo(self,ctx):
    start_time = time.time()
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    members = 0
    for guild in self.bot.guilds:
      members += guild.member_count - 1

    embed = discord.Embed(title=":desktop: Bot Info :desktop:")
    embed.add_field(name=":robot: Bot name",value="Bar Bot#1743")
    embed.add_field(name="<:online:898170147993440266> Status",value="Online")
    embed.add_field(name="<:servers:898170039595831306> Servers ",value=f"{len (self.bot.guilds)}")
    embed.add_field(name="<:members:891897587286818847> Users",value=members)
    embed.add_field(name="<:prefix:898174448916639754> Prefix",value="`b!`")
    embed.add_field(name="<:botshard:898174197119983616> Shards",value="2")
    embed.add_field(name="<:idcard:898173965044944916> Client ID",value="859713560774574101")
    embed.add_field(name="<:uptime:898173066172051476> Uptime",value=text)
    await ctx.send(embed=embed)
  
  @commands.command()
  async def credits(self,ctx):
    embed=discord.Embed(title="<:info:898166671066402826> Credits")
    embed.add_field(name="<:owner:891265219664437309> Owner :", value="NotAlexy_kyu#4003", inline=False)
    embed.add_field(name="<:developer:891263247452372993> Developer :", value="||Dank Lord||#9919 and VincentRPS#9183", inline=False)
    embed.add_field(name="<:manager:899209735914536961> Manager",value="mordekaiser0720#0720",inline = False)
    embed.add_field(name="<:Helper:898168928562475038> Helpers :",value="ᗰᗩKI#3109 and LancepticMC#6379",inline = False)
    embed.add_field(name="<:discordpy:898169620261924884> Made in :", value="Python and discord.py", inline=False)
    embed.set_footer(text=f"Requested by {ctx.author}")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Botinfo(client))
