import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='#',help_command=None)  

#Starting Bot with rich presence

@bot.event
async def on_ready():
    print ('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name=f"#help for more info | Currently in {str(len(bot.guilds))} servers"))

#Ping Command

@bot.command()
async def ping(ctx):
    ping = "Pong :ping_pong: → {} ms".format(round(bot.latency*1000,3))
    embed = discord.Embed(title=ping,color=discord.Color.green())
    await ctx.send(embed=embed)
    
 #Help Command   
 
@bot.command()
async def help(ctx):
    help_embed = discord.Embed(title="General Help. Prefix - #",description="Hey there! Thanks for using Dissobot 😃. Here are different group of commands that might guide you.",color=0x8920EB)
    help_embed.add_field(name="Moderation 🛠",value="`#helpmod`",inline=True)
    help_embed.add_field(name="Management ⚙",value="`#helpmgt`",inline=True)
    help_embed.add_field(name="Fun and Games 🎲",value="`#helpfun`",inline=True)
    help_embed.add_field(name="Miscellaneous 😃",value="`#helpmisc`",inline=True)
    help_embed.set_footer(text=f"requested by {ctx.author}")
    user = bot.get_user(859809701298569227)
    pfp = user.avatar_url
    help_embed.set_thumbnail(url=pfp)
    await ctx.send(embed=help_embed)

@bot.command()
async def helpmod(ctx):
    mod_embed = discord.Embed(title="Moderation commands",description="Here is a list of commands for moderation")
    mod_embed.add_field(name='`#ban [mention user]`',value='**bans a user permanently**',inline=False)
    mod_embed.add_field(name='`#kick [mention user]`',value='**kicks a user**',inline=False)
    mod_embed.add_field(name='`#mute [mention user]`',value='**mutes a user permanently**',inline=False)
    mod_embed.add_field(name='`#unmute [mention user]`',value='**unmutes a user**',inline=False)
    mod_embed.set_footer(text=f"requested by {ctx.author}")    
    await ctx.send(embed=mod_embed)


@bot.command()
async def helpmgt(ctx):
    mgmt_embed = discord.Embed(title="Management commands",description="Here is a list of commands for server management")
    mgmt_embed.add_field(name='`#addchannel [channel name]`',value='**Creates a channel** (eg. `#delchannel Test Channel`)',inline=False)
    mgmt_embed.add_field(name='`#delchannel [channel name]`',value='**Deletes a channel** (eg. `#delchannel Test Channel`)',inline=False)
    mgmt_embed.add_field(name='`#role [name of role] [mention user]`',value='**Gives/takes a role from a user** (eg. `#role Bot` <@859809701298569227>)',inline=False)
    mgmt_embed.add_field(name='`#addrole [name of role]`',value='**Creates a role for the server** (eg. `#addrole Member`)',inline=False)
    mgmt_embed.add_field(name='`#userinfo [user mention]`',value='**Looks up the information of a member in the server** (eg. `#userinfo` <@859809701298569227>)',inline=False)
    mgmt_embed.set_footer(text=f"requested by {ctx.author}")    
    await ctx.send(embed=mgmt_embed)

@bot.command()
async def helpfun(ctx):
    fun_embed = discord.Embed(title="Fun commands",description="Here is a list of commands for fun and games")
    fun_embed.add_field(name='`#kill [user mention]`',value='**Kills a user** (eg. `#kill` <@859809701298569227>)',inline=False)
    fun_embed.add_field(name='`#meme`',value='**Sends a meme from reddit**',inline=False)
    fun_embed.add_field(name='`#edgy`',value='**Sends a meme for the Shitposting edge Lords**',inline=False)
    fun_embed.add_field(name='`#subreddit [name of a subreddit]`',value='**Sends a meme/post from a selected subreddit** (eg. `#subreddit pewdiepie`)',inline=False)
    fun_embed.add_field(name='`#rps`',value='**Plays rock paper scissors with you**',inline=False)
    fun_embed.add_field(name='`#guessword`',value='**Plays a guess word game with you**',inline=False)
    fun_embed.set_footer(text=f"requested by {ctx.author}")    
    await ctx.send(embed=fun_embed)

@bot.command()
async def helpmisc(ctx):
    misc_embed = discord.Embed(title="Fun commands",description="Here is a list of commands for fun and games")
    misc_embed.add_field(name='`#calculate [expression]`',value='**Calculates an expression for you** (eg. `#calculate 2+2-3*4/5`)',inline=False)
    misc_embed.add_field(name='`#ytsearch [video name]`',value='**Sends a video according to the name** (eg. `#ytsearch Valorant gameplay`)',inline=False)
    misc_embed.add_field(name='`#google [search something]`',value='**Sends the first link according to your search** (eg. `#google Sports news`)',inline=False)
    misc_embed.add_field(name='`#meaning [word]`',value='**Sends the meaning of a particular word** (eg. `#meaning life`)',inline=False)
    misc_embed.add_field(name='`#poll [title], [option 1], [option 2]`',value='**Sends a poll (max 6 options)** (eg. `#poll Which one?, Windows, MacOS, Linux`)',inline=False)
    misc_embed.add_field(name='`#giveaway [time] [prize]`',value='**Sends a react giveaway thing** (eg. `#giveaway 1h nitro classic`)',inline=False)
    misc_embed.add_field(name='`#embed [title] [description]`',value='**Embeds what you send** (eg. `#embed "This is a title" this is a description`)',inline=False)
    misc_embed.add_field(name='`#avatar [user mention]`',value='**Displays the avatar of a user** (eg. `#avatar` <@859809701298569227>)',inline=False)


    misc_embed.set_footer(text=f"requested by {ctx.author}")    
    await ctx.send(embed=misc_embed)
   

bot.run('TOKEN')

 
