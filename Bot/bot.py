import discord
from discord.ext import commands 

# --- Подключение конфигов ---

import load_configs

CONFIG = load_configs.load()

# --- Инциализация клиента ---

client = commands.Bot(command_prefix = CONFIG["prefix"], case_insensitive= 1)
extensions = ['handler']

@client.event
async def on_ready():
    print("Client started!")

# --- Запуск ---

if __name__ == '__main__':
    
    # --- подключение расширений ---    

    for extension in extensions:
        try:
            client.load_extension(extension)

        except Exception as error:
            print(f'{extension} --- {error}')

    client.run(CONFIG['token'])

