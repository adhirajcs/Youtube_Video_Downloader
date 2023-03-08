# import the required package 
import sys
from pytube import YouTube

# Initialize max file size to 0
max_file_size = 0


# Define function for on download completion
def on_complete(stream, path):
    print("Video has been successfully downloaded")
    print()

# Define function for displaying download progress
def on_progress(stream, chunk, bytes_remaining):
    percent = int(100 - (100 * (bytes_remaining/max_file_size)))
    print(percent)

# Take user input for YouTube video link
link = input("Enter the YT video link: ")

# Create a YouTube object and register the on_progress_callback and on_complete_callback functions
yt = YouTube(link, on_progress_callback = on_progress, on_complete_callback=on_complete)

# Print the title of the video
print("Title:" , yt.title)

# Take user input for preferred resolution
choice = input("Enter the Resolution: \n1080, \n720, \n480, \n360: ")
res = choice + "p"

# Print the resolution of the downloaded video
print("The video will be downloaded in " + res + " resolution.")

try:
    # Get the stream with the specified resolution
    video = yt.streams.get_by_resolution(res)

except:
    # Error message if stream with specified resolution is not available
    print("Something went Wrong!!!\nPlease close the window and try Again :)")
    print()

# Set the max file size to the size of the video
max_file_size = video.filesize

# Download the video to the specified location
video.download(".\downloads")

# Prompt the user to close the window
close = input("Enter y to close the window: ")
if close == "y":
    sys.exit()