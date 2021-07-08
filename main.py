from discord.ext import commands
from discord import utils

client = commands.Bot(command_prefix='!')
TOKEN = 'PUT YOUR APPLICATIONS TOKEN INSIDE THE QUOTATION MARKS'

@client.event
async def on_ready():
    print(f'You are logged in as {client.user.name} (ID: {client.user.id})')

@client.event
async def on_message(message):
    message_content = message.clean_content
    message_content = utils.remove_markdown(message_content)

    file = open('messages.txt', 'a')
    file.write(f'{message.author.name}: {message.content}\n')

    if message.author.id == 270904126974590976:
        file2 = open('recent.txt', 'w')
        file2.write(f'{message.author.name}: {message.content}\n')

client.run(TOKEN)