from discord.ext import commands
import discord
import random
from googleapiclient.discovery import build
import os
import json

api_key = os.environ['api_key']

def read_json(filename):
  with open(filename, 'r') as f:
    data = json.load(f)
  return data

class Order(commands.Cog):
    def __init__(self, client):
        self.bot = client
        self._last_member = None

    @commands.command(aliases=["odr"])
    async def order(self, ctx, *,search=None):
        data = read_json("blacklist.json")
        blacklisted = data["blusers"]
        if ctx.author.id in blacklisted:
          await ctx.send(f'{ctx.author.mention}, looks like ur blacklisted please contact my devs to unblacklist you.')
          return
        dataitems = read_json("banitems.json")
        banned_item = dataitems["banitems"]
        if search in banned_item:
          e = discord.Embed(title=":no_entry_sign: Sorry this item is blacklisted.",description="The item you were trying to order is in blacklisted items.")
          await ctx.send(embed=e)
          return
        if search == None:
          await ctx.send('Wrong Syntax Correct way : b!order <urdrink> example : b!order beer')
          return
        else:
          ran = random.randint(0, 9)
          resource = build("customsearch", "v1", developerKey=api_key).cse()
          result = resource.list(
            q=f"{search}", cx="3251b1acb3385e7b0", searchType="image"
            ).execute()
          url = result["items"][ran]["link"]
          embed1 = discord.Embed(title=f"<a:order:898428926530027521> Here is ur {search.title()}!",description="If the bot doesnt respond to you it is a common bug that we cant fix so please be patient and try again around 15-20 mins.")
          embed1.set_image(url=url)
          embed1.set_footer(text=f"Thanks for using BarBot!! || Requested By {ctx.author.name}")
          await ctx.reply(embed=embed1)


def setup(client):
    client.add_cog(Order(client))
