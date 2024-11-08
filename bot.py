import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('MTMwMzM4NzEzOTEyMzQ0OTkzNw.Ga3B9p.nN8DXHKsY6tFOLC3MoEIpqbQcKozKuWldz4iHs')

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Load the math cog
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    bot.load_extension("cogs.math_cog")

bot.run(TOKEN)
