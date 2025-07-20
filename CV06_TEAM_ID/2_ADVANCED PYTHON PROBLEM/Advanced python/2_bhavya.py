import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Replace these with your actual credentials from Spotify Developer Dashboard
CLIENT_ID = "f616fcacc1f24b6d81fed29544ca6ae1"
CLIENT_SECRET = "d651e480c46e4bd8851aaeecf95966b1"

# Set up client credentials manager
client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

# Create a Spotipy client
sp = spotipy.Spotify(auth_manager=client_credentials_manager)

# Function to search for a song
def search_song(query):
    try:
        results = sp.search(q=query, limit=5, type='track')
        tracks = results['tracks']['items']

        if not tracks:
            print("❌ No results found.")
            return
        print("\n🎧 Top 5 Search Results:\n")
        for i, track in enumerate(tracks, 1):
            name = track['name']
            artist = track['artists'][0]['name']
            album = track['album']['name']
            url = track['external_urls']['spotify']
            print(f"{i}. 🎵 {name}\n   👤 Artist: {artist}\n   💿 Album: {album}\n   🔗 Link: {url}\n")

    except spotipy.SpotifyException as e:
        print("Spotify error:", e)
    except Exception as e:
        print("Something went wrong:", e)

# Entry point
if __name__ == "__main__":
    query = input("🎵 Enter a song or artist name to search on Spotify: ")
    if query.strip():
        search_song(query)
    else:
        print("⚠ Please enter a valid search term.")