from pytube import YouTube


link = input("Your link here: ")
yt = YouTube(link)

video = yt.streams.get_highest_resolution()
video.download()

print("DONE!!")
