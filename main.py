# Imports
import json, requests
import interactions


# Get stuff from config.json
def config():
    # Open the file and get the json
    file = open("config.json")
    data = json.load(file)
    file.close()
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
    
    await ctx.send("It's Morbin' time")

    url = config()["lbcapi"]
    noticesString = requests.get(url).text
    noticesJson = json.loads(noticesString)

    await ctx.send(str(noticesJson))


# Morbin' time command
@client.command(name="morb", description="It's Morbin' time", scope=guild_ids)
async def morbCommand(ctx: interactions.CommandContext):
    await ctx.send("It's Morbin' time")
    #TODO: Send a random Morbius gif


# Start the bot
client.start()