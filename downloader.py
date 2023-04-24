import os
from tqdm import tqdm
from pytube import YouTube, Playlist, Search
from moviepy.editor import *

def downloadVideo(url):
    video = YouTube(url)
    video.streams.get_highest_resolution().download()
    print('download MP4 completed successfully')
def downloadAudio(url):
    audio = YouTube(url)
    out_file = audio.streams.get_audio_only().download()
    base = os.path.splitext(out_file)
    new_file = base[0] + '.mp3'
    print(base)
    print(new_file)
    os.rename(out_file, new_file)
    
    print('download MP3 completed successfully')
def chooseDownload(opc):
    if ((opc==2)or(opc=='mp4')or(opc=='2')or(opc=='Video')or(opc=='video')or(opc=='v')or(opc=='V')):
        downloadVideo(input('Paste the Url: '))
    elif ((opc==1)or(opc=='mp3')or(opc=='1')or(opc=='Audio')or(opc=='audio')or(opc=='a')or(opc=='A')or(opc=='music')or(opc=='Music')):
        downloadAudio(input('Paste the Url: '))
    elif(opc=='3'):
        downloadPlaylistMusic(input('Paste the Url: '))
    elif(opc=='3'):
        downloadPlaylistVideo(input('Paste the Url: '))    
def wannaStop(opc):
    return ((opc=='1')or(opc=='true')or(opc=='True')or('stop')or('s')or('y')or('S')or('Y'))
def cleanTerminal():
    os.system('clean')

def search():
    search = YouTube()

def downloadPlaylistVideo(url):
    print()
    playlist = Playlist(url)

    pbar = tqdm(playlist.videos)
    for video in pbar:
        pbar.set_description(f"Downloading {video.title}")
        video.streams.get_highest_resolution().download()
    print('download Playlist completed successfully')
def downloadPlaylistMusic(url):
    print()
    playlist = Playlist(url)
    pbar = tqdm(playlist.videos)
    for video in pbar:
        pbar.set_description(f"Downloading {video.title}")
        out_file = video.streams.get_audio_only().download()
        base = os.path.splitext(out_file)
        #print(base)
        #print(video)
        new_file = base[0] + '.mp3'
        os.rename(out_file, new_file)
    pbar.set_description('Download Completed!')
    print('download Playlist completed successfully')


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
        print('3    to download a playlist video')
        print('4    to download a playlist music')
        print()
        print('-------------------------------------------')
        chooseDownload(input('download type: '))

        stop = wannaStop(input('Wanna Stop?'))
        if stop: cleanTerminal()