import os
import discord


class Taalbot(discord.Client):
    def __init__(self):
        # Intents of bot.
        intents = discord.Intents.default()
        intents.messages = True
        intents.guilds = True
        intents.members = True

        # Activity and status of bot.
        activity = discord.Game(name="TODO")
        status = discord.Status.online

        super().__init__(intents=intents, activity=activity, status=status)

    async def on_ready(self):
        # Add cogs (order matters for checking order and help command).
        # TODO
        #await self.add_cog(Misc())

        print("Taalbot is now ready.")
