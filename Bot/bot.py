import discord
from discord.ext import commands 

# --- config ---

import load_configs

CONFIG = load_configs.load()

# --- client ---

client = commands.Bot(command_prefix = CONFIG["prefix"], case_insensitive= 1)
extensions = ['handler']

@client.event
async def on_ready():
    print("Client started!")

@client.command()
async def load(extension):
    try:
        client.load_extension(extension)

    except Exception as error:
        print(f'{extension} --- {error}')



# --- run ---

if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)

        except Exception as error:
            print(f'{extension} --- {error}')

    client.run(CONFIG['token'])

