import __init__

from pathlib import Path
import os

APP_PATH = Path(os.getenv("APP_PATH"))
ROBOFLOW_API_KEY = os.getenv("ROBOFLOW_API_KEY")

from roboflow import Roboflow

DATASETS_PATH = APP_PATH / 'datasets'

rf = Roboflow(api_key=ROBOFLOW_API_KEY)
project = rf.workspace("ultimate-0fe1g").project("elephants_16")
dataset = project.version(1).download("yolov8", location=f'{DATASETS_PATH}')
