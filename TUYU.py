import discord
from discord.ext import commands
import datetime
import asyncio 
import random

f = open("Rules.txt","r")
rules = f.readlines()

gifs = ['https://tenor.com/view/pat-head-loli-dragon-anime-gif-9920853',
'https://tenor.com/view/neko-anime-girl-cute-kawaii-touch-face-gif-14809730',
'https://tenor.com/view/anime-head-pat-pat-very-good-good-girl-gif-17187002',
'https://tenor.com/view/pet-cute-anime-head-pat-good-job-gif-16919214',
'https://tenor.com/view/anime-head-pat-anime-head-rub-neko-anime-love-anime-gif-16121044',
'https://tenor.com/view/pat-head-gif-10947495',
'https://tenor.com/view/anime-pat-head-blushing-happy-gif-13327143',
'https://tenor.com/view/behave-anime-head-pats-head-pat-gif-15882394',
]

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
    await ctx.send("Read carefully :p")

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

            await ctx.send(member_name +" has been unbanned! (～o￣3￣)～")

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
    await member.send("￣へ￣ You have been warned,Because "+reason)
    await ctx.send(member.mention + " has been warned. =￣ω￣=")

@client.command()
async def Pat(ctx):
    random_link = random.choice(gifs)

    await ctx.send(random_link)

    await ctx.send("Nya~ Thx master")

@client.group(invoke_without_command = True)
async def Help(ctx):
    em = discord.Embed(title = "Help", description = "Use ~Help <command> for extended Info about that command")

    em.add_field(name = "Moderation", value = "Kick,Ban,Unban,Warn,Mute,Unmute,Clear,Info")
    em.add_field(name = "Fun", value = "Pat")


    await ctx.send(embed = em)

@Help.command()
async def Kick(ctx):

    em = discord.Embed(title = "Kick", description = "Kicks a member from the server",color = ctx.author.color)

    em.add_field(name = "***Syntax***", value = "~kick <member> [reason]")

    await ctx.send(embed = em)

@Help.command()
async def Ban(ctx):

    em = discord.Embed(title = "Ban", description = "Bans a member from the server",color = ctx.author.color)

    em.add_field(name = "***Syntax***", value = "~ban <member> [reason]")

    await ctx.send(embed = em)
    
@Help.command()
async def Unban(ctx):

    em = discord.Embed(title = "Unban", description = "Unbans a member from the server",color = ctx.author.color)

    em.add_field(name = "***Syntax***", value = "~kick <member>")

    await ctx.send(embed = em)
    
@Help.command()
async def Warn(ctx):

    em = discord.Embed(title = "Warn", description = "Warns a member and sends a Message in thier dms",color = ctx.author.color)

    em.add_field(name = "***Syntax***", value = "~Warn <member> [reason]")

    await ctx.send(embed = em)

@Help.command()
async def Mute(ctx):

    em = discord.Embed(title = "Mute", description = "Mutes a member in the server",color = ctx.author.color)

    em.add_field(name = "***Syntax***", value = "~Mute <member>")

    await ctx.send(embed = em)


@Help.command()
async def Unmute(ctx):

    em = discord.Embed(title = "Unmute", description = "Unmutes a member in the server",color = ctx.author.color)

    em.add_field(name = "***Syntax***", value = "~Unmute <member>")

    await ctx.send(embed = em)

@Help.command()
async def Clear(ctx):

    em = discord.Embed(title = "Clear", description = "Clears a specified number of messages (It will clear 2 messages if no amount is given)",color = ctx.author.color)

    em.add_field(name = "***Syntax***", value = "~Clear <amount>")

    await ctx.send(embed = em)

@Help.command()
async def Info(ctx):

    em = discord.Embed(title = "Info", description = "Gives some necessary info about a user",color = ctx.author.color)

    em.add_field(name = "***Syntax***", value = "~Info <member>")

    await ctx.send(embed = em)

@Help.command()
async def Pat(ctx):

    em = discord.Embed(title = "Pat", description = "No one likes working without headpats :p",color = ctx.author.color)

    em.add_field(name = "***Syntax***", value = "~Pat")

    await ctx.send(embed = em)
  
client.run("ODQxODc2MDc5ODk4Nzg3ODgw.YJtIMg.fD2TUtztXzfultFyKeMuJwJJdGY")
