from discord.ext import commands
from discord.utils import get, find
from guildconfig import *


class Onboarding(commands.Cog):
    '''
    TODO
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Step 0: Remove all onboarding-process-related roles from the user.
        # TODO
      
        # Step 1: DM the new user with an introduction.        
        text = ('Hello, and welcome to **Nederlands Leren**! Let me introduce myself: I am taalbot, a bot that does things. I primarily live on this server.'
            'I would like to walk you through our introduction process, so that you can experience the server to its fullest in no time!\n'
            'For now, you only have access to a few channels, but there are many more!'
            'In order for you to get the most out of your journey on this server, we first need to assign yourself some roles.'
            'They will automatically give you access to currently hidden channels, and also let fellow members know about your Dutch proficiency level, so that they can adapt themselves!\n'
            'Shall we get started? React to this message with ▶️, like I just did! This will be our main interaction method during the process.')
        choices = {'▶️': None}
        self.prompt(member, text, choices)
        
        # Step 2: Ask the user if they are a native speaker or not.
        text = ('Right, first things first, let\'s talk about your proficiency.'
                'Are you a **native Dutch speaker**?')
        choices = {
            '👍': Action(role=ROLE_NAME_NATIVE, message=f'Nice, I\'ve assigned you the **{ROLE_NAME_NATIVE}** role!'),
            '👎': None
        }
        reaction = self.prompt(member, text, choices)
        
        # Step 3.1: If the user is a native speaker, ask which version of dutch they speak.
        if reaction == '👍':
            text = ('OK! Which Dutch do you speak?\n'
                    '🇳🇱 The Netherlands'
                    '🇧🇪 Belgium (Flanders)'
                    '🇸🇷 Suriname, Sint-Maarten, Sint-Eustatius, Saba + ABC Islands')
            choices = {
              '🇳🇱': Action(role=ROLE_NAME_NL, message=f'Okay. I\'ve assigned you the **{ROLE_NAME_NL}** role.'),
              '🇧🇪': Action(role=ROLE_NAME_BE, message=f'Okay. I\'ve assigned you the **{ROLE_NAME_BE}** role.'),
              '🇸🇷': Action(role=ROLE_NAME_SA, message=f'Okay. I\'ve assigned you the **{ROLE_NAME_SA}** role.'),
            }
            self.prompt(member, text, choices)
            
        # Step 3.2: If the user is not a native speaker, ask which level of dutch they speak.
        else:  # reaction == '👎'
            text = ('OK! What is your current Dutch level?'
                    'Are you unsure, or need more info? Check https://en.wikipedia.org/wiki/Common_European_Framework_of_Reference_for_Languages#Common_reference_levels.\n'
                    '🇴: **Onbekend** (unknown), total beginner'
                    '🇦: **Basic user**, corresponds to CEFR A1 (breakthrough) and A2 (waystage)'
                    '🇧: **Independent user**, corresponds to CEFR B1 (threshold) and B2 (vantage)'
                    '🇨: **Proficient user**, corresponds to CEFR C1 (advanced) and C2 (mastery)')
            choices = {
              '🇴': Action(role=ROLE_NAME_LEVEL_O, message=f'Okay. I\'ve assigned you the **{ROLE_NAME_LEVEL_O}** role.'),
              '🇦': Action(role=ROLE_NAME_LEVEL_A, message=f'Okay. I\'ve assigned you the **{ROLE_NAME_LEVEL_A}** role.'),
              '🇧': Action(role=ROLE_NAME_LEVEL_B, message=f'Okay. I\'ve assigned you the **{ROLE_NAME_LEVEL_B}** role.'),
              '🇨': Action(role=ROLE_NAME_LEVEL_C, message=f'Okay. I\'ve assigned you the **{ROLE_NAME_LEVEL_C}** role.'),
            }
            self.prompt(member, text, choices)

        # Step 4: Ask the user wihich country they are from.
        text = ('We\'re making progress! Now, if you want, you can tell me the name of the **country you live in**.\n'
                'I said earlier that we\'d communicate via reactions, but there are far too many different options!'
                'For this time only, I am asking you to *type* the country name (in Dutch!)'
                'React with ⏩ to skip this step.\n'
                'Example: **Nederland**\n'
                'If you don\'t know what yours is, here is a list of country names in Dutch:'
                'https://www.101languages.net/dutch/country-names-dutch/')
        choices = {
            '⏩': Action(message=f'Okay then, keep your secrets 👀.'),
        }
        # TODO add all countries with loop?
        # message=f'🌍 Great! I added the **{country}** role to your profile!'
        self.prompt(member, text, choices)
        
        # Step 5: Ask the user if they want additional roles.
        text = ('Awesome, you\'re *almost* set! 🥳'
                'There are still a few optional roles you can decide to add to your profile.'
                '*Note*: these roles can also be obtained later, should you ever change your mind.\n'
                f'🇧🇪 **BN**: if you are interested in Belgian Dutch! Gives access to the <#{BELGIE_CHANNEL_ID}> channel.'
                f'📗 **Woord**: get a notification when a new *woord van de dag* (word of the day) is posted in <#{WVDD_CHANNEL_ID}>.'
                '🏫 **Sessies**: get a notification when members of this server organize impromptu / planned (voice) Dutch sessions.'
                '💪 **Verbeter mij**: this tag lets natives (or everyone) know that you\'d like your mistakes to be corrected.'
                '✅ When you\'re satisfied with your choices.')
        choices = {
            '🇧🇪': Action(role=ROLE_NAME_BN, message=f'👍 Gave you the **{ROLE_NAME_BN}** role!'),
            '📗': Action(role=ROLE_NAME_WVDD, message=f'👍 Gave you the **{ROLE_NAME_WVDD}** role!'),
            '🏫': Action(role=ROLE_NAME_SESSIONS, message=f'👍 Gave you the **{ROLE_NAME_SESSIONS}** role!'),
            '💪': Action(role=ROLE_NAME_CORRECT_ME, message=f'👍 Gave you the **{ROLE_NAME_CORRECT_ME}** role!'),
            '✅': Action(message='Great! You\'re done 🎉. Enjoy the server.'),
        }
        self.prompt(member, text, choices, allow_multiple=True, terminate_choice='✅')
        
        # Step 6: Send the user a friendly goodbye message.
        text = ('Phew, finally done!'
                f'Take a look at <#{ALGEMEEN_GENERAL_CHANNEL_ID}>, as I believe people there just gave you, or will give you, a warm welcome! (Let me know if they don\'t, though!)'
                f'Make sure to read the rules in <#{INFORMATIE_CHANNEL_ID}>, too!'
                'Veel plezier!')
        member.send(text)

    async def prompt(self, member, text, choices, allow_multiple=False, terminate_choice=None):
        '''
        Prompt the member with a given text and give the keys of the choices dictionary as possible reactions.
        Reacting with an emoji causes an action (if one is given) or skips the prompt (if none is given).
        Multiple choices can be made by the member if a terminating choice, that will end the prompt, is provided.
        '''
        
        if allow_multiple and terminate_choice is None:
            raise ValueError('There must exist a terminating choice when allowing multiple choices.')
        
        # Send prompt to user.
        message = await member.send(text)
        
        # Add reactions to message.
        emojis = choices.keys()
        [await message.add_reaction(e) for e in emojis]
        
        # Wait for user to react.
        while True:
            reaction, user = await self.bot.wait_for(
                'reaction_add', timeout=600,
                check=lambda: user == member and reaction.message.id == message.id and str(reaction.emoji) in emojis)
            
            # Perform the action assosiated with the choice (if the action is not None).
            action = choices[reaction]
            if action is not None:
                self.perform(action, member)
            
            # Stop listening to more reactions if the last reaction was the terminating choice.
            if reaction == terminate_choice:
                break
            
            # Stop listening to more reactions if only one reaction is allowed.
            if not allow_multiple:
                break
        
        # Return the last reaction from the user.
        return reaction

    async def perform(action, member):
        '''Performs all steps in an action if they are not None.'''
        if action.role is not None:
            # Assign role to user.
            role = get(member.guild.roles, name=action.role)
            member.add_roles(role)

        if action.message is not None:
            # Send feedback message to user.
            member.send(action.message)
            pass


class Action():
    '''
    A Class representing an action that happens after a user clicks a reaction to continue in the onboarding process.
    If the role parameter is not None, the role to be assigned assigned to the user when the reaction is clicked.
    If the message parameter is not None, the feedback for clicking the reaction.
    '''
    def __init__(self, role=None, message=None):
        self.role = role
        self.message = message
