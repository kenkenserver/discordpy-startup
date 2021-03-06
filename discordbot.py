from discord.ext import commands
import os
import discord
import traceback

bot = commands.Bot(command_prefix='k!')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def test(ctx):
    await ctx.send('テスト')

@bot.command()
async def embed(ctx):
     embed = discord.Embed(title="embedのテスト",description="送信テスト",color=discord.Colour.from_rgb(177,215,255))
     embed.add_field(name="フィールドのテスト",value="送信テスt(ry")
     embed.set_thumbnail(url="https://m.box.com/file/685787952461/download?shared_link=https%3A%2F%2Fapp.box.com%2Fs%2Frq225l0odgu7ed6w6isgsb713sskbmvy")
     await ctx.send(embed=embed)

@bot.command()
async def say(ctx, arg):
       await ctx.send(arg)

@bot.command()
async def emsay(ctx, arg):
     embed = discord.Embed(description=arg)
     await ctx.send(embed=embed)

@bot.command()
async def emsayc(ctx, arg1, arg2, arg3, arg4):
     embed = discord.Embed(description=arg1,color=discord.Colour.from_rgb(arg2,arg3,arg4))
     await ctx.send(embed=embed)

bot.run(token)
