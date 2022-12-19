import discord


from cogs.greeting import Greeting


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

        # Pass arguments to super constructor.
        super().__init__(command_prefix='??', intents=intents, activity=activity, status=status)

    async def on_ready(self):
        print('Taalbot is preparing...')
        
        # Add cogs to the bot.
        await self.add_cog(Greeting(self))

        print("Taalbot is now ready.")
