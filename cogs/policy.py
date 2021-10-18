from discord.ext import commands
import discord

class Policy(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self._last_member = None

    @commands.command()
    async def policy(self,ctx):
        embed=discord.Embed(title=":page_with_curl: **Privacy & Policy**", description="By adding our bot to your server. You agree to have the following data collected, unless an exception was made. The data that is collected may include Guild id and usernames such as user id's. We do not sell any data that is collected.If you do not wish to follow this policy, you are not permitted to use our bot, or any of its services.")
        embed.set_footer(text="By urs truly TheOneWhoLives#4003")
        await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Policy(client))
