import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="mp!",help_command=None)

@client.event
async def on_ready():
  print('CrystalOrb Bot online.')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
      client.load_extension(f"cogs.{filename[:-3]}")
print("All Cogs Loaded! 👍")

@client.command()
async def policy(ctx):
  e=discord.Embed(title=":page_with_curl:**Privacy & Policy**",description="By adding our bot to your server. You agree to have the following data collected, unless an exception was made. The data that is collected may include Guild id and usernames such as user id's. We do not sell any data that is collected.If you do not wish to follow this policy, you are not permitted to use our bot, or any of its services.")
  e.set_footer(text="By urs truly TheOneWhoLives#4003")
  await ctx.send(embed=e)

token = os.environ["TOKEN"]

client.run(token)
