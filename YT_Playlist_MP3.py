import os, shutil, subprocess
from tqdm import tqdm
from pytube import Playlist, YouTube
from pytube.exceptions import AgeRestrictedError

def main(plist, destination_folder):
    links = plist.video_urls
    for link in tqdm(links, desc="Downloading"):
        try:

            ytube = YouTube(link)
            music = ytube.streams.filter(file_extension="mp4").first()
            #filename of the first video stream
            default_filename = music.default_filename
            
            # downloads first video stream and rename the first video stream
            music.download()
            default_filename_no_spaces = default_filename.replace(" ", "_").replace("(", "_").replace(")", "_").replace("&", "")
            try:
                # if its already renamed then pass
                os.rename(default_filename, default_filename_no_spaces)
            except:
                pass
                
            # replaces mp4 with mp3 for ffmeg output
            new_filename = default_filename_no_spaces.replace("mp4", "mp3")
            new_filename_no_spaces = new_filename.replace(" ", "")
            
            # converts mp4 video to mp3 audio, needs either ffmpeg exe in dir or in system PATH
            subprocess.call(f"ffmpeg -i {default_filename_no_spaces} {new_filename_no_spaces} -y", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # if exception then create download folder if not exists and store the downloaded audios
            # Move the converted audio file to the destination folder
            # Move the converted audio file to the destination folder
            new_audio_path = os.path.join(destination_folder, new_filename_no_spaces)
            shutil.move(new_filename_no_spaces, new_audio_path)

            # Create "Downloaded music" directory if it doesn't exist in the destination folder
            downloaded_music_dir = os.path.join(destination_folder, "Downloaded music")
            if not os.path.exists(downloaded_music_dir):
                os.makedirs(downloaded_music_dir)

            # Move the audio file to the "Downloaded music" directory
            shutil.move(new_audio_path, os.path.join(downloaded_music_dir, new_filename_no_spaces))

            # Remove the downloaded video file
            os.remove(default_filename_no_spaces)
        except AgeRestrictedError as e:
            print(f"Skipped age-restricted video: {link}")
            continue

                
    print("Download finished.")


if __name__ == "__main__":
    # Ask for the destination folder
    destination_folder = input("Enter the destination folder(skip for downloads folder): ")
    if destination_folder == "":
        # Get the user's home directory
        home_directory = os.path.expanduser("~")
        # Join the home directory with the "Downloads" folder
        destination_folder = os.path.join(home_directory, "Downloads")
    # Ask for the playlist URL
    playlist_url = input("Enter the playlist URL: ")
    print("Playlist URL:", playlist_url)
    print("Destination folder:", destination_folder)
    plist = Playlist(playlist_url)
    main(plist, destination_folder)
