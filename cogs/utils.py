import discord
from discord.ext import commands
import asyncio
import aiohttp
from io import BytesIO
import json

def read_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


def write_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

class Utils(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command()
    async def remoji(self, ctx, emoji: discord.Emoji):
        guild = ctx.guild
        if ctx.author.guild_permissions.manage_emojis:
            await ctx.send(f'{emoji} Has been deleted')
            await emoji.delete()

    @commands.command()
    async def addemoji(sef,ctx,url:str,* ,name):
     guild = ctx.guild
     async with aiohttp.ClientSession() as ses:
       async with ses.get(url) as r:
         try:
          imgorgif = BytesIO(await r.read())
          evalue = imgorgif.getvalue()
          if r.status in range(200, 299):
            emoji = await guild.create_custom_emoji(image=evalue, name=name)
            await ctx.send('Emoji Added.')
            await ses.close()
          else:
            await ctx.send('Sorry, something went wrong while processing this emoji.')
         except discord.HTTPException:
          await ctx.send('The File seems to be too large :/')
    
    @commands.command(aliases=["disable-mod"])
    @commands.has_permissions(administrator=True)
    async def disable_mod(self,ctx):
      guild = ctx.guild
      data = read_json("autoserver.json")
      automod = data["autoserver"]
      if guild.id not in automod:
        await ctx.send('You did not enable automod yet! <a:nono:900278651906572288>')
        return
      guild = ctx.guild
      data = read_json("autoserver.json")
      data["autoserver"].remove(guild.id)
      write_json(data, "autoserver.json")
      await ctx.send('Automod disabled! <a:checkmark:900276103942377472>')
    
    @commands.command(aliases=["enable-mod"])
    @commands.has_permissions(administrator=True)
    async def enable_mod(self,ctx):
      guild = ctx.guild
      data = read_json("autoserver.json")
      automod = data["autoserver"]
      if guild.id in automod:
        await ctx.send('Automod has already been enabled in this server! <a:nono:900278651906572288>')
        return

      data = read_json("autoserver.json")
      data["autoserver"].append(guild.id)
      write_json(data, "autoserver.json")
      await ctx.send('Automod enabled! <a:checkmark:900276103942377472>')

def setup(client):
  client.add_cog(Utils(client))
