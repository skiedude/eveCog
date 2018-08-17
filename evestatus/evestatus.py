import discord
import requests
from discord.ext import commands
from datetime import datetime

class evestatus:
    eve_url = "https://esi.evetech.net"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def evestatus(self):
        """Returns the Current time in EVE Online"""

        utc_time = datetime.utc_time()
        try:
        	current_status = requests.get(eve_url + '/v1/status/')
        	current_status.json()
        await self.bot.say(utc_time)

def setup(bot):
   	bot.add_cog(evestatus(bot))
