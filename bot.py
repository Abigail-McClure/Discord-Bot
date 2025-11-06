import discord
import requests
import json
import os
import asyncio
import random

TENOR = os.environ["TENOR_API_KEY"]
TOKEN = os.environ["DISCORD_TOKEN"]

#deafult parameter is meme
def get_gif(query="meme"):
    try:
        r = requests.get(
            "https://tenor.googleapis.com/v2/search",
            params={"q": query, "key": TENOR, "limit": 25, "media_filter": "gif,tinygif"},
            timeout=(3,8),
        )
        r.raise_for_status()
        results = r.json().get("results", [])
        if not results: return None
        urls = []
        for item in results:
            mf = item.get("media_formats", {})
            # prefer the full GIF; if that’s missing, use the tiny GIF; if neither exists, use an empty dict so we don’t crash
            url = (mf.get("gif") or mf.get("tinygif") or {}).get("url")
            if url:
                urls.append(url)

        # pick a random url and return it
        return random.choice(urls) if urls else None

    except Exception as e:
        print("get_gif error:", repr(e))
        return None

def get_meme():
    try:
        r = requests.get(
            'https://meme-api.com/gimme',
            timeout=(3, 8)  # (connect timeout, read timeout)
        )
        r.raise_for_status()
        data = r.json()
        return data.get("url")
    except Exception as e:
        print("get_meme error:", repr(e))
        return None



class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):
        if message.author.bot:
            return
        if message.content.startswith("$gif"):
            # use whatever comes after $gif to search for a gif or default to a random meme from tenor
            q = message.content[len("$gif"):].strip() or "meme"
            url = await asyncio.to_thread(get_gif, q)
            await message.channel.send(url or "No gif right now ")

        # default to tenor gif if reddit api doesn't work
        elif message.content.startswith("$meme"):
            url = await asyncio.to_thread(get_meme)
            if not url:
                url = await asyncio.to_thread(get_gif)
            await message.channel.send(url or "Couldn't fetch a meme right now")
            return

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
