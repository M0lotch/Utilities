from pytag import AudioReader, FormatNotSupportedError
import os, sys
import shutil


current_directory = os.listdir(".")

def check_path(artist, album):
	if os.path.exists(str(artist) + "/" + str(album)) == True:
		return True
	else:
		return False

def move_song(song, artist, album, title):
	if os.path.exists(str(artist) + "/" + str(album)) == True:
		shutil.move(str(song), str(artist) + "/" + str(album) + "/" + str(title))
	else:
		os.makedirs(str(artist) + "/" + str(album))


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