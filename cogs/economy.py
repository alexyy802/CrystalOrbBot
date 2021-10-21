import discord
import json
from discord.ext import commands
import random

async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("bank.json", "w") as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open("bank.json", "r") as f:
        users = json.load(f)

    return users


async def update_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json", "w") as f:
        json.dump(users, f)
    bal = users[str(user.id)]["wallet"], users[str(user.id)]["bank"]
    return bal

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def balance(self,ctx):
        await open_account(ctx.author)

        user = ctx.author

        users = await get_bank_data()

        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        em = discord.Embed(title=f"{user.name}'s balance.", color=discord.Color.red())
        em.add_field(
            name=f"Wallet <a:money:891257220937945108>",
            value=wallet_amt,
            inline=False,
        )
        em.add_field(
            name="Bank <:barbank:899206420547907625>", value=bank_amt, inline=False
        )
        em.set_thumbnail(
            url="https://images.discordapp.net/avatars/859713560774574101/a9c0ec8517ff31e32a8132678ebe3fbe.png?size=128"
        )
        await ctx.send(embed=em)
    
    @commands.command()
    async def beg(self,ctx):
      await open_account(ctx.author)

      user = ctx.author

      users = await get_bank_data()

      earnings = random.randrange(101)

      await ctx.send(f"Someone gave you `{earnings}`$")

      users[str(user.id)]["wallet"] += earnings

      with open("bank.json", "w") as f:
          json.dump(users, f)
    
    @commands.command(aliases=["with"]) 
    async def withdraw(self,ctx,* ,amount=None):
      await open_account(ctx.author)
      if amount == None:
          await ctx.send("Please enter the amount")
          return

      bal = await update_bank(ctx.author)

      amount = int(amount)

      if amount > bal[1]:
          await ctx.send("You do not have sufficient balance")
          return
      if amount < 0:
          await ctx.send("Amount must be positive!")
          return

      await update_bank(ctx.author, amount)
      await update_bank(ctx.author, -1 * amount, "bank")
      await ctx.send(f"{ctx.author.mention} You withdrew {amount} coins")


    @commands.command(aliases=["dep"])
    async def deposit(ctx, amount=None):
      await open_account(ctx.author)
      if amount == None:
          await ctx.send("Please enter the amount")
          return

      bal = await update_bank(ctx.author)

      amount = int(amount)

      if amount > bal[0]:
          await ctx.send("You do not have sufficient balance")
          return
      if amount < 0:
          await ctx.send("Amount must be positive!")
          return

      await update_bank(ctx.author, -1 * amount)
      await update_bank(ctx.author, amount, "bank")
      await ctx.send(f"{ctx.author.mention} You deposited {amount} coins")
    
    @commands.command()
    async def give(self,ctx,member:discord.Member,* ,amount=None):
      await open_account(ctx.author)
      await open_account(member)
      if amount == None:
          await ctx.send("Please enter the amount")
          return

      bal = await update_bank(ctx.author)
      if amount == "all":
          amount = bal[0]

      amount = int(amount)

      if amount > bal[0]:
          await ctx.send("You do not have sufficient balance")
          return
      if amount < 0:
          await ctx.send("Amount must be positive!")
          return

      await update_bank(ctx.author, -1 * amount, "wallet")
      await update_bank(member, amount, "bank")
      await ctx.send(f"{ctx.author.mention} You gave {member} {amount} coins")

def setup(client):
  client.add_cog(Economy(client))
