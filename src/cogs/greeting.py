import os


from discord.ext import commands
from discord.utils import get
from guildconfig import GREETING_CHANNEL

class Greeting(commands.Cog):
    def __init__(self, bot, channel):
        self.bot = bot
        self.channel = get(GREETING_CHANNEL)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.channel.send(f'Welcome {member.mention}.')
