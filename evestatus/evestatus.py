import discord
import requests
from discord.ext import commands
from datetime import datetime

class evestatus:
    eve_url = "https://esi.evetech.net"

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def evestats(self):
        """Returns the Current time, players online in EVE Online"""

        utc_time = datetime.utcnow().strftime('%I:%M:%S %p')
        current_status = requests.get(self.eve_url + '/v1/status/')
        rsp = current_status.json()
        await self.bot.say("Current Time: " + utc_time + "\n Player Count: " + str(rsp['players']))

def setup(bot):
   	bot.add_cog(evestatus(bot))
