import discord
from discord.ext import commands
import os
import json

keys = json.load(open("./keys.json", "r"))

client = commands.Bot(command_prefix=keys["prefix"])
client.remove_command("help")


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"loaded {filename}")

client.run(keys["clientToken"])
