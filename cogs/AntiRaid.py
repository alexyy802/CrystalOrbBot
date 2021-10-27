import discord
from discord.ext import commands

class Antiraid(commands.Cog):
  def __innit__(self, client):
    self.bot = client
    
  @commands.command()
  async def serverlock(self,ctx,channel:discord.Textchannel=None):
      for channel in ctx.guild.channels:
        await channel.set_permissions(ctx.guild.default_role, reason=f"Server lockdown triggerd by : {ctx.author}")
      e = discord.Embed(title="Anti Raid Triggerd!")
      e.add_field(name="Server is locked down, please be patient till a admin unlocks the server!",value="AntiRaid by NotAlexy_Kyu#4003")
      await ctx.send(embed=e)
      
  @commands.command()
  async def serverunlock(self,ctx,channel:discord.Textchannel=None):
    for channel in ctx.guild.channels:
      await channel.set_permissions(ctx.guild.default_role, reason=f"Server unlock triggerd by : {ctx.author}")
      e = discord.Embed(title="Server Unlocked!",description=f"{ctx.author} has unlocked the server)
      await ctx.send(embed=e)
                        
def setup(client):
  client.add_cog(Antiraid(client))
