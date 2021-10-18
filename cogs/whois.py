from discord.ext import commands
import discord

class Whois(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @commands.command(aliases=["whois"])
    async def userinfo(self, ctx, member: discord.Member = None):
     if not member:
        member = ctx.message.author
     roles = [role for role in member.roles]
     embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                            title=f"User Info - {member}")
     embed.set_thumbnail(url=member.avatar_url)
     embed.set_footer(text=f"Requested by {ctx.author}")

     embed.add_field(name="ID:", value=member.id)
     embed.add_field(name="Display Name:", value=member.display_name,inline=True)

     embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
     embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

     embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
     embed.add_field(name="Highest Role:", value=member.top_role.mention)
     await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Whois(client))
