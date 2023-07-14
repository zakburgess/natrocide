import discord

TOKEN = open("token.txt","r").readline()

intents = discord.Intents.all()
client = discord.Client(intents = intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    role = discord.utils.find(lambda r: r.name == 'Newcomer (Lvl1+)', message.guild.roles)    
    if role in message.author.roles and "natro" in message.content.lower():
        await message.delete()
        await message.author.send("You are in the wrong discord. Please join the official Natro discord at https://discord.com/invite/natromacro")
        print(f"{message.author}: {message.content}")

if __name__ == "__main__" :
    client.run(TOKEN)
