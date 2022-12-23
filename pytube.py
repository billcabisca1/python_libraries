from  pytube import YouTube

def Download(link):
    youtube_video = YouTube(link)
    youtube_video = youtube_video.streams.get_highest_resolution();
    youtube_video.download()
    print("YouTube video has been downloaded")


link = input("enter the video link you want to install: ")
Download(link)
