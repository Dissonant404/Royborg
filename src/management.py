import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='#')  

# Creates a channel

@bot.command()
@commands.has_permissions(manage_channels = True)

async def addchannel(ctx, *,channel_name):
    
        await ctx.guild.create_text_channel(channel_name)
        channel_name=list(channel_name)
        for n,i in enumerate(channel_name):
            if i==' ':
                channel_name[n]='-'

        channel_name = ''.join(map(str, channel_name))
        channel = discord.utils.get(ctx.guild.channels, name=channel_name)

        channel_id = channel.id
        await ctx.send("A new channel was successfully created called <#{}>".format(channel_id))
 
# Deletes a channel

@bot.command()
@commands.has_permissions(manage_channels = True)

async def delchannel(ctx, *,channel_name):
   guild = ctx.message.guild
   existing_channel = discord.utils.get(guild.channels, name=channel_name)
   if existing_channel is not None:
      await existing_channel.delete()
   else:
      await ctx.send(f'No channel named, "{channel_name}", was found')
   await ctx.send("A channel was successfully deleted called **{}**".format(channel_name))
  
# Gives/Takes a role from a user

@bot.command()
@commands.has_permissions(manage_roles = True)

async def role(ctx,member:discord.Member=None,*,role):
    guild=ctx.guild
    role = discord.utils.get(guild.roles,name=role)
    if role in member.roles:
        await member.remove_roles(role)
        role_embed = discord.Embed(title="Role removed",description=f"{ctx.author.mention} has removed {role} role from {member.mention}")
        await ctx.send(embed=role_embed)
    else:
        await member.add_roles(role)
        role_embed = discord.Embed(title="Role added",description=f"{ctx.author.mention} has added {role} role to {member.mention}")
        await ctx.send(embed=role_embed)
        
# Creates a role for a server

@bot.command()
@commands.has_permissions(manage_roles = True)

async def addrole(ctx,*,role):
    guild = ctx.guild
    role = await guild.create_role(name=role)
    role_embed = discord.Embed(title="Role created",description=f"{ctx.author.mention} has created a role called {role}")
    await ctx.send(embed=role_embed)

# Checks the info of a User

@bot.command()
async def userinfo(ctx,member:discord.Member=None):
    if not member:
        member = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in member.guild_permissions if p[1]])
    
    user = bot.get_user(member.id)
    # pfp = user.avatar_url

    info_embed = discord.Embed(title=f"User Information",color=0x03FF06)
    info_embed.set_thumbnail(url=member.avatar_url)
    info_embed.add_field(name="Username",value = member,inline=True)

    # info_embed.set_image(url=(pfp))
    
    info_embed.add_field(name="Joined at:",value = member.joined_at.strftime(date_format),inline=True)
    info_embed.add_field(name="Registered at:",value = member.created_at.strftime(date_format),inline=True)

    if len(member.roles) > 1:
        role_string = ' '.join([r.mention for r in member.roles][1:])
        info_embed.add_field(name="Roles [{}]".format(len(member.roles)-1), value=role_string, inline=True)

    info_embed.add_field(name="Guild permissions", value=perm_string, inline=False)

    info_embed.set_footer(text='ID: ' + str(member.id) + f' • requested by {ctx.author}' )

    await ctx.send(embed=info_embed)

bot.run('TOKEN')
