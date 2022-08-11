import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()  # Create application window
musicplayer.title("Music Player")  # Set title to application window
musicplayer.geometry('450x350')

directory = askdirectory()
os.chdir(directory)
songList = os.listdir()
playlist = tkr.Listbox(musicplayer, font="Helvetica 12 bold", bg="#cdd4d3", selectmode=tkr.SINGLE)

for item in songList:
    pos = 0
    playlist.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def exit_music_player():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


Button1 = tkr.Button(musicplayer, font="Helvetica 12 bold", bg="#c2ad8b", text="PLAY", width=5, height=3, command=play)
Button2 = tkr.Button(musicplayer, font="Helvetica 12 bold", bg="#b38395", text="STOP", width=5, height=3, command=exit_music_player)
Button3 = tkr.Button(musicplayer, font="Helvetica 12 bold", bg="#758493", text="PAUSE", width=5, height=3, command=pause)
Button4 = tkr.Button(musicplayer, font="Helvetica 12 bold", bg="#b47d54", text="UNPAUSE", width=5, height=3, command=unpause)


var = tkr.StringVar()
songTitle = tkr.Label(musicplayer, font="Helvetica 12 bold", textvariable=var)

songTitle.pack()
Button1.pack(fill='x')
Button2.pack(fill='x')
Button3.pack(fill='x')
Button4.pack(fill='x')
playlist.pack(fill='x', expand='yes')

musicplayer.mainloop()