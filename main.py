#!/usr/bin/env python3
import discord
import aux

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logado como {0}!'.format(self.user))

client = MyClient()
client.run(aux.get_token())
