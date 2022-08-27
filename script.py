# importing the module
import sys

from pytube import YouTube

# link of the video to be downloaded
link = input("Please Enter your link:\n")

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error") # to handle exception
    sys.exit(0)

# filters out all the files with "mp4" extension
mp4files = yt.filter('mp4')

# to set the name of the file
yt.set_filename('GeeksforGeeks Video')

# get the video with the extension and
# resolution passed in the get() function
d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)
try:
    # downloading the video
    d_video.download()
except:
    print("Some Error!")
print('Task Completed!')