from bs4 import BeautifulSoup
import requests     
import spotipy
from spotipy.oauth2 import SpotifyOAuth
scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
#music_date = input("Enter a date in YYYY-MM-DD format to see the top songs from that day: ")
music_date = "2003-08-26"
headers = {"USER-AGENT":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
response = requests.get(f"https://www.billboard.com/charts/hot-100/{music_date}/",headers=headers)
page = response.text
soup = BeautifulSoup(page, 'html.parser')

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(response.status_code)
print(song_names)
