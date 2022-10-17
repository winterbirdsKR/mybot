import discord
import sys

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
        if message.content == '!입장 1113':
            await message.author.add_roles(role)
        elif message.content == '!퇴장 1113':
            await message.author.remove_roles(role)
        
        await message.delete()
            

client.run('MTAzMDI3NTkwMTQxNTUxMDA5Ng.GzOza8.LF3hV8G8FQsjbpZRm8N3qQJZqswGft9s5gj-qY')