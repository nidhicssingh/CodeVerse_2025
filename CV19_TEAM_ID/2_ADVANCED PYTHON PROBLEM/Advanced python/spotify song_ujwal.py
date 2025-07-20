import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Enable UTF-8 encoding (for Windows consoles)
sys.stdout.reconfigure(encoding='utf-8')

# Replace with your actual credentials from Spotify Developer Dashboard
CLIENT_ID = "b2438d81452d42628fe9a5df2d56b663"
CLIENT_SECRET = "005c1b8afa154e0aa684d9da3596b6ac"

# Auth Manager
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def search_song(query):
    try:
        results = sp.search(q=query, limit=5, type='track')
        tracks = results['tracks']['items']

        if not tracks:
            print("No results found.")
            return

        print("\nTop Results:")
        for i, track in enumerate(tracks):
            name = track['name']
            artist = track['artists'][0]['name']
            album = track['album']['name']
            url = track['external_urls']['spotify']
            print(f"{i+1}. {name} by {artist} | Album: {album}")
            print(f"   Link: {url}")
    except Exception as e:
        print(f"Error occurred: {e}")

# Example usage
query = input("Enter a song or artist name to search on Spotify: ")
search_song(query)