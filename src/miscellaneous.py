import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
from py_expression_eval import Parser
import urllib.parse, urllib.request, re
from bs4 import BeautifulSoup
from googlesearch import search 

bot = commands.Bot(command_prefix='#')
parser = Parser()

# Calculates an expression

@bot.command()
async def calculate(ctx,equation):
  try:
    equation_solved = round(parser.parse(equation).evaluate({}),2)
    await ctx.send("**Answer** = {}".format(equation_solved))
  except ZeroDivisionError:
    await ctx.send("Cant divide by zero.")

# Does a google search

@bot.command()
async def google(ctx,*,gsearch):
    search_keyword=gsearch
    l = []
    for url in search(search_keyword,3):
            l.append(url)
    l.pop(-1)
    links  = '\n\n'.join(map(str, l))

    search_embed = discord.Embed(title=f"Search results for {search_keyword}",description=links)
    await ctx.send(embed=search_embed)
    
# Sends a video from youtube according to search

@bot.command()
async def ytsearch(ctx,*,search):


    search_keyword=search
    search_keyword=list(search_keyword)
    for n,i in enumerate(search_keyword):
        if i==' ':
            search_keyword[n]='+'

    search_keyword = ''.join(map(str, search_keyword))
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    await ctx.send("https://www.youtube.com/watch?v=" + video_ids[0])
    
# Makes a poll (max 6 choices)

@bot.command()
async def poll(ctx,*,title_and_options):
    title_and_options = list(title_and_options)
    l1 = []
    if title_and_options.count(',') == 2:
        indices = [i for i, x in enumerate(title_and_options) if x == ","]
        comma_1 = indices[0]
        comma_2 = indices[1]
        title = ''.join(title_and_options[0:comma_1])
        option_1 = ''.join(title_and_options[comma_1:comma_2])
        option_2 = ''.join(title_and_options[comma_2::])
        # title.replace(',','')
        option_1=list(option_1)
        option_1.remove(',')
        option_1=''.join(map(str, option_1))

        option_2=list(option_2)
        option_2.remove(',')
        option_2=''.join(map(str, option_2))
        # print(option_2)
        embed_poll = discord.Embed(title=title,description=f'🔴 {option_1} \n\n 🟠 {option_2}',color=discord.Color.blue())
      
        message = await ctx.send(embed=embed_poll)
        await message.add_reaction('🔴')
        await message.add_reaction('🟠')

    elif title_and_options.count(',') == 3:
        indices = [i for i, x in enumerate(title_and_options) if x == ","]
        comma_1 = indices[0]
        comma_2 = indices[1]
        comma_3 = indices[2]
        title = ''.join(title_and_options[0:comma_1])
        option_1 = ''.join(title_and_options[comma_1:comma_2])
        option_2 = ''.join(title_and_options[comma_2:comma_3])
        option_3 = ''.join(title_and_options[comma_3::])
        # title.replace(',','')
        option_1=list(option_1)
        option_1.remove(',')
        option_1=''.join(map(str, option_1))

        option_2=list(option_2)
        option_2.remove(',')
        option_2=''.join(map(str, option_2))

        option_3=list(option_3)
        option_3.remove(',')
        option_3=''.join(map(str, option_3))
    
        embed_poll = discord.Embed(title=title,description=f'🔴 {option_1} \n\n 🟠 {option_2} \n\n 🟡 {option_3}',color=discord.Color.blue())
     
        message = await ctx.send(embed=embed_poll)
        await message.add_reaction('🔴')
        await message.add_reaction('🟠')
        await message.add_reaction('🟡')

    elif title_and_options.count(',') == 4:
        indices = [i for i, x in enumerate(title_and_options) if x == ","]
        comma_1 = indices[0]
        comma_2 = indices[1]
        comma_3 = indices[2]
        comma_4 = indices[3]
        title = ''.join(title_and_options[0:comma_1])
        option_1 = ''.join(title_and_options[comma_1:comma_2])
        option_2 = ''.join(title_and_options[comma_2:comma_3])
        option_3 = ''.join(title_and_options[comma_3:comma_4])
        option_4 = ''.join(title_and_options[comma_4::])
        # title.replace(',','')
        option_1=list(option_1)
        option_1.remove(',')
        option_1=''.join(map(str, option_1))

        option_2=list(option_2)
        option_2.remove(',')
        option_2=''.join(map(str, option_2))

        option_3=list(option_3)
        option_3.remove(',')
        option_3=''.join(map(str, option_3))

        option_4=list(option_4)
        option_4.remove(',')
        option_4=''.join(map(str, option_4))
    
        embed_poll = discord.Embed(title=title,description=f'🔴 {option_1} \n\n 🟠 {option_2} \n\n 🟡 {option_3} \n\n 🟢 {option_4}',color=discord.Color.blue())
     
        message = await ctx.send(embed=embed_poll)
        await message.add_reaction('🔴')
        await message.add_reaction('🟠')
        await message.add_reaction('🟡')
        await message.add_reaction('🟢')

    elif title_and_options.count(',') == 5:
        indices = [i for i, x in enumerate(title_and_options) if x == ","]
        comma_1 = indices[0]
        comma_2 = indices[1]
        comma_3 = indices[2]
        comma_4 = indices[3]
        comma_5 = indices[4]
        title = ''.join(title_and_options[0:comma_1])
        option_1 = ''.join(title_and_options[comma_1:comma_2])
        option_2 = ''.join(title_and_options[comma_2:comma_3])
        option_3 = ''.join(title_and_options[comma_3:comma_4])
        option_4 = ''.join(title_and_options[comma_4:comma_5])
        option_5 = ''.join(title_and_options[comma_5::])
        
        # title.replace(',','')
        option_1=list(option_1)
        option_1.remove(',')
        option_1=''.join(map(str, option_1))

        option_2=list(option_2)
        option_2.remove(',')
        option_2=''.join(map(str, option_2))

        option_3=list(option_3)
        option_3.remove(',')
        option_3=''.join(map(str, option_3))

        option_4=list(option_4)
        option_4.remove(',')
        option_4=''.join(map(str, option_4))

        option_5=list(option_5)
        option_5.remove(',')
        option_5=''.join(map(str, option_5))
    
        embed_poll = discord.Embed(title=title,description=f'🔴 {option_1} \n\n 🟠 {option_2} \n\n 🟡 {option_3} \n\n 🟢 {option_4} \n\n 🔵 {option_5}',color=discord.Color.blue())
     
        message = await ctx.send(embed=embed_poll)
        await message.add_reaction('🔴')
        await message.add_reaction('🟠')
        await message.add_reaction('🟡')
        await message.add_reaction('🟢')
        await message.add_reaction('🔵')
    elif title_and_options.count(',') == 6:
        indices = [i for i, x in enumerate(title_and_options) if x == ","]
        comma_1 = indices[0]
        comma_2 = indices[1]
        comma_3 = indices[2]
        comma_4 = indices[3]
        comma_5 = indices[4]
        comma_6 = indices[5]
        title = ''.join(title_and_options[0:comma_1])
        option_1 = ''.join(title_and_options[comma_1:comma_2])
        option_2 = ''.join(title_and_options[comma_2:comma_3])
        option_3 = ''.join(title_and_options[comma_3:comma_4])
        option_4 = ''.join(title_and_options[comma_4:comma_5])
        option_5 = ''.join(title_and_options[comma_5:comma_6])
        option_6 = ''.join(title_and_options[comma_6::])
        
        # title.replace(',','')
        option_1=list(option_1)
        option_1.remove(',')
        option_1=''.join(map(str, option_1))

        option_2=list(option_2)
        option_2.remove(',')
        option_2=''.join(map(str, option_2))

        option_3=list(option_3)
        option_3.remove(',')
        option_3=''.join(map(str, option_3))

        option_4=list(option_4)
        option_4.remove(',')
        option_4=''.join(map(str, option_4))

        option_5=list(option_5)
        option_5.remove(',')
        option_5=''.join(map(str, option_5))
        
        option_6=list(option_6)
        option_6.remove(',')
        option_6=''.join(map(str, option_6))
    
        embed_poll = discord.Embed(title=title,description=f'🔴 {option_1} \n\n 🟠 {option_2} \n\n 🟡 {option_3} \n\n 🟢 {option_4} \n\n 🔵 {option_5} \n\n 🟣 {option_6}',color=discord.Color.blue())
     
        message = await ctx.send(embed=embed_poll)
        await message.add_reaction('🔴')
        await message.add_reaction('🟠')
        await message.add_reaction('🟡')
        await message.add_reaction('🟢')
        await message.add_reaction('🔵')
        await message.add_reaction('🟣') 

    
    else:
        await ctx.send(f"{ctx.author.mention}, You can't add more than six options.")

# Makes a giveaway

@bot.command()
async def giveaway(ctx,time,*,prize):
    sec = time[:-1]
    unit = time[-1]
    sec = int(sec)
    if unit=='m':
        sec = sec*60
    elif unit=='h':
        sec = sec*3600
    elif unit=='d':
        sec = sec*86400
    elif unit=='s':
        sec = sec
    else:
        await ctx.send("Mention an appropriate time eg. s, m, h, d")
    endtime = datetime.utcnow() + timedelta(seconds=sec)
    date = str(endtime.date())[-2:]
    month = endtime.strftime("%B")
    hr = endtime.strftime("%H")
    mins = endtime.strftime("%M")


    giveaway_embed = discord.Embed(title="Giveaway Started",description=f"Prize: {prize} \n Ends At: {date}th {month} {hr}:{mins} UTC \n \n React with 🎉 to join the giveaway ")
    message = await ctx.send(embed=giveaway_embed)
    await message.add_reaction('🎉')
    await asyncio.sleep(sec)

    msg = await ctx.channel.fetch_message(message.id)
    users = await  msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))
    winner = random.choice(users)
    await ctx.send(f"POG! {winner.mention} won {prize}")
    
# Makes an embed

@bot.command()
async def embed(ctx,title,*,description=None):
    embed = discord.Embed(title=title,description=description,color = discord.Color.orange())
    if description==None:
        await ctx.send("You didn't give a description of your embed. Correct syntax: ```#embed [title] [description]```")
    else:
        await ctx.send(embed=embed)
        
# Finds a meaning of a word

@bot.command()
async def meaning(ctx,word):
    url = "https://www.vocabulary.com/dictionary/" + word + ""
    htmlfile = urllib.request.urlopen(url)
    soup = BeautifulSoup(htmlfile, 'lxml')
    meaning = soup.find(class_="short")

    try:
        meaning = meaning.get_text()
    except AttributeError:
        await ctx.send('Cannot find such word! Check spelling.')

    await ctx.send(f"{ctx.author.mention} MEANING OF **{word}** \n\n ```{meaning}``` ")

# Displays the avatar of a user

@bot.command()
async def avatar(ctx,member: discord.Member=None):
    if not member:
        member = ctx.author

    av_embed = discord.Embed(title=f"Avatar of {member}")
    av = member.avatar_url
    av_embed.set_image(url=(av))
    av_embed.set_footer(text=f"requested by {ctx.author}")
    await ctx.send(embed=av_embed)
    
bot.run('TOKEN')
 
