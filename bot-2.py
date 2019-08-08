import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import asyncio
import requests
import os

TOKEN = 'NjA4MTg0ODczNDkyMDIxMjg4.XUklBw.3kOz9OlwsOmHJQRCt4RV3DYH4BU'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.idle, activity = discord.Game("Смотрит за сервером"))
	print("Bot is ready")

@client.event
async def on_member_join(member):
	print(f'{member} Зашел на сервiр!')

@client.event
async def on_member_left(member):
	print(f'{member} Покинул нас :(')

@client.command()
async def ping(ctx):
	await ctx.send(f'Ping - {round(client.latency * 1000)} ms')

@client.command(aliases=['q'])
async def _q(ctx, *, question=''):
	responses = ['Да',
	             'Нет',
	             'Наверное',
	             'Думаю, нет',
	             'Думаю, да',
	             'Возможно',
	             'Привет',
	             'Ты кто',
	             'Соси',
	             'Сам бот, сука',
	             'Ты дурачек?',
	             'Я не бот атвечаю',
	             'Хорошо',
	             'Нормально)',
	             'Я чесно не бот',
	             'Кто бот, я бот? А может быть ты бот?']

	if question != '':

		await ctx.send(f'{random.choice(responses)}')
		
	else:
	
		await ctx.send('Вы не задали вопроса?')

@client.command()
async def clear(ctx, amount=5):
	await ctx.channel.purge(limit = int(amount))
	await ctx.send(f'Удалено {amount} сообщений')


@client.command()
async def kick(ctx, member : discord.Member, *, reason = None):
	await member.kick(reason=reason)
	await ctx.send(f'Подлый {member} был кикнут.')


@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
	await member.ban(reason=reason)
	await ctx.send(f'Подлый {member} был забанен.')

@client.command()
async def unban(ctx, *, member):

    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:

        user = ban_entry.user

        await ctx.guild.unban(user)

        await ctx.send(f'Разбанен - {user.mention}')

@client.event
async def on_member_join(member):
	role = discord.utils.get(member.guild.roles, name = 'Участник •')
	await member.add_roles(role, atomic=True)



client.run(str(os.environ.get('TOKEN')))
