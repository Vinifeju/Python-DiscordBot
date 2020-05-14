import discord
from discord.ext import commands


# --- Подключение нужных модулей ---

import requests

class Handler(commands.Cog):
	def __init__(self, client):
		self.client = client

	# --- Обработка комманд ---

	@commands.command()
	async def ping(self, ctx):
		await ctx.send('Pong!')

	@commands.command()
	async def ascii(self, ctx, *text):
		if len(text) == False:
			text = ('Hello', 'World')

		get_parameter = '+'.join(text)
		response = requests.get(f'http://artii.herokuapp.com/make?text={get_parameter}')
		
		await ctx.send(f'``` {response.text} ```')

def setup(client):
	client.add_cog(Handler(client))