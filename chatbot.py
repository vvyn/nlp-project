import discord
from dotenv import load_dotenv
import os
import logging
import requests

load_dotenv('.env.local')

# lets bot subscribe to bucket of events
# intents = discord.Intents.default()
# intents.message_content = True
intents = discord.Intents(messages=True, guilds=True, reactions=True)

# connection to discord
client= discord.Client(intents=intents)

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    # don't want own messages
    if message.author == client.user:
        return

    if message.content.startswith('$foodie'):
        await message.channel.send('Hello!')

def rec_food(query):
    if 'fishy' in query:
        return 'sushi, salmon, or cod'
    elif 'sweet' in query:
        return 'cheesecake, cherries, or chocolate'
    else:
        'how about something fishy?'

client.run(os.getenv('BOT_TOKEN'), log_handler=handler)
