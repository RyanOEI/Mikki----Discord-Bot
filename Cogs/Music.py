import discord
from discord.ext import commands
from discord import app_commands

from yt_dlp import YoutubeDL

class Song():
    def __init__(self):
        self.name: str = None
        self.duration: int = None
        self.url = None
        self.channel = None
        self.thumbnail = None
    
    def formated_duration(self):
        pass

class player():
    def __init__(self):
        pass

class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is ready!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot=bot))