import discord
from discord.ext import commands
from prsaw import RandomStuff

bot = commands.Bot(command_prefix='#')
api_key = 'the api key'
rs = RandomStuff(async_mode = True,api_key=api_key)

@bot.event
async def on_message(message):
    if bot.user == message.author:
        return
    if message.channel.id == ['channel id']:
        response = await rs.get_ai_response(message.content)
        # await message.me(response)
        response = response[0]
        response = response.get('message')
        channel = bot.get_channel(['channel id'])
        response =  f"{message.author.mention} {response}"
        await channel.send(response)


    await bot.process_commands(message)
