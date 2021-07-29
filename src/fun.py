import discord
from discord.ext import commands
import praw
from english_words import english_words_set
import random

bot = commands.Bot(command_prefix='#')

reddit = praw.Reddit(client_id ="[Client ID]",
                     client_secret = "[Client Secret]",
                     username = "[Username]",
                     password = "[password]",
                     user_agent = "royborg")

# Kills a user in some way

@bot.command()
async def kill(ctx,user:discord.User = None):
    if not user:
        await ctx.send(f"{ctx.author.mention} Please mention someone you wanna kill")
    ways_to_die = ['died of ketamine overdose.','died from choking five gallons of cumjar',f'contemplated suicide after dealing with the stupidity of {ctx.author.mention}','was assassinated by the Minecraft stan leader after he said "Dream sucks" in his SMP server',f'amputated his legs in an isolated beach to fill his starving tummy. {user.mention} died of blood loss',f'was stabbed by {ctx.author.mention} 69 times',f'died after {ctx.author.mention} pulled his tongue out so hard that it came off']
    random_death = random.choice(ways_to_die)
    await ctx.send("<@{}> {}".format(user.id,random_death))

# Sends a meme from r/memes

@bot.command()
async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    top = subreddit.top(limit=50,time_filter="day")
    for submission in top:
        all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    meme_embed = discord.Embed(title=name,color=discord.Color.red())
    meme_embed.set_image(url = url)
    await ctx.send(embed=meme_embed)
    

    

    
# Minigames | Rock paper scissors

@bot.command()
async def rps(ctx):
    await ctx.send("Welcome to Rock Paper Scissors Game! \n What do you want to choose: rock 🪨, paper 📰 or scissor ✂ ?")
    msg = await bot.wait_for('message')
    l = ['rock','paper','scissor']
    bot_turn = random.choice(l)

    if msg.content.lower()== bot_turn:
        await ctx.send(f"I chose {bot_turn}. The game ended in a tie. GGs!")
    elif (msg.content.lower() == 'rock' and bot_turn=='scissor') or (msg.content.lower() == 'paper' and bot_turn=='rock') or (msg.content.lower() == 'scissor' and bot_turn=='paper'):
         await ctx.send(f"I chose {bot_turn}. You win! GGs!")
    elif (msg.content.lower() == 'scissor' and bot_turn=='rock') or (msg.content.lower() == 'rock' and bot_turn=='paper') or (msg.content.lower() == 'paper' and bot_turn=='scissor'):
        await ctx.send(f"I chose {bot_turn}. You lost! GGs Next time")
        
# Minigames | Guess word game

@bot.command()
async def guessword(ctx):
    c=0
    player = ctx.author.mention
    l1 = []
    l = list(english_words_set)
    await ctx.send(f"{player} Welcome to Guess the Word Game! In this game, we will give you **4** hints and you have to guess the word. Please pick a difficulty level before we start. \n\n 🟩 Easy \n 🟨 Normal \n 🟥 Hard")
    msg = await bot.wait_for('message')

    if msg.content.lower() == 'easy' or msg.content.lower() == 'Easy':
        
        for i in l:
            if len(i) < 5:
                l1.append(i)

    elif msg.content.lower() == 'normal' or msg.content.lower() == 'Normal':
        for i in l:
            if len(i) > 5 and len(i) < 10:
                l1.append(i)

    elif msg.content.lower() == 'hard' or msg.content.lower() == 'Hard':
        for i in l:
            if len(i) > 10:
                l1.append(i)


    word = random.choice(l1)
    congrats_message =f"{player} Congratulations! You guessed the word. The word was {word}"
    vowel_list = []
    for vowel in word:
        if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u":
            vowel_list.append(vowel) 

    await ctx.send(f"{player} Hint 1: Your word contains {len(word)} letters")
    msg_word_1 = await bot.wait_for('message')
    if msg_word_1.content.lower() == word:
        await ctx.send(congrats_message)
    else:
        await ctx.send(f"{player} Hint 2: First letter of word is {word[0]}")
        msg_word_2 = await bot.wait_for('message')

        if msg_word_2.content.lower()==word:
            await ctx.send(congrats_message)
        else:
            await ctx.send(f"{player} Hint 3: Last letter of word is {word[-1]}")
            msg_word_3 = await bot.wait_for('message')
            if msg_word_3.content.lower()==word:
                await ctx.send(congrats_message)
            else:
                await ctx.send(f"{player} Hint 4: The word contains vowel(s) {vowel_list}")
                msg_word_4 = await bot.wait_for('message')
                if msg_word_4.content.lower()==word:
                    await ctx.send(congrats_message)
                else:
                    await ctx.send(f"That was the last hint. You lost {player}. The correct word was **{word}**. Better luck next time!")
                    

bot.run('TOKEN')
