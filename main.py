from pytube import YouTube
instructiunii = ()

link = input("Your link here: ")
yt = YouTube(link)

video = yt.streams.get_highest_resolution()
video.download()

print("DONE!!")
