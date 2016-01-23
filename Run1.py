import string
from Read1 import getUser, getMessage
from Socket1 import openSocket, sendMessage
from Initalize1 import joinRoom
import sys
import random
import pygame as pg
import youtube_dl as ydl

giveawayBool = False
userArray = []
s = openSocket()
joinRoom(s)
readbuffer = ""
bytebuffer = b''
stringbuffer = ""
music_file = ""
volume = 0.4

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

while True:
    bytebuffer = s.recv(1024)
    stringbuffer = bytebuffer.decode('utf-8')
    readbuffer = readbuffer + stringbuffer
    temp = str.split(readbuffer, "\n")
    readbuffer = temp.pop()

    for line in temp:
        print(line)
        if "PING" in line:
            line = str.encode("PONG")
            s.send(line)
            break
        user = getUser(line)
        message = getMessage(line)
        print(user + " typed :" + message)
        if "You Suck" in message:
            sendMessage(s, str.encode("No, you suck!"))
            break
        if user == "nerfireliapls" and "!startgiveaway" in message:
            sendMessage(s, str.encode("Starting giveaway! Type !giveaway to enter!"))
            giveawayBool = True
            break
        if user not in userArray and giveawayBool == True and "!giveaway" in message:
            userArray.append(user)
            break
        if len(userArray) != 0 and user == "nerfireliapls" and "!endgiveaway" in message and giveawayBool == True:
            randomInt = random.randint(0, len(userArray) - 1)
            sendMessage(s, str.encode("Congratulations ") + userArray[randomInt] + str.encode(", you won the giveaway!"))
            giveawayBool = False
            userArray = []
            break
        if user == "nerfireliapls" and "!AllNight" in message:
            music_file = "C:/Users/Devin/PycharmProjects/Fun/AllNight.mp3"
            play_music(music_file, volume)
            break
        if "!milk" in message:
            music_file = "C:/Users/Devin/PycharmProjects/Fun/Milk.mp3"
            play_music(music_file, volume)
            break
        if "!bnd" in message:
            sendMessage(s, str.encode("I love it DEEP gachiGASM"))
        if user == "nerfireliapls" and "!sysquit" in message:
            sendMessage(s, str.encode("Leaving chat FeelsBadMan"))
            sys.exit()