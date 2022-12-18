import sys
sys.path.insert(0, 'src')


from taalbot import Taalbot
import pytest


@pytest.mark.asyncio
async def test_pls(bot):
    s = Taalbot()
    pass
