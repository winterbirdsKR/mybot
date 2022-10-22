import discord
import os
import sys

intents = discord.Intents.default()
intents.members = True
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
            await message.channel.send('사용방법 : 봇과의 DM채널에 아래 명령어 입력')
            await message.channel.send('!입장 [비밀번호]')
            await message.channel.send('!퇴장 [비밀번호]')
            await message.delete()
    
    if str(message.channel.type) == 'private':
        password = os.environ["PASSWORD"]
        server = client.get_guild(1029765705203204201)
        role = server.get_role(1031372933895032992)
        user = server.get_member(message.author.id)
        if message.content == '!입장 ' + password:
            await user.add_roles(role)
        elif message.content == '!퇴장 '+ password:
            await user.remove_roles(role)

            

            
token = os.environ["BOT_TOKEN"]

client.run(token)
