import discord
from discord.ext import commands
import datetime
import asyncio 
import random

f = open("Rules.txt","r")
rules = f.readlines()

filtered_words = ["Cunt","Nigger","Fuck","Bitch","Asshole","Motherfucker","cunt","nigger","fuck","bitch","asshole","motherfucker"]

client = commands.Bot(command_prefix="~")

@client.event
async def on_ready():
    print("Bot Is Online")

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("Hmph~ You Lack Permissions")
        await ctx.message.delete()
    elif isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Nu! Please enter the required info.")
        await ctx.message.delete()
    else:
        raise error

@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()

    await client.process_commands(msg)

@client.command()
async def TUYU(ctx):
    await ctx.send("(～￣▽￣)～")
    await ctx.send("Any work?")

@client.command()
async def Rule(ctx,*,number):
    await ctx.send(rules[int(number)-1])

@client.command()
@commands.has_permissions(manage_messages = True)
async def Clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount)
    await ctx.send("ヾ(≧▽≦*)o Successfully removed")
    
@client.command()
@commands.has_permissions(kick_members = True)
async def Kick(ctx,member: discord.Member,*,reason= "No reason provided"):
    try:
        await member.send("T-T Looks like you have been kicked,Because "+reason)
    except:
        await ctx.send("ヾ(≧へ≦)〃 ,The Member's dms are closed")
    await member.kick(reason=reason)

@client.command()
@commands.has_permissions(ban_members = True)
async def Ban(ctx,member: discord.Member,*,reason= "No reason provided"):
    try:
        await member.send("T-T Looks like you have been banned,Because "+reason)
    except:    
        await ctx.send("(* ￣︿￣) The Member's dms are closed")        
    await member.ban(reason=reason)

@client.command()
@commands.has_permissions(ban_members=True)
async def Unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):

            await ctx.guild.unban(user)
            await ctx.send("nya~" + member_name +" has been unbanned! (～o￣3￣)～")
            return
    await ctx.send(member+" was not found 〒▽〒")

@client.command()
@commands.has_permissions(kick_members=True)
async def Mute(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(835075972893769759)

    await member.add_roles(muted_role)

    await ctx.send(member.mention + " has been muted. Such a bad boy :(")

@client.command()
@commands.has_permissions(kick_members=True)
async def Unmute(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(835075972893769759)

    await member.remove_roles(muted_role)

    await ctx.send(member.mention + " has been unmuted. U behaved well :p")

@client.command()
@commands.has_permissions(kick_members=True)
async def Info(ctx, member : discord.Member):
    embed = discord.Embed(title = member.name , description = member.mention , color = discord.Color.blue())
    embed.add_field(name = "ID", value = member.id , inline = True)
    embed.set_thumbnail(url = member.avatar_url)
    embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members = True)
async def Warn(ctx,member: discord.Member,*,reason= "No reason provided"):
    await member.send("￣へ￣ have been warned,Because "+reason)
    await ctx.send(member.mention + " has been warned. =￣ω￣=")

@client.command()
async def Pat(ctx):
    await ctx.send("https://tenor.com/view/anime-head-pat-anime-head-rub-neko-anime-love-anime-gif-16121044")
    await ctx.send("Nya~! Thx master")
    
client.run("ODQxODc2MDc5ODk4Nzg3ODgw.YJtIMg.fD2TUtztXzfultFyKeMuJwJJdGY")
