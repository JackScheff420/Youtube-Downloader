##Maxcode##
import tkinter as tk
from turtle import down
from pytube import YouTube
from pytube import Playlist
import os






def download_plist(p):
    purl = Playlist(p)

    print(f'Downloading: {p.title}')

    for video in purl.videos:
        print(video.title)
        st = video.streams.get_highest_resolution()
        st.download()




download_plist(input("Your YouTube url: "))

# video = YouTube(url)

# print("*********************Video Title************************")
# print(video.title)

# print("********************Tumbnail Image***********************")
# print(video.thumbnail_url)



# eingabe = input("mp3 oder mp4? ")
# if eingabe == 'mp3':

#     stream = video.streams.get_audio_only()
#     stream.download()

#     mp4_file = os.path.join("H:\Eigene Dateien\Arbeit\Programmieren\Python\Youtube-Downloader", video.title + ".mp4")
#     mp3_file = os.path.join("H:\Eigene Dateien\Arbeit\Programmieren\Python\Youtube-Downloader", video.title + ".mp3")
#     os.rename(mp4_file, mp3_file)

# elif eingabe == 'mp4':
#     stream = video.streams.get_highest_resolution()
#     stream.download()

# else:
#     exit()








# root = tk.Tk()
# root.title("YouTube Mp3/Mp4 downloader")
# root.geometry('600x400+50+50')


# root.mainloop()