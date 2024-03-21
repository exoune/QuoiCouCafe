# Utilisez une image Python officielle en tant qu'image de base
FROM python:3.11-bookworm

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le contenu actuel du répertoire de l'hôte dans le répertoire de travail du conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -U discord.py python-dotenv pymongo

# Commande pour exécuter le bot lorsque le conteneur démarre
CMD ["python", "main.py"]
