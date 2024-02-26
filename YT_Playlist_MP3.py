import os, shutil, subprocess
from tqdm import tqdm
from pytube import Playlist, YouTube

def main():
    # Ask for the playlist URL
    playlist_url = input("Enter the playlist URL: ")

    # Ask for the destination folder
    destination_folder = input("Enter the destination folder(skip for downloads folder): ")
    if destination_folder == "":
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Join the home directory with the "Downloads" folder
        destination_folder = os.path.join(home_directory, "Downloads")

    # Now you can use playlist_url and destination_folder in your code
    # For example, you can use them with pytube to download the playlist videos
    # Below is just a placeholder for the rest of your code

    print("Playlist URL:", playlist_url)
    print("Destination folder:", destination_folder)



if __name__ == "__main__":
    main()
