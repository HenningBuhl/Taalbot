import pytest
import discord.ext.test as dpytest
from guildconfig import GREETING_CHANNEL

from time import sleep

@pytest.mark.asyncio
async def test_greeting(bot):
    member = await dpytest.member_join()
    assert dpytest.verify().message().contains().content("Welcome ")
