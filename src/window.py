from customtkinter import CTk, set_appearance_mode
from pathlib import Path

# Define o caminho para a pasta de assets
ASSETS_PATH = Path(__file__).parent / "assets"

class Window(CTk):
    def __init__(self, width, height, title, resizable):
        """Inicializa a janela principal da aplicação."""
        super().__init__()
        self.title(title)
        self.minsize(width, height)
        self.resizable(resizable, resizable)
        self.iconbitmap(ASSETS_PATH / "icon.ico")
        set_appearance_mode("light")
        
        # Configura o peso das linhas e colunas para o layout
        self.rowconfigure(3, weight= 3)
        self.columnconfigure(3, weight= 3)