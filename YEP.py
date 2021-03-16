import discord
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix="!")

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):

        if str(message.author) == "Willhoe#6666":
            await message.channel.send("Fuck you, " + str(message.author) + "!")
        else:
            await message.channel.send("Hello, I am a bot.")

@client.command()
async def play(ctx, url : str):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if not voice.is_connected():
        await voiceChannel.connect()
    
@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("I am not connected to a voice channel.")

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("I am not playing any music currently.")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("I am not paused.")

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

client.run('ODIxMjkyMjk1ODIzMTYzNDEy.YFBmDg.TFd7sjd3hfsZOrkD_VUI3xy_io4')
