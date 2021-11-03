import discord
from discord.ext import commands
import os
from server import server

bot = commands.Bot(command_prefix='c.',help_command=None)

bot.lava_nodes = [
      {
        'host': 'owo.lonk',
        'port': pog,
        'rest_uri': 'http://owo.lonk:10010',
        'password': 'Nodepassword123lolpog:o',
        'identifier': 'MAIN MUSIC',
        'region': 'ea town'
      }
    ]

bot.load_extension('dismusic')

@bot.event
async def on_ready():
  print('Logged in!')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="c.help for help! :D"))

for filename in os.listdir("./src"):
  if filename.endswith(".py"):
    bot.load_extension(f"src.{filename[:-3]}")
  print("All was loaded! 👍")


@bot.event
async def on_message(message):
  mention = f"<@!{bot.user.id}>"
  if message.content == mention:
    e = discord.Embed(title=f"Hello! my name is {bot.user}! you can use `c.help` for my help command!",colour=discord.Color.blue())
    await message.channel.send(embed=e)
  await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingPermissions): 
    await ctx.send(f'{ctx.author.mention}, hey you dont have permissions to use this command! <:redCross:902465119534080001>', delete_after=5.0)
    return
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('I dont seem to know that command <:CONFUSION:900280334787166248>', delete_after=5.0)
    await ctx.message.add_reaction("<:LC_QuestionMark:902424772913287208>")
    return
  raise error

@bot.command()
async def support(ctx):
      e = discord.Embed(colour=discord.Color.blue())
      e.add_field(name="Invite me!",value="[Click me!](https://discord.com/api/oauth2/authorize?client_id=899838782994546698&permissions=8&scope=bot%20applications.commands)",inline=False)
      e.add_field(name="Website",value="[Click me!](https://crystalorb.alexydacoder.repl.co)",inline=False)
      e.add_field(name="Support Server",value="[Click me!](https://discord.gg/K2QND4VMVz)",inline=False)
      await ctx.send(embed=e)

@bot.command()
async def invite(ctx):
      e = discord.Embed(colour=discord.Color.blue())
      e.add_field(name="Invite me!",value="[Click me!](https://discord.com/api/oauth2/authorize?client_id=899838782994546698&permissions=8&scope=bot%20applications.commands)",inline=False)
      e.add_field(name="Website",value="[Click me!](https://crystalorb.alexydacoder.repl.co)",inline=False)
      e.add_field(name="Support Server",value="[Click me!](https://discord.gg/K2QND4VMVz)",inline=False)
      await ctx.send(embed=e)

token = os.environ['token']
server()
bot.run(token)
