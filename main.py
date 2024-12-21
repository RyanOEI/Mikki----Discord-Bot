import discord
from discord.ext import commands
from discord import app_commands

from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True
intents.presences = True

class Mikki(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned, intents=intents)
    
    async def load_cogs(self):
        for filename in os.listdir("./Cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"Cogs.{filename[:-3]}")
    
    async def setup_hook(self):
        await self.load_cogs()
        synced_commands = await self.tree.sync()
        print(f"Synced {len(synced_commands)} commands")

def main():
    bot = Mikki()

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user} (ID: {bot.user.id}")
    
    @bot.event
    async def on_guild_join(guild: discord.Guild):
        print(f"Joined new guild: {guild.name} (ID: {guild.id})")
        synced_commands = await bot.tree.sync(guild=guild)
        print(f"Synced {len(synced_commands)} commands")
    
    bot.run(token=TOKEN)

if __name__ == "__main__":
    main()