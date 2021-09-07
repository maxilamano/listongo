import os
import discord
from discord.ext import commands
from xlsx import *
from fecha import *

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']

client = commands.Bot(command_prefix='o<')

#------------------------------------------------------------------------------------------------------------
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="o<lista"))
    print('BOT INICIADO')
#------------------------------------------------------------------------------------------------------------
@client.command()
async def ping(ctx):
    await ctx.send(f'Latencia total: {round(client.latency * 1000)}ms')
#------------------------------------------------------------------------------------------------------------
@client.command(aliases=['lista','l'],pass_context=True)
async def list(ctx):
    member = ctx.message.author
    server = ctx.message.guild.name
    if  not member.voice:
        await ctx.send("Entra a un canal de voz para poder usar este comando")
        return
    voiceChannel = member.voice.channel
    voiceName = voiceChannel.name
    voiceID = voiceChannel.voice_states.keys()

    voiceUsersName  = []
    voiceBotsName   = []
    for userID in voiceID:
        user = await ctx.guild.fetch_member(userID)
        userNick = user.nick
        if userNick == None:
            userNick = user.name
        
        #comprobar si es bot o no
        if not user.bot:
          voiceUsersName.append(userNick)
        else:
          voiceBotsName.append(userNick)

    #EMBED

    #------------------------------------------------texto------------------------------------------------
    #texto usuarios
    usersNickText = ''
    for user in voiceUsersName:
        usersNickText += user + '\n'
    usersNickText = ''.join(usersNickText)

    #texto bots 
    botsNickText = ''
    for bot in voiceBotsName:
        botsNickText += bot + '\n'
    botsNickText = ''.join(botsNickText)

    embed = discord.Embed(
        title = f'lista de usuarios en {voiceName}',
        colour = discord.Colour.red()
    )
    #-----------------------------------------------------------------------------------------------------

    #lista de usuarios
    if len(voiceUsersName) == 1:
      embed.add_field(name=f' 😃 hay {len(voiceUsersName)} usuario conectado 😃 ', value=usersNickText, inline = True)
    else:
      embed.add_field(name=f' 😃 hay {len(voiceUsersName)} usuarios conectados 😃 ', value=usersNickText, inline = True)

    #lista de bots
    if len(voiceBotsName) > 0:
      if len(voiceBotsName) == 1:
        embed.add_field(name=f' 🤖 hay {len(voiceBotsName)} bot conectado 🤖 ', value=botsNickText, inline = False)
      else:
        embed.add_field(name=f' 🤖 hay {len(voiceBotsName)} bots conectados🤖 ', value=botsNickText, inline = False)

    #obtener fecha
    fecha = fechaFile()
    fechaText = fechaActual()

    embed.set_footer(text=fechaText)
    
    #enviar lista en embed
    await ctx.send(embed=embed)

    #crear y enviar archivo
    nombreArchivo = server +'_'+ fecha + '.xlsx'
    createXlsxFile(nombreArchivo,server, voiceUsersName, voiceBotsName)
    await ctx.send(file=discord.File(nombreArchivo))
    os.remove(nombreArchivo)

    #Imprimir en consola
    print("--------------------LIST REQUEST--------------------")
    print("Server: ", server)
    print("Fecha: ", fechaText)
    print("Voice channel: ", voiceName)
    print("Connected users: ", voiceUsersName)
    print("Connected bots: ", voiceBotsName)
    print("File name: ", nombreArchivo)
    print("----------------------------------------------------")
    print()
client.run(DISCORD_TOKEN)
