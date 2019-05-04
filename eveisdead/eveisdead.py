import discord
import random
from discord.ext import commands
from datetime import datetime

class eveisdead:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def isevedead(self):
        """Answers the age old question about eve dying"""
        answers = ['Depends, did you take the blue pill or the red pill', 'Was it ever alive?', 'Reddit says it is, and the internet would never lie to me', 'We\'re all just norn alts in the end', 'As long as I can buy skins, this game is alive', 'Blink twice if you\'re being held hostage', 'EVE has been dying since 2003 silly goose']
        await self.bot.say(random.choice(answers))

def setup(bot):
   	bot.add_cog(eveisdead(bot))
