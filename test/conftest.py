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


@pytest_asyncio.fixture
async def bot():
    bot = Taalbot()
    await bot._async_setup_hook()
    dpytest.configure(bot, 1, 1, 1)
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
