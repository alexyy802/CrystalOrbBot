import discord
from discord.ext import commands
import json

def read_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


def write_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["disable-mod"])
    @commands.has_permissions(administrator=True)
    async def disable_mod(self,ctx):
      guild = ctx.guild
      data = read_json("db/autoserver.json")
      automod = data["autoserver"]
      if guild.id not in automod:
        await ctx.send('You did not enable automod yet! <a:nono:900278651906572288>')
        return
      guild = ctx.guild
      data = read_json("db/autoserver.json")
      data["autoserver"].remove(guild.id)
      write_json(data, "db/autoserver.json")
      await ctx.send('Automod disabled! <a:checkmark:900276103942377472>')
    
    @commands.command(aliases=["enable-mod"])
    @commands.has_permissions(administrator=True)
    async def enable_mod(self,ctx):
      guild = ctx.guild
      data = read_json("db/autoserver.json")
      automod = data["autoserver"]
      if guild.id in automod:
        await ctx.send('Automod has already been enabled in this server! <a:nono:900278651906572288>')
        return

      data = read_json("db/autoserver.json")
      data["autoserver"].append(guild.id)
      write_json(data, "db/autoserver.json")
      await ctx.send('Automod enabled! <a:checkmark:900276103942377472>')

    @commands.command(name="enable-autolink")
    async def enable_link(self,ctx):
      guild = ctx.guild
      data = read_json("db/antilink.json")
      antilink = data["antilink"]
      if guild.id in antilink:
        await ctx.send('Anti Link has already been enabled in this server! <a:nono:900278651906572288>')
        return
      
      data = read_json("db/antilink.json")
      data["antilink"].append(guild.id)
      write_json(data, "db/antilink.json")
      await ctx.send('Anti link enabled! <a:checkmark:900276103942377472>')
      return

    @commands.command(name="disable-autolink")
    async def disable_link(self,ctx):
      guild = ctx.guild
      data = read_json("db/antilink.json")
      antilink = data["antilink"]
      if guild.id not in antilink:
        await ctx.send('Anti Link is not active in this server! <a:nono:900278651906572288>')
        return
      
      data = read_json("db/antilink.json")
      data["antilink"].append(guild.id)
      write_json(data, "db/antilink.json")
      await ctx.send('Anti link disabled! <a:checkmark:900276103942377472>')
      return


def setup(bot):
  bot.add_cog(Settings(bot))
