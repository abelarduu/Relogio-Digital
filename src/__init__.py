from src.window import Window
from customtkinter import CTkImage
from pathlib import Path
from PIL import Image

# Define o caminho para a pasta de assets
ASSETS_PATH = Path(__file__).parent / "assets"

# Cria a janela principal
MASTER = Window(350, 200, "TimeLite", True)

# Carrega e cria as imagens para os botões de controle
IMG_PLAY = CTkImage(light_image=Image.open(ASSETS_PATH / "play.png"), size=(32, 32))
IMG_STOP = CTkImage(light_image=Image.open(ASSETS_PATH / "stop.png"), size=(32, 32))