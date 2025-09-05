import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user} (id: {bot.user.id})")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hey {ctx.author.mention}! 📚")

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    if not TOKEN:
        print("❌ ERROR: No DISCORD_TOKEN found. Set it in Railway Variables.")
    else:
        bot.run(TOKEN)
