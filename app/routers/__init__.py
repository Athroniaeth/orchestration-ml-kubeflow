from fastapi import APIRouter

router = APIRouter

""" On se sert du fichier __init__.py pour 'capturer' toutes les routes des dossiers enfants. """
import sys
from pathlib import Path
import importlib
from fastapi import APIRouter

router = APIRouter()

current_directory = Path(__file__).parent

# Listez tous les fichiers Python dans le dossier actuel, sauf "__init__.py"
python_files = [file.stem for file in current_directory.glob("*.py") if file.is_file() and file.stem != "__init__"]

# Importez dynamiquement le module
for file in python_files:
    sys.path.append(f"{current_directory}")
    module = importlib.import_module(f"{file}")
    sys.path.remove(f"{current_directory}")

    if hasattr(module, "router"):
        print(f"Add router '/{file}'")
        router.include_router(getattr(module, "router"), prefix=f'/{file}')  # pas de préfix pour les rediriger sur la racine
        # TODO : Il faudrait lancer une exception, et faire un test unitaire pour savoir si l'application gère toujours de manière dynamique les ajouts des routers
