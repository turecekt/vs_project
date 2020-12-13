"""
Music Player.

Data:12/12/2020
"""
# Import pozadovanych modulu a knihoven
# Importing Required Modules & libraries
from tkinter import StringVar
from tkinter import GROOVE
from tkinter import LabelFrame
from tkinter import Label
from tkinter import Button
from tkinter import Scrollbar
from tkinter import VERTICAL
from tkinter import Listbox
from tkinter import SINGLE
from tkinter import RIGHT
from tkinter import Y
from tkinter import BOTH
from tkinter import END
from tkinter import ACTIVE
from tkinter import Tk
import pygame
import os


class MusicPlayer:
    """Zakladani classu MusicPlayer."""

    # Definovani Konstruktoru
    def __init__(self, root):
        """
        Zakladani objektu pro inicializace okna programu.

        Data:12/12/2020
        """
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
        trackframe = LabelFrame(self.root,
                                text="Song Track",
                                font=("times new roman", 15, "bold"),
                                bg="grey",
                                fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)
        # Vlozeni labelu hudby
        Label(trackframe, textvariable=self.track,
              width=20, font=("times new roman", 24, "bold"),
              bg="grey", fg="gold").grid(row=0, column=0, padx=10, pady=5)
        # Vlozeni labelu stavu
        Label(trackframe, textvariable=self.status,
              font=("times new roman", 24, "bold"), bg="grey",
              fg="gold").grid(row=0, column=1, padx=10, pady=5)

        # Vytvoreni ramecku tlacitek
        buttonframe = LabelFrame(self.root,
                                 text="Control Panel",
                                 font=("times new roman", 15, "bold"),
                                 bg="grey",
                                 fg="white", bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=100, width=600, height=100)
        # Vlozeni tlacitka Play
        Button(buttonframe,
               text="PLAY", command=self.playsong, width=6, height=1,
               font=("times new roman", 16, "bold"), fg="navyblue",
               bg="gold").grid(row=0, column=0, padx=10, pady=5)
        # Vlozeni tlacitka Pause
        Button(buttonframe, text="PAUSE",
               command=self.pausesong, width=8, height=1,
               font=("times new roman", 16, "bold"),
               fg="navyblue", bg="gold").grid(row=0, column=1, padx=10, pady=5)
        # Vlozeni tlacitka Unpause
        Button(buttonframe,
               text="UNPAUSE", command=self.unpausesong, width=10, height=1,
               font=("times new roman", 16, "bold"),
               fg="navyblue", bg="gold").grid(row=0, column=2, padx=10, pady=5)
        # Vlozeni tlacitka Stop
        Button(buttonframe,
               text="STOP", command=self.stopsong, width=6, height=1,
               font=("times new roman", 16, "bold"),
               fg="navyblue", bg="gold").grid(row=0, column=3, padx=10, pady=5)

        # Vytvoreni ramecku seznamu hudby
        songsframe = LabelFrame(self.root, text="Song Playlist",
                                font=("times new roman", 15, "bold"),
                                bg="grey",
                                fg="white", bd=5, relief=GROOVE)
        songsframe.place(x=600, y=0, width=400, height=200)
        # Vlozeni posuvniku tzv scrollbar
        scrol_y = Scrollbar(songsframe, orient=VERTICAL)
        # Vlozeni seznamu hudby
        self.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set,
                                selectbackground="gold", selectmode=SINGLE,
                                font=("times new roman", 12, "bold"),
                                bg="silver",
                                fg="navyblue", bd=5, relief=GROOVE)
        # Pouziti posuvniku na listbox
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Zmena adresare pro nacitani hudby
        os.chdir("C:/Songs")
        # Nacitani hudby
        songtracks = os.listdir()
        # Vkladani hudby do playlistu
        for track in songtracks:
            self.playlist.insert(END, track)

    # Definovani funkce Play hudby
    def playsong(self):
        """Zalozeni funkce playsong."""
        # Zobrazeni vybraneho nazvu skladby
        self.track.set(self.playlist.get(ACTIVE))
        # Zobrazeni stavu
        self.status.set("Playing...")
        # Nacitani vybrane hudby
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Prehravani vybrane hudby
        pygame.mixer.music.play()

    # Definovani funkce Stop hudby
    def stopsong(self):
        """Zalozeni funkce stopsong."""
        # Zobrazeni stavu
        self.status.set("Stopped...")
        # Zastaveni hudby
        pygame.mixer.music.stop()

    # Definovani funkce Pause hudby
    def pausesong(self):
        """Zalozeni funkce pausesong."""
        # Zobrazeni stavu
        self.status.set("Paused...")
        # Pozastaveni hudby
        pygame.mixer.music.pause()

    # Definovani funkce Unpause hudby
    def unpausesong(self):
        """Zalozeni funkce unpausesong."""
        # Zobrazeni stavu
        self.status.set("Playing...")
        # Prehravani hudby
        pygame.mixer.music.unpause()


if __name__ == "__main__":
    # Vytvoreni TK kontejneru
    root = Tk()
    # Absolvovani Root do klassu MusicPlayer
    MusicPlayer(root)
    # Smycka korenoveho okna
    root.mainloop()
