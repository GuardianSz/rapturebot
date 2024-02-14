import discord
import schedule
import asyncio

TOKEN = process.env.token
ROLE_ID = 123456789012345678
CHANNEL_ID = 123456789012345678

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready.')

async def ping_role():
    guild = client.get_guild(123456789012345678)
    role = guild.get_role(ROLE_ID)
    channel = guild.get_channel(CHANNEL_ID)
    await channel.send(f'Vote for Craftersmc, {role.mention}!')

schedule.every().day.at("10:00").do(asyncio.run, ping_role)

client.run(TOKEN)
