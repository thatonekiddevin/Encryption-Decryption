import socket
from Settings1 import HOST, PORT, ircPASS, ircIDENT, ircCHANNEL, CHANNEL

def openSocket():

    s = socket.socket()
    s.connect((HOST, PORT))
    s.send(ircPASS)
    s.send(ircIDENT)
    s.send(ircCHANNEL)
    return s

def sendMessage(s, message):
    messageTemp = ("PRIVMSG #" + CHANNEL + " :" + message.decode('utf-8'))
    s.send(str.encode(messageTemp) + str.encode("\r\n"))
    print("Sent: " + messageTemp)