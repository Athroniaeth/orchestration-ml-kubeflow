import requests

url = "http://127.0.0.1:8000/predict/"

# Ouvrir le fichier image en mode binaire
with open("dog.jpeg", "rb") as f:
    # Effectuer la requête POST
    response = requests.post(url, files={"file": f})

# Afficher la réponse
print(response.json())
