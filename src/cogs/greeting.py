from discord.ext import commands
from discord.utils import get, find
from guildconfig import GREETING_CHANNEL


class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = get(member.guild.channels, name=GREETING_CHANNEL)
        print(channel)
        print(member)
        await channel.send(f"Hallo {member.mention}, welkom op Nederlands Leren! I'll send you a DM to help you get the right roles.")
        print('SUCCESS')
