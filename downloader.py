import os
from pytube import YouTube
from moviepy.editor import *
def downloadVideo(url):
    video = YouTube(url)
    video.streams.get_highest_resolution().download()
    print('download MP4 completed successfully')
def downloadAudio(url):
    audio = YouTube(url)
    out_file = audio.streams.get_audio_only().download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print('download MP3 completed successfully')
def chooseDownload(opc):
    if ((opc==2)or(opc=='mp4')or(opc=='2')or(opc=='Video')or(opc=='video')or(opc=='v')or(opc=='V')):
        downloadVideo(input('Paste the Url: '))
    if ((opc==1)or(opc=='mp3')or(opc=='1')or(opc=='Audio')or(opc=='audio')or(opc=='a')or(opc=='A')or(opc=='music')or(opc=='Music')):
        downloadAudio(input('Paste the Url: '))
def wannaStop(opc):
    return ((opc=='1')or(opc=='true')or(opc=='True')or('stop')or('s')or('y')or('S')or('Y'))
def cleanTerminal():
    os.system('cls')
if __name__=="__main__":
    stop = False
    while(stop==False):
        cleanTerminal()
        print('--------------------------------------------')
        print()
        print('              Youtube Downloader')
        print()
        print('choose the type of download')
        print()
        print('1, mp3, music, audio, a    to download mp4')
        print('2, mp4, video, v           to download mp4')
        print()
        print('-------------------------------------------')
        chooseDownload(input('download type: '))
        stop = wannaStop(input('Wanna Stop?'))
        if stop: cleanTerminal()
