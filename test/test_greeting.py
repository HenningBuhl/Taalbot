import pytest
import discord.ext.test as dpytest
from guildconfig import GREETING_CHANNEL

from time import sleep

@pytest.mark.asyncio
async def test_greeting(bot):
    #await dpytest.backend.FakeHttp().create_channel(0, 'text')
  
  

    await dpytest.member_join()
    print('LOOOOOOOOOL')
    #sleep(1)
    
    assert dpytest.verify().message().contains().content("Welcome ")

    #c = await dpytest.back.FakeHttp().get_channel(0)
    #print(c)
