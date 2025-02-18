import discord
from discord.ext import commands
import httpx
import asyncio
import os

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

async def generate_response(prompt):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://llm_server:8000/generate", json={"prompt": prompt})
        return response.json()["response"]

@bot.command()
async def ask(ctx, *, prompt):
    await ctx.send("Thinking... 🤔")
    response = await generate_response(prompt)
    await ctx.send(f"🤖 Answer: {response}")

bot.run(TOKEN)