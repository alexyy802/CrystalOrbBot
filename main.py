import discord
from discord.ext import commands
import os
from discord.ext.commands import CommandNotFound, MissingPermissions

intents = discord.Intents.all()

client = discord.Client(intents=intents)

client = commands.Bot(command_prefix="mp!",help_command=None)

@client.event
async def on_ready():
  print('CrystalOrb Bot online.')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      client.load_extension(f"cogs.{filename[:-3]}")
print("All Cogs Loaded! 👍")

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, MissingPermissions):
    await ctx.send(f'{ctx.author.mention}, hey you dont have permissions to use this command! <a:nono:900278651906572288>')
    return
  if isinstance(error, CommandNotFound):
    await ctx.send('I dont seem to know that command <:CONFUSION:900280334787166248>')
    return

@client.command()
async def policy(ctx):
  e=discord.Embed(title=":page_with_curl:**Privacy & Policy**",description="By adding our bot to your server. You agree to have the following data collected, unless an exception was made. The data that is collected may include Guild id and usernames such as user id's. We do not sell any data that is collected.If you do not wish to follow this policy, you are not permitted to use our bot, or any of its services.")
  e.set_footer(text="By urs truly TheOneWhoLives#4003")
  await ctx.send(embed=e)

token = os.environ["TOKEN"]

client.run(token)
