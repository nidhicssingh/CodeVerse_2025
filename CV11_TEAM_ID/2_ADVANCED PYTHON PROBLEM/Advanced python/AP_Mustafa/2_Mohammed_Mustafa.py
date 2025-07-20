import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#Spotify developer account: https;//developer.spotify.com
#gota dashboard create app
#Redirect URIs*(https://localhost:8888/callback)
#Replace these with your own credentials
CLIENT_ID = "d99decff523f4467b507f3a2ba568fae"
CLIENT_SECRET = "69ea7f04fcaf46e8983082733d3eaf28"

# Auth Manager
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def search_song(query):
    results = sp.search(q=query, limit=5, type='track')
    tracks = results['tracks']['items']

    if not tracks:
        print("❌ No results found.")
        return

    print("\n🎧 Top Results:")
    for i, track in enumerate(tracks):
        name = track['name']
        artist = track['artists'][0]['name']
        album = track['album']['name']
        url = track['external_urls']['spotify']
        print(f"{i+1}. {name} by {artist} | Album: {album}\n   🔗 {url}")

# Example usage
query = input("🎵 Enter a song or artist name to search on Spotify: ")
search_song(query)
