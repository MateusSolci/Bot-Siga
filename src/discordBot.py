import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

class Comandos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def alo(self, ctx):
        await ctx.send("OI !")

    @commands.command()
    async def tomate(self, ctx):
        await ctx.send('Ô primo')

def setup(client):
    client.add_cog(Comandos(client))