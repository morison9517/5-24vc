import discord
from discord.ext import commands, tasks
from datetime import datetime
from decouple import config
import os

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

DISCORD_GUILD_ID = int(config('DISCORD_GUILD_ID'))
DISCORD_VC_CHANNEL_ID = int(config('DISCORD_VC_CHANNEL_ID'))

@tasks.loop(minutes=5)
async def update_vc_name():
    now = datetime.now()
    current_hour = now.hour

    guild = bot.get_guild(DISCORD_GUILD_ID)
    vc = guild.get_channel(DISCORD_VC_CHANNEL_ID)

    if 5 <= current_hour < 10:
        new_name = "朝活"
    elif 10 <= current_hour < 18:
        new_name = "昼活"
    elif 18 <= current_hour < 22:
        new_name = "夜活"
    else:
        return

    await vc.edit(name=new_name)
    print(f"VC name changed to {new_name}")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    update_vc_name.start()

bot.run(config('DISCORD_BOT_TOKEN'))
