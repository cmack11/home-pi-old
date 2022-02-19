#!/usr/bin/python
import random
import requests
import spotipy
import cred
import time
import threading

from spotipy.oauth2 import SpotifyOAuth
from PIL import Image
from io import BytesIO

scope = "user-read-playback-state"

class SpotifyAssetManager:
	def __init__(self):
		self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username="22ej4dth6quu3mpgvum4e5yki",client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope, open_browser=False))

		self.setSongDataLock = threading.Lock()
		self.setImageLock = threading.Lock()
		self.imagePath = ''
		self.trackId = None
		self.image = None

		# start new thread
		self.songPollingThread = threading.Thread(target=self.beginPollingForSong)
		self.songPollingThread.start()

	def beginPollingForSong(self):
		while True:
			info = self.sp.current_playback(additional_types="episode");
			if info == None:
				self.setSongData('', None)
				return
			isEpisode = info['item']['type'] == 'episode'
			track_id = info['item']['id']
			if isEpisode:
				album_cover_art = info['item']['images'][0]['url']
			else:
				album_cover_art = info['item']['album']['images'][0]['url']

			self.setSongData(album_cover_art, track_id)
			time.sleep(1)

	def imageRetrieval(self):
		return


	def setSongData(self, imagePath, trackId):
		if trackId == self.trackId:
			return
		self.setSongDataLock.acquire()
		self.imagePath = imagePath
		self.trackId = trackId
		response = requests.get(imagePath)
		img = Image.open(BytesIO(response.content))
		self.setImageLock.acquire()
		self.image = img
		self.setImageLock.release()
		self.setSongDataLock.release()

	def getImagePath(self):
		self.setSongDataLock.acquire()
		path = self.imagePath
		self.setSongDataLock.release()
		return path

	def getTrackId(self):
		self.setSongDataLock.acquire()
		id = self.trackId
		self.setSongDataLock.release()
		return id

	def getImage(self):
		self.setImageLock.acquire()
		img = self.image
		self.setImageLock.release()
		return img

def main():
	spManager = SpotifyAssetManager()
	track = None
	while True:
		if spManager.getTrackId() == track:
			continue
		track = spManager.getTrackId()
		print(spManager.getImagePath())

if __name__ == '__main__':
	main()
