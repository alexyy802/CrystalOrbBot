from pistonapi import PistonAPI
import discord
from discord.ext import commands

piston = PistonAPI()

class CodeCompiler(commands.Cog):
  def __innit__(self,bot):
    self.bot = bot

  @commands.command()
  async def run(self,ctx,n,* ,code):
    nm = n.lower()
    a = code.replace("```","")

    if nm == "bh":
      b = (piston.execute(language="bash",version="5.1.0",code=a))
      c = str(b)
      em = discord.Embed(title="Bash Code Run",description=f"```bash\nOutput:\n{c}```")
      await ctx.send(embed=em)
      return
    if nm == "jav":
      b = (piston.execute(language="java",version="15.0.2",code=a))
      c = str(b)
      em = discord.Embed(title="Java Code Run",description=f"```java\nOutput:\n{c}```",colour=discord.Color.blue())
      await ctx.send(embed=em)
      return
    elif nm == "py":
      b = (piston.execute(language="python",version="3.10.0",code=a))
      c = str(b)
      em = discord.Embed(title="Python Code Run",description=f"```py\nOutput:\n{c}```",colour=discord.Color.blue())
      await ctx.send(embed=em)
      return
    else:
      await ctx.send(f'{ctx.author.mention}, The Programming Language you provided is not supported yet!')
      return
    
  @commands.command()
  async def help_run(self,ctx):
    e = discord.Embed(colour=discord.Color.blue())
    e.add_field(name="INFORMATION",value="Please remember that this command is only for code executing and not an eval command so dont even try to use it for bad!")
    e.add_field(name="Language codes",value="```yaml\nBash = bh\n \nPython = py\n \nJava = jav\n")
    e.set_footer(text="More languages coming soon!")

def setup(bot):
  bot.add_cog(CodeCompiler(bot))
