import discord
from discord.ext import commands

class Help(commands.Cog):
  def __innit__(self,client):
      self.bot = client
      self._last_member = None

  @commands.command()
  async def help(self,ctx):
    embed=discord.Embed(title="--={**All Commands**}=--")
    embed.add_field(name="Ping", value="Ping's a user in the server")
    embed.add_field(name="Eightball", value="the best 8ball around")
    embed.add_field(name="Smoke", value="Smoke some good old cigars")
    embed.add_field(name="Cointoss", value="Toss a coin!")
    embed.add_field(name="Youtube",value="Search a video from yt!")
    embed.add_field(name="serverinfo", value="Gives you info about the server")
    embed.add_field(name="Whois", value="Get info of a user ")
    embed.add_field(name="Help", value="Give's a list of commands")
    embed.add_field(name="Guide", value="Gives guide for new bot users")
    embed.add_field(name="Credits", value="Give's a list of developers and owner of the bot")
    embed.add_field(name="Botinfo",value="Gives info about the bot")
    embed.add_field(name="Server",value="Join our support server!")
    embed.add_field(name="Balance",value="Check ur balance!")
    embed.add_field(name="Beg",value="Get some money from beggin!")
    embed.add_field(name="Work",value="Get a job and earn some money!")
    embed.add_field(name="Deposit",value="Deposit money to ur bank!")
    embed.add_field(name="Withdraw",value="Withdraw some money from ur bank to ur wallet!")
    embed.add_field(name="Feedback",value="Give us ur feedback!")
    embed.set_thumbnail(url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}",icon_url="https://ctl.s6img.com/society6/img/UzBlOKW_TEifrUOrlc043un9ehg/w_700/prints/~artwork/s6-0054/a/23111039_13741984/~~/cute-booze-beer-prints.jpg")
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Help(client))
