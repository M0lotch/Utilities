from pytag import AudioReader, FormatNotSupportedError
import os, sys
import shutil


current_directory = os.listdir(".")

def check_path(artist, album):
	return os.path.exists(str(artist) + "/" + str(album))
	
def move_song(song, artist, album, title):
	if check_path(artist, album) == False:
		os.makedirs(str(artist) + "/" + str(album))
	shutil.move(str(song), str(artist) + "/" + str(album) + "/" + str(title))


def main():
	print("Organizing...")

	for song in current_directory:
		filename = song

		try:
			if filename.endswith(".mp3"):
				audio = AudioReader(song)
				check_path(audio.artist, audio.album)
				move_song(filename, audio.artist, audio.album, audio.title)
		except FormatNotSupportedError:
			print(filename + "Skipped, must be organized manually!")

	print("Oranizing complete. Hopefully it's not all fucky!")


main()