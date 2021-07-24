from discord.ext import commands
import json
import os
load = json.load(open(os.path.join(os.path.dirname(__file__), 'config.json'),"r"))

client = commands.Bot(command_prefix='!')
TOKEN = load['TOKEN']

@client.event
async def on_ready():
    print(f'You are logged in as {client.user.name} (ID: {client.user.id})')

@client.event
async def on_message(message):
    if message.author.id == 270904126974590976:
        file2 = open(os.path.join(os.path.dirname(__file__), "recent.txt"), 'w')
        file2.write(f'{message.author.name}: {message.content}\n')

client.run(TOKEN)
