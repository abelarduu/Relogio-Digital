from src import *
from customtkinter import CTk, CTkButton, CTkLabel, CTkTabview
from time import localtime, gmtime, strftime

class App:
    def __init__(self):
        """Inicializa a aplicação e seus componentes."""
        # Declarando Variáveis
        self.n = 0
        self.btn_play = False
        self.time = strftime("%T", localtime())
        self.timer = strftime("%T", gmtime(self.n))
        
        self.tab_view = CTkTabview(MASTER, height=90)
        self.tab_view.grid(row=2, column=2, rowspan=3, columnspan=3)
        self.tab_view.add("Digital Clock")
        self.tab_view.add("Stopwatch")
        
        # Criando elementos da interface
        self.time_lbl = CTkLabel(self.tab_view.tab("Digital Clock"),
                                 text=self.time,
                                 font=("LCDD", 90))

        self.timer_lbl = CTkLabel(self.tab_view.tab("Stopwatch"),
                                  text=self.timer,
                                  font=("LCDD", 90))

        self.btn_timer = CTkButton(self.tab_view.tab("Stopwatch"),
                                   text=None,
                                   bg_color="transparent",
                                   image=IMG_PLAY,
                                   command=self.play)
      
        # Adicionando elementos na interface
        self.time_lbl.grid(sticky="nsew", padx=5)
        self.timer_lbl.grid(sticky="nsew", padx=5)
        self.btn_timer.grid(sticky="nsew", padx=5)

        self.get_time()
        MASTER.mainloop()

    def play(self):
        """Inicia o cronômetro."""
        self.btn_play = True
        self.btn_timer.configure(image=IMG_STOP, command=self.stop)

    def stop(self):
        """Para o cronômetro."""
        self.btn_play = False
        self.btn_timer.configure(image=IMG_PLAY, command=self.play)

    def get_time(self):
        """Atualiza o horário e o cronômetro a cada segundo."""
        if self.btn_play:
            self.n += 1
        else:
            self.n = 0

        self.time = strftime("%T", localtime())
        self.timer = strftime("%T", gmtime(self.n))

        self.time_lbl.configure(text=self.time)
        self.timer_lbl.configure(text=self.timer)
        MASTER.after(1000, self.get_time)

if __name__ == "__main__":
    App()