from bs4 import BeautifulSoup
import requests, spotipy
from spotipy.oauth2 import SpotifyOAuth

question = input("Which year do you want to travel to? Type the date in this form YYYY-MM-DD:")

print(question)

URL = f"https://www.billboard.com/charts/hot-100/{question}"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id="",
        client_secret="",
        show_dialog=True,
        cache_path="token.txt",
        username="buitendam11", 
    )
)
user_id = sp.current_user()["id"]