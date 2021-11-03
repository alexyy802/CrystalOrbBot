import discord
from discord.ext import commands
import asyncio
import json

def read_json(filename):
    with open(filename, "r") as f:
      data = json.load(f)
    return data


def write_json(data, filename):
    with open(filename, "w") as f:
      json.dump(data, f, indent=4)

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
      server = message.guild
      data = read_json("db/autoserver.json")
      automod = data["autoserver"]
      data = read_json("db/antilink.json")
      antilink = data["antilink"]
      if server.id in automod:
        banword=[
        'fuck',
        'Fuck',
        'FUCKING',
        'Bitch',
        'BITCH',
        'asshole',
        'Trash',
        'trash',
        'nigga',
        'ASSHOLE',
        'Nigga',
        'FUCK',
        'Fucking',
        'SHIT',
        'shit',
        'Shit',
        'NIGGA'
        ]

        if message.content in banword:
          await message.delete()
          await message.channel.send(message.author.mention+", Hey! that word isnt allowed in here!")
          return
      if server.id in antilink:
        if message.content.startswith('https://'):
          await message.delete()
          await message.channel.send(message.author.mention+", Hey! links are not allowed in this server!")
          return
        else:
          return

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,* ,user:discord.Member=None):
      if user == None:
        await ctx.send('Mention a member before using this command to ban someone!')
      else:
        try:
          await user.ban()
          await ctx.send(f'{user} has been banned.')
          if user == ctx.author.bot:
            return
          else:
            await user.send(f'You were banned from {ctx.guild}')
            return
        except:
          await ctx.send('Couldnt ban that member...')
          return
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def kick(self,ctx,* ,user:discord.Member=None):
      if user == None:
        await ctx.send('Mention a member before using this command to ban someone!')
      else:
        try:
          await user.ban()
          await ctx.send(f'{user} has been kicked.')
          if user == ctx.author.bot:
            return
          else:
            await user.send(f'You were banned for {ctx.guild}')
            return
        except:
          await ctx.send('Couldnt ban that member...')
          return
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def lock(self,ctx,* ,channel : discord.TextChannel=None):
      channel = channel or ctx.channel
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = False
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      await ctx.send('Channel locked. :lock:')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unlock(self,ctx,* ,channel:discord.TextChannel=None):
      channel = channel or ctx.channel
      overwrite = channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      await ctx.send('Channel unlocked. :unlock:')
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, id: int):
      try:
        user = await self.client.fetch_user(id)
        await ctx.guild.unban(user)
        await ctx.send(f'{user} has been unbanned.')
      except:
        await ctx.send('Couldnt unban that member.')
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        amount = amount + 1
        if amount > 101:
            e = discord.Embed(title="<:error:902425347767820298> You are over the purge limit! the max limit is 100 messages",colour=discord.Color.red())
            return await ctx.send(embed=e)
        else:
            await ctx.channel.purge(limit=amount)
            msg = await ctx.send(f"Cleared {amount} Messages.")
            await asyncio.sleep(3)
            await msg.delete()
  

def setup(bot):
  bot.add_cog(Moderation(bot))
