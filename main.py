import discord
import asyncio
import os
from keep_alive import keep_alive

TOKEN = os.environ['TOKEN']
GUILD_ID = 998991500450996335  # <- Replace with YOUR server ID
VC_CHANNEL_ID = 1390092074262728785  # <- Replace with YOUR voice channel ID
AUDIO_FILE = "audio.mp3"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user.name}")

    guild = client.get_guild(GUILD_ID)
    channel = guild.get_channel(VC_CHANNEL_ID)
    if not channel:
        print("❌ Voice channel not found.") 
        return

    try:
        vc = await channel.connect()
        print(f"🔊 Connected and playing in {channel.name}")
    except discord.ClientException:
        vc = discord.utils.get(client.voice_clients, guild=guild)
        print("⚠ Reusing existing VC connection")

    # Start playback immediately to avoid 4006 disconnects
    if not vc.is_playing():
        vc.play(discord.FFmpegPCMAudio(source=AUDIO_FILE))

    # Loop forever
    while True:
        if not vc.is_playing():
            print("🔁 Restarting loop...")
            vc.play(discord.FFmpegPCMAudio(source=AUDIO_FILE))
        await asyncio.sleep(1)

keep_alive()
client.run(TOKEN)
