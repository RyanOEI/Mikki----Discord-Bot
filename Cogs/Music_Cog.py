import discord
from discord.ext import commands
from discord import app_commands

from dataclasses import dataclass

from urllib.parse import urlparse
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
    
    async def search_song(self, query: str) -> list[Song]:
        def is_url(text: str) -> bool:
            parsed = urlparse(text)
            return parsed.scheme in ("http", "https") and bool(parsed.netloc)
        
        if not is_url(query):
            query = f"ytsearch:{query}"
        
        ydl_opts = {
            "format": "bestaudio/best",
            "noplaylist": True,
            "quiet": True,
            "extract_flat": False,
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)

            if "entries" in info:
                return [Song(
                    title=entry.get("title"),
                    url=entry.get("webpage_url"),
                    channel_name=entry.get("uploader"),
                    channel_url=entry.get("uploader_url"),
                    duration=entry.get("duration"),
                    thumbnail_url=entry.get("thumbnail")
                ) for entry in info["entries"]]
            else:
                return [Song(
                    title=info.get("title"),
                    url=info.get("webpage_url"),
                    channel_name=info.get("uploader"),
                    channel_url=info.get("uploader_url"),
                    duration=info.get("duration"),
                    thumbnail_url=info.get("thumbnail")
                )]

    @app_commands.command(name="play", description="Play a song from YouTube.")
    async def play(self, interaction: discord.Interaction, query: str):
        pass
        # songs = await self.search_song(query)

        # for song in songs:
        #     print(f"Found song: {song.title} ({song.url}) by {song.channel_name} ({song.channel_url}) [{song.duration} seconds]")


async def setup(bot: commands.Bot):
    await bot.add_cog(Music_Cog(bot=bot))