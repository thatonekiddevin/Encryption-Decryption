import pygame as pg
import time
import os

def play_music(music_file, volume):

    freq = 44100
    bitsize = -16
    channels = 2
    buffer = 2048
    pg.mixer.init(freq, bitsize, channels, buffer)
    pg.mixer.music.set_volume(volume)
    clock = pg.time.Clock()

    pg.mixer.music.load(music_file)
    pg.mixer.music.play()
    while pg.mixer.music.get_busy():
        clock.tick(30)

music_file = "C:/Users/Devin/PycharmProjects/Fun/Milk.mp3"

volume = 0.4

play_music(music_file, volume)

os.remove(music_file)