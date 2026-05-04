import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()
import random as rdm


TOKEN = os.getenv("DISCORD_TOKEN")

# Token check
if not TOKEN:
    raise ValueError("DISCORD_TOKEN is null")

# Intents (required to read messages and members)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # needed for selecting users

# Create bot instance
bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None # To show my own help
)

# BOT READY EVENT
@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")

# HELP COMMAND
@bot.command()
async def help(ctx):
    """Shows available commands"""
    help_text = """
**Bot Commands:**
`!help` → Show this message  
`!hello` → Simple greeting  
`!friends` → Pick 2 random friends from the server  
`!random [min] [max]` → Generate a random number (default: 1-10000)
"""
    await ctx.send(help_text)


# HELLO COMMAND: Say Hello World
@bot.command()
async def hello(ctx):
    """Simple hello world command"""
    await ctx.send("Hello World 👋")


# FRIENDS COMMAND: search two random members as friends
@bot.command()
async def friends(ctx):
    """Selects 2 random members from the server"""
    members = [member for member in ctx.guild.members if not member.bot]

    if len(members) < 2:
        await ctx.send("Not enough members to pick friends.")
        return

    selected = rdm.sample(members, 2)

    await ctx.send(
        f"👬 Friends picked: {selected[0].mention} ❤️ {selected[1].mention}"
    )

# RANDOM NUMBER COMMAND: generate random number
@bot.command()
async def random(ctx, min_value: int = 1, max_value: int = 10000):
    """Generates a random number between min and max"""
    
    if min_value > max_value:
        await ctx.send("Invalid range: min is greater than max.")
        return

    number = rdm.randint(min_value, max_value)

    await ctx.send(f"🎲 Random number: {number}")


# RUN BOT
bot.run(TOKEN)