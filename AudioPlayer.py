from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from pathlib import Path
import os
import pygame

root = Tk()

# Název programu
root.title('Audio Player')

# Nastavení ikonky pro aplikace
root.iconbitmap('C:/Users/Temirkhan Amanzhanov/Downloads/playbutton.ico')

# Nastavení rozměrů hlavního okna programu
root.geometry('600x400')

# Inicializace knihovny pygame
pygame.init()
pygame.mixer.init()

audio_file_name = []
audioName = []


# Funkce přidání písni
def add_song():
    global audio_file_name, audioName
    # Zachování do proměnné celé cesty do písničky
    audio_file_name = filedialog.askopenfilename(filetypes=(("Audio Files", ".mp3 .wav .ogg"), ("All Files", "*.*")))
    # Změna pro zobrázení pouze nazvu písni
    audioName = Path(audio_file_name).stem
    # Přídání do listboxu nazev písni
    song_box.insert(END, audioName)


# add many songs to playlist
def add_many_songs():
    global audio_file_name, audioName

    audio_file_names = filedialog.askopenfilenames(filetypes=(("Audio Files", ".mp3 .wav .ogg"), ("All Files", "*.*")))

    for audio_file_name in audio_file_names:
        audioName = Path(audio_file_name).stem
        song_box.insert(END, audioName)


# Přehravání vybráné písničky
def play():
    global audio_file_name
    FileName = os.path.realpath(audio_file_name)

    pygame.mixer.music.load(FileName)
    pygame.mixer.music.play(loops=0)



def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)


# create Global pause variable
global paused
paused = False


# pause and unpause songs:
def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


# Vytvoření listboxu pro zobrazení seznamu písniček
song_box = Listbox(root, bg='black', fg='yellow', width=70, height=20, font='Azonix 8', selectbackground='white',
                   selectforeground='black')
song_box.pack(pady=20)

# Změna rozměru obrázků pro tlačitka
b_img = Image.open('C:/Users/Temirkhan Amanzhanov/Documents/MATLAB/UTB projects/Project_2/previoussongbutton.png')
b_img = b_img.resize((50, 50), Image.ANTIALIAS)
back_img = ImageTk.PhotoImage(b_img)

f_img = Image.open('C:/Users/Temirkhan Amanzhanov/Documents/MATLAB/UTB projects/Project_2/nextsongbutton.png')
f_img = f_img.resize((50, 50), Image.ANTIALIAS)
forward_img = ImageTk.PhotoImage(f_img)

p_img = Image.open('C:/Users/Temirkhan Amanzhanov/Documents/MATLAB/UTB projects/Project_2/playbutton.png')
p_img = p_img.resize((70, 70), Image.ANTIALIAS)
play_img = ImageTk.PhotoImage(p_img)

pe_img = Image.open('C:/Users/Temirkhan Amanzhanov/Documents/MATLAB/UTB projects/Project_2/pausebutton.png')
pe_img = pe_img.resize((50, 50), Image.ANTIALIAS)
pause_img = ImageTk.PhotoImage(pe_img)

s_img = Image.open('C:/Users/Temirkhan Amanzhanov/Documents/MATLAB/UTB projects/Project_2/stopbutton.png')
s_img = s_img.resize((50, 50), Image.ANTIALIAS)
stop_img = ImageTk.PhotoImage(s_img)

# Vytvoření framu pro nastavení polohy tlačitek
controls_frame = Frame(root)
controls_frame.pack()

# Vytvoření tlačitek pro ovladání audioplayeru
back_button = Button(controls_frame, image=back_img, borderwidth=0)
forward_button = Button(controls_frame, image=forward_img, borderwidth=0)
play_button = Button(controls_frame, image=play_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_img, borderwidth=0, command=stop)

back_button.grid(row=0, column=0, padx=15)
forward_button.grid(row=0, column=1, padx=15)
play_button.grid(row=0, column=2, padx=15)
pause_button.grid(row=0, column=3, padx=15)
stop_button.grid(row=0, column=4, padx=15)

# Vytvoření položky "Menu"
upper_menu = Menu(root)
root.config(menu=upper_menu)

# Vytvožení "přidat písní" menu
add_song_menu = Menu(upper_menu)
upper_menu.add_cascade(label='Přidat písní', menu=add_song_menu)
add_song_menu.add_command(label='Přidat píseň do playlistu', command=add_song)

# add many songs to playlist
add_song_menu.add_command(label='Přidat písní do playlistu', command=add_many_songs)

# Uzavření cyklu programu
root.mainloop()
