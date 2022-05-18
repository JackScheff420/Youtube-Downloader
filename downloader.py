from pytube import YouTube

url = 'https://www.youtube.com/watch?v=2MFO66voVm0'
my_video = YouTube(url)

print("####################### Video Title ############################")
print (my_video.title)

print("####################### Thumbnail ############################")
print (my_video.thumbnail_url)

my_video = my_video.streams.get_audio_only()

# my_video = my_video.streams.get_highest_resolution()
# mp4 option

my_video.download()