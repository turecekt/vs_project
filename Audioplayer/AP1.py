# Import pozadovanych modulu a knihoven
from tkinter import *
import pygame
import os


class MusicPlayer:
    # Definovani Konstruktoru
    def __init__(self, root):
        self.root = root
        # Nazev okna
        self.root.title("Music Player")
        # Geometrie okna
        self.root.geometry("1000x200+200+200")
        # Zahajeni PyGame
        pygame.init()
        # Zahajeni PyGame Mixer
        pygame.mixer.init()
        # Deklarace promenne hudby
        self.track = StringVar()
        # Deklarace stavu promenne
        self.status = StringVar()

        # Vytvoreni ramecku hudby pro label hudby a stavovy label
        trackframe = LabelFrame(self.root, text="Song Track", font=("times new roman", 15, "bold"), bg="grey",
                                fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)
        # Vlozeni labelu hudby
        songtrack = Label(trackframe, textvariable=self.track, width=20, font=("times new roman", 24, "bold"),
                          bg="grey", fg="gold").grid(row=0, column=0, padx=10, pady=5)
        # Vlozeni labelu stavu
        trackstatus = Label(trackframe, textvariable=self.status, font=("times new roman", 24, "bold"), bg="grey",
                            fg="gold").grid(row=0, column=1, padx=10, pady=5)

        # Vytvoreni ramecku tlacitek
        buttonframe = LabelFrame(self.root, text="Control Panel", font=("times new roman", 15, "bold"), bg="grey",
                                 fg="white", bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=100, width=600, height=100)
        # Vlozeni tlacitka Play
        playbtn = Button(buttonframe, text="PLAY", command=self.playsong, width=6, height=1,
                         font=("times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=0, padx=10,
                                                                                              pady=5)
        # Vlozeni tlacitka Pause
        playbtn = Button(buttonframe, text="PAUSE", command=self.pausesong, width=8, height=1,
                         font=("times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=1, padx=10,
                                                                                              pady=5)
        # Vlozeni tlacitka Unpause
        playbtn = Button(buttonframe, text="UNPAUSE", command=self.unpausesong, width=10, height=1,
                         font=("times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=2, padx=10,
                                                                                              pady=5)
        # Vlozeni tlacitka Stop
        playbtn = Button(buttonframe, text="STOP", command=self.stopsong, width=6, height=1,
                         font=("times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=3, padx=10,
                                                                                              pady=5)

        # Vytvoreni ramecku seznamu hudby
        songsframe = LabelFrame(self.root, text="Song Playlist", font=("times new roman", 15, "bold"), bg="grey",
                                fg="white", bd=5, relief=GROOVE)
        songsframe.place(x=600, y=0, width=400, height=200)
        # Vlozeni posuvniku tzv scrollbar
        scrol_y = Scrollbar(songsframe, orient=VERTICAL)
        # Vlozeni seznamu hudby
        self.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE,
                                font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)
        # Pouziti posuvniku na listbox
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Zmena adresare pro nacitani hudby
        os.chdir("C:/Users/Temirkhan Amanzhanov/Documents/MATLAB/UTB projects/Project_2")
        # Nacitani hudby
        songtracks = os.listdir()
        # Vkladani hudby do playlistu
        for track in songtracks:
            self.playlist.insert(END, track)

    # Definovani funkce Play hudby
    def playsong(self):
        # Zobrazeni vybraneho nazvu skladby
        self.track.set(self.playlist.get(ACTIVE))
        # Zobrazeni stavu
        self.status.set("Playing...")
        # Nacitani vybrane hudby
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Prehravani vybrane hudby
        pygame.mixer.music.play()


    def stopsong(self):
        # Zobrazeni stavu
        self.status.set("Stopped...")
        # Zastaveni hudby
        pygame.mixer.music.stop()

    def pausesong(self):
        # Zobrazeni stavu
        self.status.set("Paused...")
        # Pozastaveni hudby
        pygame.mixer.music.pause()

    def unpausesong(self):
        # Zobrazeni stavu
        self.status.set("Playing...")
        # Prehravani hudby
        pygame.mixer.music.unpause()


# Vytvoreni TK kontejneru
root = Tk()
# Absolvovani Root do klassu MusicPlayer
MusicPlayer(root)
# Smycka korenoveho okna
root.mainloop()