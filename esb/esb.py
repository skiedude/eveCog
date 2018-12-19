import discord
import requests
from discord.ext import commands

from __main__ import send_cmd_help


class esb:
    esb_url = "https://eveskillboard.com"

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def esb(self, ctx):
        """Eveskillboard related commands"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    #@esb.command()
    #async def pilot(self, *, pilot_name: str):
    #    """Look up a pilots skillboard"""

    #    pilot_found = requests.get(self.esb_url + '/pilot/' + pilot_name, allow_redirects=False)
    #    location = pilot_found.headers.get('Location')

    #    if (location is not None and '/password/' in location):
    #        await self.bot.say("Pilot Found! But looks like it has a password\n" + self.esb_url + '/pilot/' + pilot_name.replace(" ", "_"))
    #    elif (location is not None and location == self.esb_url): 
    #        await self.bot.say("Pilot wasn't found on EveSkillboard")
    #    elif (location is None and pilot_found.status_code == 200):
    #        await self.bot.say("Pilot Found!\n" + self.esb_url + '/pilot/' + pilot_name.replace(" ", "_"))
    #    else:
    #        await self.bot.say("Not sure what happened, but it wasn't good")

    @esb.command()
    async def transfer(self):
        """Provide information on how to transfer a character"""
        await self.bot.say("**How do transfers work?**\nhttps://eveskillboard.com/guides/transfer")
                
def setup(bot):
   	bot.add_cog(esb(bot))
