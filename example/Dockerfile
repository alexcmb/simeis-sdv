FROM python:3.12-slim

WORKDIR /app

# On copie le script client
COPY client.py .

# Le nom du joueur est passé en argument au lancement du container
CMD ["python3", "client.py", "test"]