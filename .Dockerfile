# Utilisez l'image de base Python
FROM python:3.11-slim

# Définissez le répertoire de travail dans l'image
WORKDIR /app

# Copiez le code de l'application Flask dans le conteneur
COPY app/ /app/

# Installez Pipenv
RUN pip install pipenv

# Copiez le fichier Pipfile et Pipfile.lock dans le conteneur
COPY Pipfile Pipfile.lock /app/

# Installez les dépendances nécessaires
RUN pipenv install --system --deploy

# Exposez le port sur lequel l'application Flask écoute
EXPOSE 80

# Commande pour exécuter l'application Flask lorsque le conteneur est démarré
CMD ["python", "app/main.py"]
