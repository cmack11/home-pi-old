#!/usr/bin/python
import requests
import time
import cred

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image
from io import BytesIO
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotifyAssetManager import SpotifyAssetManager

scope = "user-read-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username="22ej4dth6quu3mpgvum4e5yki",client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope, open_browser=False))

def get_current_track():
	playback = sp.current_playback(additional_types="episode")
	if playback == None:
#		print("No song playing")
		return { "id": "" }

	json_resp = playback;

	isEpisode = json_resp['item']['type'] == 'episode'

	track_id = json_resp['item']['id']
	track_name = json_resp['item']['name']
#	artists = [artist for artist in json_resp['item']['artists']]

#	link = json_resp['item']['external_urls']['spotify']

#	artist_names = ', '.join([artist['name'] for artist in artists])
	album_cover_art = ''
	if isEpisode:
		album_cover_art = json_resp['item']['images'][0]['url']
	else:
		album_cover_art = json_resp['item']['album']['images'][0]['url']

	current_track_info = {
		"id": track_id,
		"track_name": track_name,
#		"artists": artist_names,
#		"link": link,
		"album_cover_art": album_cover_art
	}

	return current_track_info



def main():
	current_track_id = None

	spManager = SpotifyAssetManager()
	# Configuration for the matrix
	options = RGBMatrixOptions()
	options.rows = 32
	options.cols = 64
	options.chain_length = 2
	options.parallel = 1
	options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
	options.gpio_slowdown = 1
	options.pixel_mapper_config = 'V-mapper:Z'

	matrix = RGBMatrix(options = options)

	i = Image.open('assets/spotify.png')
	fallback_dimensions = (matrix.width // 2, matrix.height // 2)
	i.thumbnail(fallback_dimensions, Image.ANTIALIAS)
	fallback_img = i.convert('RGB')
	pixel_list = list(fallback_img.getdata())
	fallback_grid = [[pixel_list[y*fallback_dimensions[1]+x] for y in range(fallback_dimensions[1])] for x in range(fallback_dimensions[0])]
	while False:
		for i in range(0, len(fallback_grid)):
			for j in range(0, len(fallback_grid[i])):
				c = fallback_grid[i][j]
				matrix.SetPixel(i,j,c[0], c[1], c[2])

	while True:
		if spManager.getTrackId() and spManger.getTrackId() != current_track_id:
			#pprint(
				#current_track_info,
				#indent=4,
			#)
			print('setting', spManager.getTrackId())
			current_track_id = spManager.getTrackId()
			img = spManager.getImage()
			if img == None:
				break;
			# Make image fit our screen.
			img.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)
			matrix.SetImage(img.convert('RGB'))
		#elif not current_track_info or not current_track_info['id']:
			#matrix.SetImage(fallback_img)
		time.sleep(1)


if __name__ == '__main__':
	main()
