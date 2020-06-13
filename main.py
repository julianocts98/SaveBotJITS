#!/usr/bin/env python3
import discord
import aux
import asyncio

client = discord.Client()

discord.opus.load_opus("libopus.so.0")

@client.event
async def on_ready():
    print('Logado como {0.user}'.format(client))
    #joao = discord.utils.find(lambda m: m.name == 'João Vittor', client.get_guild(98846974278664192))
    #print(joao)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!!!tururu"):
        voice_client = await message.author.voice.channel.connect()
        def my_after(error):
            coro = voice_client.disconnect()
            fut = asyncio.run_coroutine_threadsafe(coro, client.loop)
            try:
                fut.result()
            except:
                # an error happened sending the message
                pass
        source = discord.FFmpegOpusAudio("audios/tururu.mp3")
        voice_client.play(source, after=my_after)

@client.event
async def on_voice_state_update(member, before, after):
    if member.id == 110036152009912320 and before.channel==None: #id do usuario que deletou o chat
        for channel in client.get_all_channels():
            if type(channel) == discord.channel.TextChannel:
                await channel.send(file=discord.File("imgs/shamegot.jpg"))
        voice_client = await after.channel.connect()
        def my_after(error):
            coro = voice_client.disconnect()
            fut = asyncio.run_coroutine_threadsafe(coro, client.loop)
            try:
                fut.result()
            except:
                # an error happened sending the message
                pass
        source = discord.FFmpegOpusAudio("audios/shame.mp3")
        voice_client.play(source, after=my_after)
client.run(aux.get_token())
