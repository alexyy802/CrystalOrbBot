import discord
from discord.ext import commands

class Help(commands.Cog):
  def __innit__(self,bot):
    self.bot = bot

  @commands.command()
  async def help(self,ctx):
    e = discord.Embed(title="Commands List",colour=discord.Color.blue())
    e.add_field(name="<:moderation:904330690085154826> Moderation Commands",value="```Ban,Kick,Lock, Unlock, Unban```",inline=False)
    e.add_field(name="<:settings:904332989230624790> Settings",value="```enable-mod, disable-mod, enable-autolink, disable-autolink```",inline=False)
    e.add_field(name="<a:CD:904334222158888991> Music Commands",value="```connect, disconnect, play, equalizer, queue, loop, resume,pause, seek, volume, nowplaying```",inline=False)
    e.add_field(name="<a:infcmd:904335868754546698> Info Commands",value="```userinfo, serverinfo, botinfo, credits```",inline=False)
    await ctx.send(embed=e)

def setup(bot):
  bot.add_cog(Help(bot))
