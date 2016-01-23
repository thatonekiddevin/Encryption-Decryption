import youtube_dl
i = "https://www.youtube.com/watch?v=6dqsX81OUxU"
ytID = 5

options = {
    'format': 'bestaudio/best', # choice of quality
    'extractaudio' : True,      # only keep the audio
    'audioformat' : "mp3",      # convert to mp3
    'outtmpl': '%(id)s',        # name the file the ID of the video
    'noplaylist' : True,        # only download single song, not playlist
}
try:
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=6dqsX81OUxU'])
except:
    print("You entered a invalid youtube URL, please try again")