import time
import discord
import logging
from pathlib import Path
import random
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
token = ()
client = discord.Client()
monkepath = __file__
path = Path(monkepath)
monkevids = ['monke.mp4', 'monke.mov', 'monkey.mp4', 'cool monke.mp4', 'monke generator.mp4', 'monkeyy.mp4', 'imaginemonke.jpg', 'chef.mp4', 'spin.mp4', 'child.mp4', 'dramatic.mp4', 'top10.mp4', 'panik.mp4', 'horny.mp4', 'balls.mp4', 'snow.mp4', 'bruh.mov', 'AAAAA.mov', 'toes.mp4', 'stoned.mp4', 'fresh.mp4', 'inspect.png', 'harmonica.mp4', 'brass.mp4', 'TRUNKMONKEY.mp4', 'lollipop.mov', 'schoo.mp4', 'astolfo.jpg', 'dies.mp4', 'phunky.mp4', 'fishing.mp4']
theme1 = ["eye", "wings", "monster", "dark", "teddy", "soft play area", "bugs", "water"]
theme2 = ["static", "CRT", "crumbling house", "rat", "mouse", "hamster", "teeth", "anime"]
theme3 = ["hospital", "clowns", "medical", "odd colours", "fish", "olive", "blood"]
children = 0
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(name='the screams of small children', type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'cum' in message.content.lower():
        await message.channel.send('cum :weary:')
    if message.content.startswith('std'):
        await message.channel.send('my asshole has many')
    if message.content.startswith('Astolfo, I respectfully request for consent to bustanut inside of your rectal passage'):
        await message.channel.send('yes')
    if message.content.startswith('piss'):
        await message.channel.send('let me drink your piss daddy :weary:')
    if message.content.startswith('jelly beans'):
        await message.channel.send('jelly beans', file=discord.File(str(path.parent) + '/' + 'jelly beans.mp4'))
    if message.content.startswith('help'):
        await message.channel.send('no')
    if 'pain' in message.content.lower():
        await message.channel.send('https://youtu.be/lh5oSs6K92w')
    if message.content.startswith('pee'):
        await message.channel.send('let me drink your pee daddy :weary:')
    if message.content.startswith('urine'):
        await message.channel.send('allow me to consume your urine father :weary:')
    if message.content.startswith('rip'):
        await message.channel.send('rip')
    if message.content.lower() == 'guys':
        await message.channel.send('what')
    if message.content.lower() == 'astolfo i love you':
        await message.channel.send('i love you too {}'.format(message.author.mention))
    if message.content.lower() == 'i love you astolfo':
        await message.channel.send('i love you too {}'.format(message.author.mention))
    if message.content.lower() == '$pingtest':
        await message.channel.send('{}'.format(message.author.mention))
    if message.content.lower() == 'astolfo loves us all':
        await message.channel.send('yeah i do :smiling_face_with_3_hearts:')
    if message.content.lower() == 'skeleton':
        await message.channel.send(file=discord.File(str(path.parent) + '/' + 'skeleton.gif')) #--i should probably update this but fuck you-- ok i updated it are you happy now
    if message.content.lower() == 'astolfo i hate you':                                        #ok ok i take it back i will update it soon
        await message.channel.send(':sob:')
    if message.content.lower() == 'i hate you astolfo':
        await message.channel.send(':sob:')
    if message.content.lower() == "monke":
        await message.channel.send('monke for you', file=discord.File(str(path.parent) + '/monke/' + random.choice(monkevids)))
    if "cum" in message.content.lower():
        await message.add_reaction("😩")
    if message.content.lower() == 'fs monkey':
        await message.channel.send('fs monkey', file=discord.File(str(path.parent) + '/monke/' + 'fmonkey.png'))
    if message.content.lower() == "weirdcore":
        await message.channel.send(random.choice(theme1) + ", " + random.choice(theme1) + ", " + random.choice(theme2) + ", " + random.choice(theme2) + ", " + random.choice(theme3) + ", " + random.choice(theme3))
client.run(token)
