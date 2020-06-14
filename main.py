#!/usr/bin/env python3
from __future__ import unicode_literals
import discord
import aux
import asyncio
import youtube_dl


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

    if message.content.startswith("-shame"):
        channel = message.channel
        await channel.send(file=discord.File("imgs/shamegot.jpg"))
        voice_client = await message.author.voice.channel.connect()
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
            if ( msg.content.startswith("1") or msg.content.startswith("2") ):
                await channel.send("Para parar de tocar, digite \"-jstop\" :) ")
            else:
                await channel.send("Infelizmente não tenho tantas opções de pneu queimado :(")
                await channel.send("Use o comando -cheiro ou -pneu novamente caso queira ouvir alguma das disponíveis :) ")


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

    if message.content.startswith("-yt"):
        conteudo = message.content[4:]
        channel = message.channel

        url = conteudo

        ydl_opts = {
            'default_search' : 'ytsearch',
            'format': 'bestaudio/best',
            'postprocessors':
                [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            'outtmpl' : 'audios/youtube-dl.%(ext)s'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        voice_client = await message.author.voice.channel.connect()
        def my_after(error):
            coro = voice_client.disconnect()
            fut = asyncio.run_coroutine_threadsafe(coro, client.loop)
            try:
                fut.result()
            except:
                # an error happened sending the message
                pass
        source = discord.FFmpegOpusAudio("audios/youtube-dl.mp3")
        voice_client.play(source, after=my_after)

#executa o bot
client.run(aux.get_token())
