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

ShinyBOARD = "LUCAS 3 : 1"

load_dotenv()

#lien du feur shiny
gif_path = "FEUR_Shiny.gif"

# Token de votre bot Discord
TOKEN = os.environ['TOKEN']

# ID du salon où envoyer le message
CHANNEL_ID = 1217786944470126672

# ID de l'utilisateur à mentionner
USER_ID = 365180026376945667

# Nombre de réactions pour déclencher l'événement
REACTION_THRESHOLD = 4

# Initialisation du dictionnaire pour stocker le compteur d'utilisation de "quoi" par utilisateur
compteur_quoi = {}

# Définir les intents
intents = discord.Intents.all()
intents.messages = True  # Autoriser la réception et l'envoi de messages
intents.guilds = True    # Autoriser l'accès aux informations des serveurs

# Initialisation du bot avec les intents
bot = commands.Bot(command_prefix='!', intents=intents)

#fonction pour sauvegarder le compteur de quoi dans un fichier csv
async def save_counters_to_csv():
  with open('data/compteurs_quoi.csv', mode='w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['Utilisateur', 'Compteur'])
      for user_id, count in compteur_quoi.items():
          writer.writerow([user_id, count])

# Fonction pour envoyer un message à un canal spécifique à une heure précise
async def send_message_at_time(channel_id, message, hour, minute):
    while True:
        # Récupération de l'heure actuelle
        now = datetime.datetime.now()
        target_time = datetime.datetime(now.year, now.month, now.day, hour, minute)

        # Si l'heure actuelle est passée, passer à l'heure suivante
        if now >= target_time:
            target_time += datetime.timedelta(days=1)

        # Calcul de la durée à attendre
        wait_seconds = (target_time - now).total_seconds()

        # Attendre jusqu'à l'heure spécifiée
        await asyncio.sleep(wait_seconds)

        # Envoyer le message
        channel = bot.get_channel(channel_id)
        if channel:
            # Envoyer un gif de chat
            await channel.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
            # Vérifier s'il s'agit du message "Clémence au dodo ! HOP HOP HOP on arrête de travailler"
            if message == "Clémence au dodo ! HOP HOP HOP on arrête de travailler":
                user = bot.get_user(USER_ID)
                if user:
                    message += f" {user.mention}"
            # Vérifier s'il s'agit des messages nécessitant une mention de rôle
            if "Pause 10h15 ?" in message or "Miam 12h : 🐮 ou 12h15 : 🐔 ?" in message:
                role = discord.utils.get(channel.guild.roles, name="QuoiCouPauseurs")
                if role:
                    message += f" {role.mention}"
            sent_message = await channel.send(message)
            # Ajouter des réactions au message
            if "Pause 10h15 ?" in message:
                await sent_message.add_reaction("🌞")  # Soleil
            elif "Miam 12h : 🐮 ou 12h15 : 🐔 ?" in message:
                await sent_message.add_reaction("🐮")  # Vache
                await sent_message.add_reaction("🐔")  # Poulet
        else:
            print(f"Channel with ID {channel_id} not found. Message not sent.")

# Fonction pour déterminer la réponse à envoyer
def determine_response_QUOI():
    # Générer un nombre aléatoire entre 0 et 1
    random_number = random.random()
    # Si le nombre aléatoire est inférieur ou égal à 0.0003 (0.03% de chance)
    if random_number <= 0.2:
        return "coupaielecafé"
    if random_number <= 0.05:
        return "coutéunemerde"
    else:
        return "COUBEH"

# Fonction pour déterminer la réponse à envoyer
def determine_response_POURQUOI():
    # Générer un nombre aléatoire entre 0 et 1
    random_number = random.random()
    # Si le nombre aléatoire est inférieur ou égal à 0.0003 (0.03% de chance)
    if random_number <= 0.2:
        with open(gif_path, "rb") as file:
            gif = discord.File(file)
            return gif
    else:
        return "Pour FEUR"
    
# Événement de réception de message
@bot.event
async def on_message(message):
    # Vérifie si le mot "quoi" est présent dans le message, indépendamment de la casse
    if 'quoi' in message.content.lower().split():
        # Incrémente le compteur d'utilisation pour cet utilisateur
        user_id = message.author.id
        compteur_quoi[user_id] = compteur_quoi.get(user_id, 0) + 1
        # Déterminer la réponse à envoyer
        response = determine_response_QUOI()
        # Utiliser la fonction reply pour répondre
        await message.reply(response)
      
    if 'pourquoi' in message.content.lower().split():
        # Incrémente le compteur d'utilisation pour cet utilisateur
        user_id = message.author.id
        compteur_quoi[user_id] = compteur_quoi.get(user_id, 0) + 1
        responseP = determine_response_POURQUOI()
        await message.reply(file=responseP)

    if message.content.startswith('!pause'):
        # Envoyer le message "PAUUUUUUUSE !!!!!" dans le canal spécifié
        await message.channel.send('PAUUUUUUUSE !!!!!  ⚠️')

    # Permettre au bot de continuer à traiter les autres événements de message
    await bot.process_commands(message)



#Accès à la liste des compteurs de "quoi"
@bot.command(name="compteurs_quoi")
async def compteurs_quoi(ctx):
    # Crée une liste de chaînes contenant les compteurs de chaque utilisateur
    compteur_liste = [f"{bot.get_user(user_id).name}: {count}" for user_id, count in compteur_quoi.items()]
    # Si aucun utilisateur n'a utilisé "quoi"
    if not compteur_liste:
        await ctx.send("Aucun utilisateur n'a utilisé le mot 'quoi'.")
    else:
        # Envoie la liste des compteurs à l'utilisateur qui a exécuté la commande
        await ctx.send("\n".join(compteur_liste))

#Commande pour proposer une pause l'aprem
@bot.command(name="pause_aprem")
async def pause_aprem(ctx):
    sent_message = await ctx.send("Pause l'aprem ?")
    await sent_message.add_reaction("🌞")  # Soleil

@bot.command(name="shiny_board")
async def shiny_board(ctx):
    sent_message = await ctx.send(ShinyBOARD)
    await sent_message.add_reaction("✌️")  # Soleil

# Événement de réaction
@bot.event
async def on_reaction_add(reaction, user):
    # Vérifier si le message est "pause l'aprem ?" et s'il y a plus de 3 réactions soleil
    if reaction.message.content == "Pause l'aprem ?" and str(reaction.emoji) == "🌞" and reaction.count > 3:
        channel = bot.get_channel(CHANNEL_ID)
        if channel:
            # Envoyer le message "PAUSE !" à 14h30
            await send_message_at_time(channel_id=CHANNEL_ID, message="PAUSE !", hour=13, minute=30)
        else:
            print(f"Channel with ID {CHANNEL_ID} not found. Message not sent.")


# Événement de démarrage du bot
@bot.event
async def on_ready():
    await save_counters_to_csv()
    if bot.user:
        print(f'{bot.user.name} est prêt à fonctionner !')
    else:
        print("Bot user not available yet. Waiting for connection to Discord.")

    # Planifier l'envoi des messages à des heures spécifiques
    # À 9h30
    asyncio.create_task(send_message_at_time(channel_id=CHANNEL_ID, message="Pause 10h15 ?", hour=8, minute=30))
    # À 10h
    asyncio.create_task(send_message_at_time(channel_id=CHANNEL_ID, message="Pause à 10h15 !!", hour=9, minute=0))
    # À 11h
    asyncio.create_task(send_message_at_time(channel_id=CHANNEL_ID, message="Miam 12h : 🐮 ou 12h15 : 🐔 ?", hour=10, minute=0))
    # Clémence au dodo !
    asyncio.create_task(send_message_at_time(channel_id=CHANNEL_ID, message="Clémence au dodo ! HOP HOP HOP on arrête de travailler", hour=14, minute=55))


"""
# Événement de réaction
@bot.event
async def on_reaction_add(reaction, user):
    # Vérifier si le message a atteint le seuil de réactions et a pour titre "Pause 10h15 ?" ou "Miam 12h : 🐮 ou 12h15 : 🐔 ?"
    if reaction.count >= REACTION_THRESHOLD and (reaction.message.content == "Pause 10h15 ?" or reaction.message.content == "Miam 12h : 🐮 ou 12h15 : 🐔 ?" or reaction.message.content == "PAUUUUUUUSE !!!!!  ⚠️"):
        # Créer l'événement
        event_title = "CAFE"
        event_time = reaction.message.created_at.time()
        await reaction.message.channel.send(f"Création de l'événement {event_title} à {event_time} !")

        # Ici, vous pouvez ajouter le code pour créer un événement dans votre calendrier.
"""

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

@bot.event
async def on_disconnect():
    await save_counters_to_csv()


# Lancer le bot
bot.run(TOKEN)

