import discord
from discord.ext import commands
from discord import app_commands

from dataclasses import dataclass

from yt_dlp import YoutubeDL
from enum import Enum
from collections import deque
import random

@dataclass
class Song:
    title: str
    url: str
    channel_name: str
    channel_url: str
    duration: float
    thumbnail_url: str

class Player():
    class PlayerState(Enum):
        STOPPED = 0
        PLAYING = 1
        PAUSED = 2
    
    class RepeatMode(Enum):
        OFF = 0
        ONE = 1
        ALL = 2

    def __init__(self, guild_id: int = None, voice_channel_id: int = None, text_channel_id: int = None):
        self.guild_id: int = guild_id
        self.voice_channel_id: int = voice_channel_id
        self.text_channel_id: int = text_channel_id

        self.queue = deque()
        self.history = []

        self.current = None

        self.state = self.PlayerState.STOPPED

        self.repeat = self.RepeatMode.OFF

        self.shuffle = False

        self.volume = 1.0

    

class Music_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is ready!")

async def setup(bot: commands.Bot):
    await bot.add_cog(Music_Cog(bot=bot))