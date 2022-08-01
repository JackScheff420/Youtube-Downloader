##Maxcode##
from functools import update_wrapper
from multiprocessing.connection import wait
import tkinter as tk
from turtle import down
from pytube import YouTube
from pytube import Playlist
import os


#hallo
#penis



# wenn der link 'playlist' im namen hat soll automatisch die playlist runtergeladen werden mit der playlist funktion

cwd = os.getcwd()



def download(video, file_ext):
    mp4_list = []

    print(f'Downloading: {video.title}')

    print("*********************Video Title************************")
    print(video.title)

    if file_ext.lower() == 'mp3':
            st = video.streams.get_audio_only()
            
            
    elif file_ext.lower() == 'mp4':
        st = video.streams.get_highest_resolution()

    else:
        exit()

    st.download()

    if file_ext.lower() == 'mp3':
        mp4_file = os.path.join(cwd, video.title + ".mp4")
        mp3_file = os.path.join(cwd, video.title + ".mp3")
        os.rename(mp4_file, mp3_file)



def download_one(link, file_ext):
    video = YouTube(link)

    print(f'Downloading: {video.title}')

    print("*********************Video Title************************")
    print(video.title)


    if file_ext.lower() == 'mp3':
            st = video.streams.get_audio_only()
            
            
    elif file_ext.lower() == 'mp4':
        st = video.streams.get_highest_resolution()

    else:
        exit()

    st.download()

    if file_ext.lower() == 'mp3':
        mp4_file = os.path.join(cwd, video.title + ".mp4")
        mp3_file = os.path.join(cwd, video.title + ".mp3")
        os.rename(mp4_file, mp3_file)


def download_plist(link, file_ext):
    purl = Playlist(link)

    print(f'Downloading: {link.title}')
    
    # mp4_list = []
    
    for video in purl.videos:
        print("*********************Video Title************************")
        print(video.title)
        
        if file_ext.lower() == 'mp3':
            st = video.streams.get_audio_only()
            
            
        elif file_ext.lower() == 'mp4':
            st = video.streams.get_highest_resolution()

        else:
            exit()

        st.download()

        

        if file_ext.lower() == 'mp3':
            mp4_file = os.path.join(cwd, video.title + ".mp4")
            mp4_list.append(mp4_file)

    for mp4_file in mp4_list:
        mp3_file = mp4_file + ".mp3"
        os.rename(mp4_file, mp3_file)
        #os.rename gibt fehlermeldung (kann datei nicht finden)




#00000000000000000000000000000000000000000


eingabe_playlist_or_one = input("möchtest du nur ein Video oder eine Playlist runterladen? (V/P) ... ")
eingabe_dateiformat = input("möchtest du mp3 oder mp4? ... ")

if eingabe_playlist_or_one.upper() == 'V':

    download_one(input("Your YouTube url: "), eingabe_dateiformat)

elif eingabe_playlist_or_one.upper() == 'P':
    
    download_plist(input("Your YouTube url: "), eingabe_dateiformat)








# root = tk.Tk()
# root.title("YouTube Mp3/Mp4 downloader")
# root.geometry('600x400+50+50')


# root.mainloop()