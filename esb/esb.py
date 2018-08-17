import discord
import requests
from discord.ext import commands

class esb:
    esb_url = "https://eveskillboard.com/pilot/"

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def esb(self, ctx):
        """Eveskillboard related commands"""
        
    @esb.command()
    async def pilot(self, *, pilot_name: str):
        """Look up a pilots skillboard"""

        pilot_found = requests.get(self.esb_url + pilot_name)
        if pilot_found.status_code == 200:
            await self.bot.say("Pilot Found! \n" + esb_url + pilot_name)
        else:
            await self.bot.say("Pilot wasn't found on Eveskillboard")
    
def setup(bot):
   	bot.add_cog(esb(bot))
