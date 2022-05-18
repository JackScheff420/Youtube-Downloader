##Maxcode##
import tkinter as tk
from pytube import YouTube

url = input("Your YouTube url: ")
video = YouTube(url)

print("*********************Video Title************************")
print(video.title)

print("********************Tumbnail Image***********************")
print(video.thumbnail_url)

print("********************Download video*************************")
#stream = video.streams.get_highest_resolution()
stream = video.streams.get_audio_only()


#Download video
stream.download()

root = tk.Tk()
root.title("YouTube Mp3/Mp4 downloader")
root.geometry('600x400+50+50')


root.mainloop()