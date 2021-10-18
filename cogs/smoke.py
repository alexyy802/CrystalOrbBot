from discord.ext import commands
import discord

class Smoke(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self._last_member = None

    @commands.command()
    async def smoke(self,ctx):
        embed=discord.Embed(description=f"{ctx.author} smoked some cigar's :smoking:")
        embed.set_image(url="https://64.media.tumblr.com/266068c786083f554f95f73612930f39/a1651ccde3a6c741-a3/s500x750/759377fb0258dc8bd48ab3e89d6658d9c0d95af6.gif")
        await ctx.reply(embed=embed)

def setup(client):
  client.add_cog(Smoke(client))
