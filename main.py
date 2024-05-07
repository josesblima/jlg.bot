import discord
from key import KEY
import asyncio
from get_response import Responder

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)
#responder_class = Responder()

@client.event
async def on_ready():
    global responder_class
    print('We have logged in as {0.user}'.format(client))
    responder_class = Responder()

@client.event
async def on_message(message):
    global responder_class

    if message.author == client.user:
        return

    response = await responder_class.get_response(message)
    if (response):
        await message.channel.send(response)

client.run(KEY)
