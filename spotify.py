import spotipy
import config
from spotipy import SpotifyClientCredentials


def connect_to_spotify():
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(config.client_id, config.client_secret))


def get_artist_list(spotify):
    # todo get artist list from spotify idk how (use class Artist from artist.py)
    # it should be our "artist database" so len(artist_list) should be ~ 10^4, 10^5
    return []


def get_artist_tracks(spotify, artist):
    # todo return list of artist tracks - idk maybe all, maybe top 10, the newest (use class Track from track.py)
    return []


# an example:
# track_features = get_track_features(spotify, 'Prosto')
# track = Track(**track_features)
def get_track_features(spotify, name):
    track_id = spotify.search(q=name, type='track')['tracks']['items'][0]['id']
    return spotify.audio_features(tracks=track_id)[0]
