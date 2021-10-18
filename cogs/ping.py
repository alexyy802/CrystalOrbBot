from discord.ext import commands
import discord

class Ping(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self._last_member = None

    @commands.command()
    async def ping(self,ctx):
      embed=discord.Embed(title=f"Pong! <a:CH_Latency:898428199183212624>", description=f"My Ping is `{round(self.bot.latency * 1000)}`ms")
      await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Ping(client))
