import sys
sys.path.insert(0, 'src')


import glob
import os
import pytest_asyncio
import discord
import discord.ext.commands as commands
import discord.ext.test as dpytest
from discord.ext.commands import Cog, command
from taalbot import Taalbot
from cogs.greeting import Greeting
from guildconfig import GREETING_CHANNEL, LOGGING_CHANNEL


@pytest_asyncio.fixture
async def bot():
    # Setup the bot for testing.
    bot = Taalbot()
    await bot._async_setup_hook()
    await bot.add_cogs()
    
    # Add clien (bot) to the config and retrieve it for further steps.
    dpytest.configure(bot, 0, 0, 0)
    config = dpytest.get_config()
    
    # Create the guild.
    guild = dpytest.back.make_guild(name='Nederlands Leren', id_num=874659874358)
    
    # Create the channels.
    greeting_channel = dpytest.back.make_text_channel(GREETING_CHANNEL, guild)
    log_channel = dpytest.back.make_text_channel(LOGGING_CHANNEL, guild)
    channels = [greeting_channel, log_channel]
    
    # Create members.
    # TODO
    
    # Create roles.
    # TODO
    
    # Assign the test setup to the config.
    config.guilds.append(guild)
    config.channels.extend(channels)
    
    return bot


@pytest_asyncio.fixture(autouse=True)
async def cleanup():
    yield
    await dpytest.empty_queue()


def pytest_sessionfinish(session, exitstatus):
    print("\n-------------------------\nClean dpytest_*.dat files")
    fileList = glob.glob('./dpytest_*.dat')
    for filePath in fileList:
        try:
            os.remove(filePath)
        except Exception:
            print("Error while deleting file: ", filePath)
