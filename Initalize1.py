import string
from Socket1 import sendMessage

def joinRoom(s):
    readbuffer = ""
    bytebuffer = b''
    stringbuffer = ""
    Loading = True
    while Loading:
        bytebuffer = s.recv(1024)
        stringbuffer = bytebuffer.decode('utf-8')
        readbuffer = readbuffer + stringbuffer
        temp = str.split(readbuffer, "\n")
        readbuffer = temp.pop()

        for line in temp:
            print(line)
            Loading = loadingComplete(line)
    sendMessage(s, str.encode("Successfully joined chat gachiGASM"))

def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True