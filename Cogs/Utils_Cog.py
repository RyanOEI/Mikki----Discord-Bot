import discord
from discord.ext import commands
from discord import app_commands

class Utils_Cog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is ready!")
    
    @app_commands.command(name="ping", description="How fast Mikki's reaction time.")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Pong! (Hit back in {int(self.bot.latency * 1000)} ms)")

async def setup(bot: commands.Bot):
    await bot.add_cog(Utils_Cog(bot=bot))