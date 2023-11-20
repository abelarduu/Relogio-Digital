from customtkinter import CTk, CTkButton, CTkImage, CTkLabel, CTkTabview
from time import  localtime, gmtime, strftime
from PIL import Image

class Master(CTk):
    def __init__(self, width:int, height:int, title:str, resizable:bool):
        super().__init__()
        self.title(title)
        self.minsize(width, height)
        self.resizable(resizable, resizable)
        #self.iconbitmap("resources/icon.ico")

        self.rowconfigure(3, weight=3)
        self.columnconfigure(3, weight=3)

class App:
    def __init__(self):
        self.master = Master(350,200,'Relogio Digital', True)
        self.tab_view= CTkTabview(self.master, height=90)
        self.tab_view.grid(row=2, column=2, rowspan=3, columnspan=3)
        self.tab_view.add("Relógio Digital")
        self.tab_view.add("Cronômetro")
        
        self.n=0
        self.btnPlay= False
        self.time= strftime("%T",localtime())
        self.timer = strftime("%T",gmtime(self.n))

        self.timeLbl= CTkLabel(self.tab_view.tab("Relógio Digital"), text=self.time, font=("LCDD", 90))
        self.timeLbl.grid(sticky="nsew", padx=5)
        self.timerLbl= CTkLabel(self.tab_view.tab("Cronômetro"), text=self.timer, font=("LCDD", 90))
        self.timerLbl.grid(sticky="nsew", padx=5)
        
        self.imgPlay= CTkImage(light_image=Image.open("resources/play.png"),size=(32,32))
        self.imgStop= CTkImage(light_image=Image.open("resources/stop.png"),size=(32,32))
        self.btnTimer= CTkButton(self.tab_view.tab("Cronômetro"), text= None, bg_color="transparent", image= self.imgPlay, command= self.play)
        self.btnTimer.grid(sticky="nsew", padx=5)

        self.get_time()
        self.master.mainloop()

    def play(self):
        self.btnPlay= True
        self.btnTimer.configure(image= self.imgStop, command= self.stop)

    def stop(self):
        self.btnPlay= False
        self.btnTimer.configure(image= self.imgPlay, command= self.play)

    def get_time(self):
        if self.btnPlay: self.n+=1
        else: self.n=0

        self.time= strftime("%T",localtime())
        self.timer= strftime("%T",gmtime(self.n))

        self.timeLbl.configure(text=self.time)
        self.timerLbl.configure(text=self.timer) 

        self.master.after(1000, self.get_time)

if __name__ == "__main__":
    App()