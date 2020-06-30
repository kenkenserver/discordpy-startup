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

     embed = discord.Embed(title="embedのテスト",description="送信テスト")
     await ctx.send(embed=embed)

bot.run(token)
