import discord
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands

bot = commands.Bot(command_prefix='#')  

#Ban Command

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    if True:
      await member.ban(reason = reason)
      embed = discord.Embed(title="Banned a user",description="{} banned by {}. Reason - {}".format(member.mention,ctx.message.author.mention,reason),color=discord.Color.red())
      await ctx.send(embed=embed)
    else:
      await ctx.send(f"{ctx.author.mention} I don't have the permission to do that. Please check if my role is higher than the person you want to ban")


@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.author.mention)
        await ctx.send(text)
        
#Unban Command

@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
      if True:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(title="Unbanned a user",description="{} unbanned by {}.".format(user.mention,ctx.message.author.mention),color=discord.Color.blue())
                await ctx.send(embed=embed)
                # await ctx.send(f'Unbanned {user.mention}')
                return
      else:
        await ctx.send(f"{ctx.author.mention} I don't have the permission to do that. Please check if my role is higher than the person you want to unban")
        
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.author.mention)
        await ctx.send(text)
        
#Kick Command

@bot.command()
@commands.has_permissions(kick_members = True)

async def kick(ctx, member : discord.Member, *, reason = None):
  
    await member.kick(reason = reason)
    embed = discord.Embed(title="Kicked a user",description="{} kicked by {}. Reason - {}".format(member.mention,ctx.message.author.mention,reason),color=discord.Color.gold())
    await ctx.send(embed=embed)


@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.author.mention)
        await ctx.send(text)
        
 #Mute Command

async def mute(ctx, member: discord.Member=None, *, reason=None):
    if not member:
        await ctx.send("You must mention a member to mute!")

    guild = ctx.guild
    Muted = discord.utils.get(guild.roles, name="Muted")
    if not Muted:
      Muted = await guild.create_role(name="Muted")
      for channel in guild.channels:
          await channel.set_permissions(Muted, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(Muted, reason=reason)
    muted_embed = discord.Embed(title="Muted a user", description=f"{member.mention} Was muted by {ctx.author.mention} for {reason}")
    await ctx.send(embed=muted_embed)
 


@mute.error
async def mute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.author.mention)
        await ctx.send(text) 
        
#Unmute Command

@bot.command()
@commands.has_permissions(manage_roles = True)

async def unmute(ctx, member: discord.Member=None, *,reason=None):
        guild = ctx.guild
        Muted = discord.utils.get(guild.roles, name="Muted")
        await member.remove_roles(Muted)
        unmute_embed = discord.Embed(title="Mute over!", description=f" {member.mention} unmuted by {ctx.author.mention}")
        await ctx.send(embed=unmute_embed)


@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.author.mention)
        await ctx.send(text)
        
 bot.run('TOKEN')

 
