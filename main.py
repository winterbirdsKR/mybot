import discord
import sys
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == '!종료':
        await sys.exit('Program stopped by !stop')

    if message.content == '!음지세팅':
        if message.channel.id == 1031373432501305397:
            await message.channel.send('!입장 [비밀번호], !퇴장 [비밀번호]')
            await message.delete()
    
    if message.channel.id == 1031373432501305397:
        server = client.get_guild(1029765705203204201)
        role = server.get_role(1031372933895032992)
        if message.content == '!입장 11131112':
            await message.author.add_roles(role)
        elif message.content == '!퇴장 11131112':
            await message.author.remove_roles(role)
        
        await message.delete()
            
token = os.environ["BOT_TOKEN"]

client.run(token)
