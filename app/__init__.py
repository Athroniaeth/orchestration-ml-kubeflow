from pathlib import Path
import os
from dotenv import load_dotenv

print('initialisation du projet')

PROJECT_PATH = Path().absolute().parent
APP_PATH = PROJECT_PATH / 'app'
ENV_PATH = PROJECT_PATH / '.env'

load_dotenv(dotenv_path=ENV_PATH)

os.environ['PROJECT_PATH'] = f'{PROJECT_PATH}'
os.environ['APP_PATH'] = f'{APP_PATH}'