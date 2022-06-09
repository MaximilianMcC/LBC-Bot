# Imports
import requests, json
import interactions


# Get stuff from config.json
def config():
    # Open the file and get the json
    file = open("config.json")
    data = json.load(file)
    file.close()

    # Give back the json
    return data


# Make the client
print("Loading...")
client = interactions.Client(token=config()["token"])
guild_ids = config()["guilds"]


# When the bot is ready
@client.event
async def on_ready():
    print("Bot is ready");


# Testing command
@client.command(name="test", description="Testing command for bot development", scope=guild_ids)
async def testCommand(ctx: interactions.CommandContext):
    await ctx.send("Among us😂😂😂")


# Notices command
@client.command(name="notices", description="Get the LBC daily notices", scope=guild_ids)
async def noticeCommand(ctx: interactions.CommandContext):
    await ctx.send("Daily Notices")


# Start the bot
client.start()