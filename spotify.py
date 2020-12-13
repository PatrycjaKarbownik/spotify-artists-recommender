import spotipy
import config
from artist import Artist
from track import Track
from spotipy import SpotifyClientCredentials

NUMBER_OF_TOP_TRACKS = 2


def connect_to_spotify():
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(config.client_id, config.client_secret))


def get_artist_list(spotify):
    # todo get artist list from spotify idk how (use class Artist from artist.py)
    # it should be our "artist database" so len(artist_list) should be ~ 10^4, 10^5
    return []


def get_artist_tracks(spotify, artist):
    track_ids, track_names = [], []

    for item in spotify.artist_top_tracks(artist.spotify_id)['tracks'][:NUMBER_OF_TOP_TRACKS]:
        track_ids.append(item['id'])
        track_names.append(item['name'])


    result = []
    for (name, features) in zip(track_names, spotify.audio_features(tracks=track_ids)):
        result.append(Track(name, **features))

    return result
