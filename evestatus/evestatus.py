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
        """Returns the Current time, players online, start_time, vip status in EVE Online"""

        utc_time = datetime.utc_time().strftime('%I:%M:%S %p')
        try:
        	current_status = requests.get(eve_url + '/v1/status/')
        	current_status.json()
        await self.bot.say("Current Time: " + utc_time + "\n")

def setup(bot):
   	bot.add_cog(evestatus(bot))
