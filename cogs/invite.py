import discord
from discord.ext import commands

class Invite(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self._last_member = None

    @commands.command()
    async def invite(self,ctx):
      e = discord.Embed(title="")
      e.add_field(name="Invite me!",value="[Click me!](https://discord.com/api/oauth2/authorize?client_id=859713560774574101&permissions=139586817024&scope=bot%20applications.commands)",inline=False)
      e.add_field(name="Website",value="[Click me!](https://BarBot.alexydacoder.repl.co)",inline=False)
      e.add_field(name="Support Server",value="[Click me!](https://discord.gg/K2QND4VMVz)",inline=False)
      await ctx.send(embed=e)

def setup(client):
  client.add_cog(Invite(client))
