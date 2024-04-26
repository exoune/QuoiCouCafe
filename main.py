import discord
import asyncio
import datetime
from discord.ext import commands
from discord import TextChannel
import os
from dotenv import load_dotenv
import sys
import csv
import random

load_dotenv()

# Token de votre bot Discord
TOKEN = os.environ['TOKEN']

# ID du salon où envoyer le message
CHANNEL_ID = 1217786944470126672

# ID de l'utilisateur à mentionner
USER_ID = 365180026376945667

# Nombre de réactions pour déclencher l'événement
REACTION_THRESHOLD = 4

# Définir les intents
intents = discord.Intents.all()
intents.messages = True  # Autoriser la réception et l'envoi de messages
intents.guilds = True    # Autoriser l'accès aux informations des serveurs

# Initialisation du bot avec les intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Événement de réception de message
@bot.event
async def on_message(message):
    # Générer un nombre aléatoire entre 0 et 1
    random_number = random.random()

    # Vérifier si le message contient l'un des mots interdits
    mots_interdits = ["étienne", "etienne", "thierry", "jérémy", "jeremy"]
    if any(mot in message.content.lower() for mot in mots_interdits):
        # Envoyer un gif d'alerte
        await message.channel.send("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeW1xb2kxa2ZzeXBwYWZ6ajcyNWRrOXZvM3dob3N1MmdvdzB1MmpiciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3og0IOa1X349KZ8E1i/giphy.gif")
        # Envoyer le message d'avertissement
        await message.channel.send("ATTENTION mot interdit ! Utilisez plutôt les e-j-t-word.")

    if random_number <= 0.0009:
            # Envoyer la réponse aléatoire
            await message.channel.send("T'as les cramptés")

    # Vérifier si l'utilisateur est celui spécifié
    if message.author.id == 124917171359973376:
        # Vérifier si le nombre aléatoire est inférieur ou égal à 0.05 (probabilité de 5%)
        if random_number <= 0.0005:
            # Envoyer un gif de dab avec un message
            await message.channel.send("https://i.gifer.com/hbA.gif")
            await message.channel.send("Regarde c'est cool!")
    
    if "lune" in message.content.lower():
        # Envoyer une image de la lune
        await message.channel.send("https://imgur.com/gallery/gDd42uN")

    # Vérifier si le message commence par "!pause"
    if message.content.startswith('!pause'):
        # Envoyer le message "PAUUUUUUUSE !!!!!" dans le canal spécifié
        await message.channel.send('PAUUUUUUUSE !!!!!  ⚠️')

    # Continuer à traiter les autres événements de message
    await bot.process_commands(message)

#Commande pour proposer une pause l'aprem
@bot.command(name="pause_aprem")
async def pause_aprem(ctx):
    sent_message = await ctx.send("Pause l'aprem ?")
    await sent_message.add_reaction("🌞")  # Soleil

# #Commande pour souhaiter un bon anniversaire
# @bot.command(name="annif")
# async def annif(ctx):
#     sent_message = await ctx.send("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmplczEwaWpld2d3dmxnMDZsbTZhMThyaHNrNjdibm54anlva2g4MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LzwcNOrbA3aYvXK6r7/giphy.gif")
#     await ctx.send("Bon anniversaire " + bot.get_user(365180026376945667).mention + "!")
#     await sent_message.add_reaction("🥳")

#Commande pour souhaiter un bon anniversaire
@bot.command(name="annif")
async def annif(ctx):
    sent_message = await ctx.send("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWsxd3N0ODI2eTd3MXZqMjBhc29peGVsbWx4NXNwOTRicnE2cndjaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lqf9NUmX7NjpCv31Er/giphy.gif")
    await ctx.send("Bon anniversaire " + bot.get_user(124917171359973376).mention + "!")
    await sent_message.add_reaction("🥳")

    # # Vérifier si c'est le 02 avril - AMBRE
    # await channel.send("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmplczEwaWpld2d3dmxnMDZsbTZhMThyaHNrNjdibm54anlva2g4MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LzwcNOrbA3aYvXK6r7/giphy.gif")
    # await channel.send("Bon anniversaire " + bot.get_user(365180026376945667).mention + "!")

    # # Vérifier si c'est le 13 avril - CLEMENCE
    # await channel.send("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmplczEwaWpld2d3dmxnMDZsbTZhMThyaHNrNjdibm54anlva2g4MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LzwcNOrbA3aYvXK6r7/giphy.gif")
    # await channel.send("Bon anniversaire " + bot.get_user(365180026376945667).mention + "!")
    
    # # Vérifier si c'est le 18 mai - BENJAMIN
    # await channel.send("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWsxd3N0ODI2eTd3MXZqMjBhc29peGVsbWx4NXNwOTRicnE2cndjaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lqf9NUmX7NjpCv31Er/giphy.gif")
    # await channel.send("Bon anniversaire " + bot.get_user(124917171359973376).mention + "!")
    
    # # Vérifier si c'est le 21 mai - FIONA
    # await channel.send("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTE1emdnNTR4ZTFlZnNva2p1cDUwenhma3k1bmt2MDAwYWZibmczaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IFjSbBHETzzr6GJdwW/giphy-downsized-large.gif")
    # await channel.send("Bon anniversaire " + bot.get_user(386880970655268865).mention + "!")
    
    # # Vérifier si c'est le 05 septembre - GWENDAL
    # await channel.send("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWpjdHR6M3c0b2Ezdnh5ZHoyazl6am85dTBoNDF2M2lsdDU2Y3Y5ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Svc9uoN3nUHbq/giphy.gif")
    # await channel.send("Bon anniversaire " + bot.get_user(217279235021209600).mention + "!")
    
    # # Vérifier si c'est le 06 septembre - LUCAS
    # await channel.send("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM243YzNteHh5c3J2eWdzaHdhZGprdHJnb20yZ2wwcHdibG1pZWZiMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/d3l79306Ne4Y8/giphy-downsized-large.gif")
    # await channel.send("Bon anniversaire " + bot.get_user(300762664714371073).mention + "!")


# Événement de démarrage du bot
@bot.event
async def on_ready():
    #await save_counters_to_csv()
    if bot.user:
        print(f'{bot.user.name} est prêt à fonctionner !')
    else:
        print("Bot user not available yet. Waiting for connection to Discord.")

#commande Coucou
@bot.command(name="coucou")
async def bonjour(ctx):
    reponse=f"Ça va, {ctx.message.author.name} ?"
    await ctx.reply(reponse)
    print(f"Réponse à message {ctx.message.id} : {reponse}")

#liste des commandes
@bot.command(name="aide")
async def aide(ctx):
    # Construire la liste des commandes disponibles
    commandes_disponibles = [f"!{command.name}" for command in bot.commands]

    # Envoyer la liste des commandes à l'utilisateur qui a exécuté la commande
    await ctx.send("Voici les commandes disponibles :\n" + "\n".join(commandes_disponibles))


# Lancer le bot
bot.run(TOKEN)

