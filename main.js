const Discord = require('discord.js');
const client = new Discord.Client();
const { google } = require('googleapis');
const { execSync } = require('child_process');

// Token de votre bot Discord
const TOKEN = process.env.TOKEN;

// ID du salon où envoyer le message
const CHANNEL_ID = '1217786944470126672';

// ID de l'utilisateur à mentionner
const USER_ID = '365180026376945667';

// Nombre de réactions pour déclencher l'événement
const REACTION_THRESHOLD = 5;

// Fonction pour envoyer un message à un canal spécifique à une heure précise
async function send_message_at_time(channel, message, hour, minute) {
    while (true) {
        // Récupération de l'heure actuelle
        const now = new Date();
        const target_time = new Date(now.getFullYear(), now.getMonth(), now.getDate(), hour, minute);

        // Si l'heure actuelle est passée, passer à l'heure suivante
        if (now >= target_time) {
            target_time.setDate(target_time.getDate() + 1);
        }

        // Calcul de la durée à attendre
        const wait_seconds = (target_time - now);

        // Attendre jusqu'à l'heure spécifiée
        await new Promise(resolve => setTimeout(resolve, wait_seconds));

        // Envoyer le message
        const channelObj = client.channels.cache.get(channel);
        if (channelObj) {
            // Envoyer un gif de chat
            channelObj.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif");
            let sentMessage = await channelObj.send(message);
            // Ajouter des réactions au message
            if (message.includes("Pause 10h15 ?")) {
                await sentMessage.react("🌞"); // Soleil
            } else if (message.includes("Miam 12h : 🐮 ou 12h15 : 🐔 ?")) {
                await sentMessage.react("🐮"); // Vache
                await sentMessage.react("🐔"); // Poulet
            }
        } else {
            console.log(`Channel with ID ${channel} not found. Message not sent.`);
        }
    }
}

// Événement de message
client.on('message', async message => {
    if (message.content.startsWith('!pause')) {
        // Envoyer le message "PAUUUUUUUSE !!!!!" dans le canal spécifié
        message.channel.send('PAUUUUUUUSE !!!!!  ⚠️');
        await sentMessage.react("⚠️"); // Danger
    }
});

// Événement de démarrage du bot
client.once('ready', async () => {
    console.log(`${client.user.tag} est prêt à fonctionner !`);

    // Planifier l'envoi des messages à des heures spécifiques
    // À 9h30
    send_message_at_time(CHANNEL_ID, "Pause 10h15 ?", 8, 30);
    // À 11h
    send_message_at_time(CHANNEL_ID, "Miam 12h : 🐮 ou 12h15 : 🐔 ?", 10, 0);
    // Clémence au dodo !
    send_message_at_time(CHANNEL_ID, "Clémence au dodo ! HOP HOP HOP on arrête de travailler", 14, 55);
});

// Événement de réaction
client.on('messageReactionAdd', async (reaction, user) => {
    // Vérifier si le message a atteint le seuil de réactions et a pour titre "Pause 10h15 ?" ou "Miam 12h : 🐮 ou 12h15 : 🐔 ?"
    if (reaction.count >= REACTION_THRESHOLD && (reaction.message.content.includes("Pause 10h15 ?") || reaction.message.content.includes("Miam 12h : 🐮 ou 12h15 : 🐔 ?"))) {
        // Créer l'événement
        const event_title = "CAFE";
        const event_time = reaction.message.createdAt;
        reaction.message.channel.send(`Création de l'événement ${event_title} à ${event_time} !`);

        // Créer un événement dans le calendrier
        try {
            execSync(`gcalcli add '${event_title}' --when '${event_time.toISOString().slice(0, 19).replace('T', ' ')}'`);
        } catch (error) {
            console.error(`Erreur lors de la création de l'événement dans le calendrier : ${error}`);
        }
    }
});

// Lancer le bot
client.login(TOKEN);
