#!/usr/bin/env python3
import discord
import aux
import asyncio

client = discord.Client()

discord.opus.load_opus("libopus.so.0")

@client.event
async def on_ready():
    print('Logado como {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if message.content.startswith("!hist"):
    #     msg_enviada = await message.channel.send("E")


    # print(message.author)
    # print(message.content)
    # print(message.created_at)

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

client.run(aux.get_token())
