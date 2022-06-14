# Imports
import json, requests, random
from turtle import color
from unicodedata import name
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
    
    # This message needs to be here to give the request more time otherwise the command will just fail
    #TODO: Figure out how to not need this
    await ctx.send("Notices loading...", ephemeral=True)

    # Get the notices
    #TODO: Try and make the request faster. Might just be my garbar internet
    url = config()["lbcapi"]
    noticesString = requests.get(url).text
    noticesJson = json.loads(noticesString)

    # Make an embed
    embed = interactions.Embed(title="Long Bay College Daily Notices", color=0x00597C)

    # Loop through all the notices
    for notice in noticesJson["notices"]:
        # Check for if the subtitle is nothing
        #TODO: Change the API to just return `""`
        if (notice["subtitle"] == "None"):
             notice["subtitle"] = ""

        # Add a new field with all of the info
        embed.add_field(name=f"{notice['title']}\n{notice['subtitle']}", value=notice["content"], inline=False)

    await ctx.send(embeds=embed)

# Morbin' time command
@client.command(name="morb", description="It's Morbin' time", scope=guild_ids)
async def morbCommand(ctx: interactions.CommandContext):
    # Send a random morb gif (its morbin' time)
    morb_gifs = ["https://tenor.com/view/morbius-ping-morbius-morbiussweep-ping-jared-leto-gif-25020117", "https://media.discordapp.net/attachments/908796016235524116/985621010130813028/meme.gif", "https://media.discordapp.net/attachments/908796016235524116/985620772859047996/uncaption.gif", "https://tenor.com/view/sentenced-no-sentence-morbius-sweep-morbius-gif-25702782", "https://tenor.com/view/morbius-morb-nation-morbius-sweep-its-morbin-time-gif-25781394"]
    await ctx.send(random.choice(morb_gifs))

# Start the bot
client.start()