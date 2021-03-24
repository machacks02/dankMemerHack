import discord

client = discord.Client()

@client.event
async def on_ready():
    print('You are logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    file = open('messages.txt', 'a')
    file.write(message.author.name + ': ' + message.content + '\n')
    if message.author.name == 'Dank Memer':
        file2 = open('recent.txt', 'w')
        file2.write(message.author.name +': ' + message.content)

client_secret = 'PUT YOUR CLIENT SECRET HERE'

client.run(client_secret)
