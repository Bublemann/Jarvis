import discord
import os
import httpx
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

LLM_SERVER_URL = "http://localhost:8000"

class Bot(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')
        if message.content.startswith('Jarvis') or message.content.startswith('jarvis'):
            prompt = message.content[len("Jarvis "):]
            if prompt:
                async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
                    response = await client.post(LLM_SERVER_URL + "/generate", json={"prompt": prompt})
                    generatet_text = response.text
                    await message.channel.send(generatet_text)
            else:
                await message.channel.send("How can I help you? Please enter a prompt after my name.")
                
intents = discord.Intents.default()
intents.message_content = True

bot = Bot(intents=intents)
bot.run(TOKEN)