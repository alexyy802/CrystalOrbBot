import os
import discord, datetime, time
import asyncio
import discord.ext
import random
import urllib.parse, urllib.request, re
from server import keep_alive
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import json

client = discord.Client()
# test

client = commands.AutoShardedBot(
    command_prefix=commands.when_mentioned_or("b!", "B!"),
    help_command=None,
    shard_count=2,
)

owner = {697323031919591454}

manager = {683555221904818194}

developer = {758290177919156244, 718868589364379699}

helper = {885681891863298069, 825633843096322108}

start_time = time.time()


@client.event
async def on_ready():
    print("Connected to bot: {}".format(client.user.name))
    print("Bot ID: {}".format(client.user.id))
    data = read_json("blacklist.json")
    client.blacklisted = data["blusers"]
    data = read_json("banitems.json")
    client.items = data["banitems"]

    servers = len(client.guilds)
    members = len(client.users)

    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f" {members} members in {servers} servers.",
        )
    )


@tasks.loop(seconds=10.0)
async def presence(client):
  servers = len(client.guilds)
  members = len(slient.users)
  await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f" {members} members in {servers} servers.",
        )
    )


async def ch_pr():
    await client.wait_until_ready()

    statuses = [
        "b!help and b!guide",
        "Thanks for 80+ servers! | b!help",
        "Family Guy :D | b!help",
    ]

    while not client.is_closed():

        status = random.choice(statuses)

        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(5)


client.loop.create_task(ch_pr())


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
print("All Cogs Loaded! 👍")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        e = discord.Embed(
            title="Internal Error!!",
            value="The command you entered was not a valid command, check b!help for a list of commands!",
        )
        e.add_field(name="Error Value :", value=f"```python3\n{error}```")
        await ctx.send(embed=e)
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(
            f"Slow down this command is in cooldown for `{error.retry_after:.2f}`seconds."
        )


@client.event
async def on_message(message):
    if message.author.bot:
        pass
    mention = f"<@!{client.user.id}>"
    if message.content == mention:
        await message.channel.send(
            "My prefix is **b!** for help run the command `b!help` and use ``b!guide`` if you need or you can ask for help in the support server, For an invite run the command `b!server`"
        )
    await client.process_commands(message)


@client.command(aliases=["si"])  # server info command
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue(),
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    await ctx.send(embed=embed)


@client.command()
@commands.is_owner()
async def reload(ctx, extension=None):
    if extension == None:
        await ctx.send("What cogs schould i reload?")
        return

    client.reload_extension(f"cogs.{extension}")
    embed = discord.Embed(
        title="Reloaded :white_check_mark:",
        description=f"{extension}.py successfully reloaded",
        color=0xFF00C8,
    )
    await ctx.send(embed=embed)


@client.command()
async def check_cogs(ctx, cog_name):
    try:
        client.load_extension(f"cogs.{cog_name}")
    except commands.ExtensionAlreadyLoaded:
        await ctx.send("Cog is loaded")
    except commands.ExtensionNotFound:
        await ctx.send("Cog not found")
    else:
        await ctx.send("Cog is unloaded")
        client.unload_extension(f"cogs.{cog_name}")


@client.command(aliases=["bi"])  # a bot info
async def botinfo(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))

    embed = discord.Embed(title=":desktop: Bot Info :desktop:")
    embed.add_field(name=":robot: Bot name", value="Bar Bot#1743")
    embed.add_field(name="<:online:898170147993440266> Status", value="Online")
    embed.add_field(
        name="<:servers:898170039595831306> Servers ", value=f"{len (client.guilds)}"
    )
    embed.add_field(name="<:members:891897587286818847> Users", value=len(client.users))
    embed.add_field(name="<:prefix:898174448916639754> Prefix", value="`b!`")
    embed.add_field(name="<:botshard:898174197119983616> Shards", value="None")
    embed.add_field(
        name="<:idcard:898173965044944916> Client ID", value="859713560774574101"
    )
    embed.add_field(name="<:uptime:898173066172051476> Uptime", value=text)
    await ctx.send(embed=embed)


@client.command()  # my support server
async def server(ctx):
    e = discord.Embed(title="")
    e.add_field(
        name="Invite me!",
        value="[Click me!](https://discord.com/api/oauth2/authorize?client_id=859713560774574101&permissions=139586817024&scope=bot%20applications.commands)",
        inline=False,
    )
    e.add_field(
        name="Website",
        value="[Click me!](https://BarBot.alexydacoder.repl.co)",
        inline=False,
    )
    e.add_field(
        name="Support Server",
        value="[Click me!](https://discord.gg/K2QND4VMVz)",
        inline=False,
    )
    await ctx.send(embed=e)


@client.command(aliases=["yt"])  # find a youtube video
async def youtube(msg, *, search):
    query_string = urllib.parse.urlencode({"search_query": search})
    html_content = urllib.request.urlopen(
        "http://www.youtube.com/results?" + query_string
    )
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    e = discord.Embed(
        title=f"<a:youtube:898490595838918656> Youtube Search For {search}",
        description="\n1. http://www.youtube.com/watch?v="
        + search_results[0]
        + "\n 2. http://www.youtube.com/watch?v="
        + search_results[1]
        + "\n3. http://www.youtube.com/watch?v="
        + search_results[2],
    )
    await msg.reply(embed=e)


@client.command(aliases=["fb"])  # send a feedback
async def feedback(ctx, *, suggestion=None):
    if ctx.author.id in client.blacklisted:
        user = discord.Member
        await ctx.send(
            f"{user.mention}, sorry but it looks like you have been blacklisted! (do b!server to join our server and ask admins there!)"
        )
        return
    if suggestion == None:
        await ctx.send(
            "Hey! there slowdown there bud, you have to give me a suggestion and not just a blank text :D"
        )
        return
    else:
        em = discord.Embed(title="Feedback Sent!")
        await ctx.send(embed=em)
        fb_channel = client.get_channel(874480088618528788)
        fck = discord.Embed(title="Feedback", description=f"{suggestion}")
        fck.set_thumbnail(url=ctx.author.avatar_url)
        fck.set_footer(
            text=f"Feedback by : {ctx.author.name}#{ctx.author.discriminator}"
        )
        await fb_channel.send(embed=fck)


@client.command(aliases=["bl"])  # blacklist a user
async def blacklist(ctx, user: discord.Member):
    if ctx.author.id in manager:
        data = read_json("blacklist.json")
        data["blusers"].append(user.id)
        write_json(data, "blacklist.json")
        e = discord.Embed(
            title=f"<:blacklist:898493775914098688> {user} Has been blacklisted",
            color=0xE67E22,
        )
        await ctx.send(embed=e)
    if ctx.author.id == 697323031919591454:
        data = read_json("blacklist.json")
        data["blusers"].append(user.id)
        write_json(data, "blacklist.json")
        e = discord.Embed(
            title=f"<:blacklist:898493775914098688> {user} Has been blacklisted",
            color=0xE67E22,
        )
        await ctx.send(embed=e)
    else:
        e = discord.Embed(
            title="Sorry you dont have the permissions ```developer``` to use this command!",
            color=0xE67E22,
        )
        await ctx.send(embed=e)


@client.command(aliases=["unbl"])  # for unblacklisting a user
async def unblacklist(ctx, user: discord.Member):
    if user is None:
        e = discord.Embed(title="Eror no value was entred!", color=0xE67E22)
        await ctx.send(embed=e)
    if ctx.author.id in manager:
        data = read_json("blacklist.json")
        data["blusers"].remove(user.id)
        write_json(data, "blacklist.json")
        e = discord.Embed(title=f"{user} Has been unblacklisted !", color=0xE67E22)
        await ctx.send(embed=e)
    if ctx.author.id == 697323031919591454:
        data = read_json("blacklist.json")
        data["blusers"].remove(user.id)
        write_json(data, "blacklist.json")
        e = discord.Embed(title=f"{user} Has been unblacklisted", color=0xE67E22)
        await ctx.send(embed=e)
    else:
        e = discord.Embed(
            title="Sorry you dont have the permissions ```developer``` to use this command!",
            color=0xE67E22,
        )
        await ctx.send(embed=e)


def read_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


def write_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["Wallet"] = 0
        users[str(user.id)]["Bank"] = 0

    with open("bank.json", "w") as f:
        json.dump(users, f)

    return True


async def get_bank_data():
    with open("bank.json", "r") as f:
        users = json.load(f)

    return users


async def update_bank(user, change=0, mode="Wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json", "w") as f:
        json.dump(users, f)
    bal = users[str(user.id)]["Wallet"], users[str(user.id)]["Bank"]
    return bal


@client.command(aliases=["bal", "Bal"])
async def balance(ctx, *, member=None):
    if member == None:
        await open_account(ctx.author)

        user = ctx.author

        users = await get_bank_data()

        wallet_amt = users[str(user.id)]["Wallet"]
        bank_amt = users[str(user.id)]["Bank"]

        em = discord.Embed(title=f"{user.name}'s balance.", color=discord.Color.red())
        em.add_field(
            name=f"Wallet Balance <a:money:891257220937945108>",
            value=wallet_amt,
            inline=False,
        )
        em.add_field(
            name="Bank <:barbank:899206420547907625>", value=bank_amt, inline=False
        )
        if ctx.author.id == 697323031919591454:
            em.add_field(
                name="Badges | Profile Badges",
                value="<:developer:891263247452372993> <:staff:891264731212550174> <:owner:891265219664437309>",
            )
        if ctx.author.id in helper:
            em.add_field(
                name="Badges | Profile Badges", value="<:Helper:898168928562475038>"
            )
        if ctx.author.id in manager:
            em.add_field(
                name="Badges | Profile Badges", value="<:manager:899209735914536961>"
            )
        em.set_thumbnail(
            url="https://images.discordapp.net/avatars/859713560774574101/a9c0ec8517ff31e32a8132678ebe3fbe.png?size=128"
        )
        await ctx.send(embed=em)
    else:
        member = discord.Member

        await open_account(member)

        user = member

        users = await get_bank_data()

        wallet_amt = users[str(user.id)]["Wallet"]
        bank_amt = users[str(user.id)]["Beer Storage"]

        em = discord.Embed(
            title=f"{member.mention}'s balance.", color=discord.Color.red()
        )
        em.add_field(
            name=f"Wallet Balance <a:money:891257220937945108>",
            value=wallet_amt,
            inline=False,
        )
        em.add_field(
            name="Beer Storage <a:dbeer:891261524478402580>",
            value=bank_amt,
            inline=False,
        )
        em.set_thumbnail(
            url="https://images.discordapp.net/avatars/859713560774574101/a9c0ec8517ff31e32a8132678ebe3fbe.png?size=128"
        )
        await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)

    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f"Someone gave you `{earnings}`$")

    users[str(user.id)]["Wallet"] += earnings

    with open("bank.json", "w") as f:
        json.dump(users, f)


@client.command(aliases=["wd"])
async def withdraw(ctx, amount=None):
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
    await update_bank(ctx.author, -1 * amount, "Bank")
    await ctx.send(f"{ctx.author.mention} You withdrew {amount} coins")


@client.command(aliases=["dp"])
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
    await update_bank(ctx.author, amount, "Bank")
    await ctx.send(f"{ctx.author.mention} You deposited {amount} coins")


@client.command(aliases=["sm"])
async def give(ctx, member: discord.Member, amount=None):
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

    await update_bank(ctx.author, -1 * amount, "Wallet")
    await update_bank(member, amount, "Bank")
    await ctx.send(f"{ctx.author.mention} You gave {member} {amount} coins")


@client.command()
async def reset_cooldown_all(ctx):
    if ctx.author.id in owner:
        beg.reset_cooldown(ctx)
        await ctx.send(
            f"{ctx.author.mention}, I have reset the cooldown of **all** commands that are set with a cooldown."
        )
    else:
        await ctx.send("Sorry only my owner can use this!")


token = os.environ["TOKEN"]

keep_alive()
client.run(token)
