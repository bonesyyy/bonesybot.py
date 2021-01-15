#importing tools
import discord
import random
import logging
import os
import discord.utils
from discord.utils import get
from discord.ext import commands



logging.basicConfig(level=logging.INFO)

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='with your feelings'))
    print('Bot is ready. lol')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Your ping is {round(client.latency * 1000)}ms')

@client.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)

@client.command(aliases =['8ball'])
async def _8ball(ctx, *, questions):
    response = ['As Daiko sees it, yes.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don’t count on it.',
                'It is certain.',
                'It is decidedly so.',
                'Most likely.',
                'Daiko\'s reply is no.',
                'Daiko\'s sources say no.',
                'Outlook not so good.',
                'Outlook good.',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Daiko says Yes.',
                'Yes - definitely says Daiko',
                'You may rely on it',
                ]
    await ctx.send(f'Question: {questions}\nAnswer: {random.choice(response)}')

@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('You forgot to type in something!')



@client.command()
async def accept(ctx, member : discord.Member, amount=2):
    role_name = 'Players'
    if ctx.author.guild_permissions.administrator:
        role = get(member.guild.roles, name=role_name)
        await ctx.channel.purge(limit=amount)
        await member.add_roles(role)
        channel = client.get_channel(770282902151364661)
        await channel.send(f'Welcome {member.mention}!')
    if not ctx.author.guild_permissions.administrator:
        await ctx.send(f'You don\'t have permission to do that!')



client.run(os.environ['token'])

