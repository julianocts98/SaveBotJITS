#!/usr/bin/env python3
import discord
import aux
import asyncio
import logger

client = discord.Client()

#biblioteca que possibilita o envio de som
discord.opus.load_opus("libopus.so.0")

@client.event
async def on_ready():
    print('Logado como {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("-jstop"):
        if(client.voice_clients):
            for voclient in client.voice_clients:
                if voclient.channel == message.author.voice.channel:
                    await voclient.disconnect()

    if any(palavra in message.content for palavra in ["-cheiro", "-pneu"]):
        channel = message.channel
        await channel.send("Você quis dizer: ")
        await channel.send("1 - Cheiro de somebody that I used to know?")
        await channel.send("2 - Cheiro de say so?")

        def check(m):
            return ( m.content.startswith("1") or m.content.startswith("2") or m ) and m.channel == channel

        try:
            msg = await client.wait_for('message', timeout=10, check=check)
        except asyncio.TimeoutError:
            await channel.send("Achei que era comigo ;-;")
        else:
            await channel.send("Para parar de tocar, digite \"-jstop\" :) ")

        if msg.content.startswith("1"):
            voice_client = await message.author.voice.channel.connect()
            def my_after(error):
                coro = voice_client.disconnect()
                fut = asyncio.run_coroutine_threadsafe(coro, client.loop)
                try:
                    fut.result()
                except:
                    # an error happened sending the message
                    pass
            source = discord.FFmpegOpusAudio("audios/cheiro_somebody.mp3")
            voice_client.play(source, after=my_after)

        if msg.content.startswith("2"):
            voice_client = await message.author.voice.channel.connect()
            def my_after(error):
                coro = voice_client.disconnect()
                fut = asyncio.run_coroutine_threadsafe(coro, client.loop)
                try:
                    fut.result()
                except:
                    # an error happened sending the message
                    pass
            source = discord.FFmpegOpusAudio("audios/cheiro_say_so.mp3")
            voice_client.play(source, after=my_after)


    if message.content.startswith("história da JITS"):
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

#executa o bot
client.run(aux.get_token())
