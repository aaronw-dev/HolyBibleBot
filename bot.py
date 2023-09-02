import discord #stuff for discord bot
from discord import app_commands #allows discord commands
from time import sleep
intents = discord.Intents().all() #we need all discord intents
client = discord.Client(intents=intents) #init a client with given intents
tree = app_commands.CommandTree(client) #for discord commands

with open("holybible.txt", "r") as file:
    holybible = file.read()

holybiblelines = holybible.split("\n")
holybiblelines = holybiblelines[2:]
@tree.command(name="holybible", description="Amen.")
async def ctfinfo(interaction):
    await interaction.response.send_message("done", ephemeral=True)
    for line in holybiblelines:
        print(line.split("\t")[0])
        await interaction.channel.send("# **" + line.upper().split("\t")[1] + "**")
        sleep(0.1)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    print(message.author.display_name + ": " + message.content)
    #await message.channel.send("balls")

@client.event
async def on_ready():
  await tree.sync()
  print("yes mom i'm awake")

with open("token.token", "r") as file:
    token = file.read()
client.run(token)