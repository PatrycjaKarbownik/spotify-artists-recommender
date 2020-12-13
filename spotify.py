from queue import Queue

import spotipy
import config
from artist import Artist
from track import Track
from spotipy import SpotifyClientCredentials

NUMBER_OF_TOP_TRACKS = 2
DATABASE_SIZE = 30


def connect_to_spotify():
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(config.client_id, config.client_secret))


def get_artists_id_list(spotify, seed):
    seed_id = spotify.search(q=seed, type='artist')['artists']['items'][0]['id']
    artists, artists_db, queue = dict(), list(), Queue()

    queue.put(seed_id)
    while queue.not_empty and len(artists) < DATABASE_SIZE:
        artist = queue.get()
        related_artists = spotify.artist_related_artists(artist)['artists']
        for artist in related_artists:
            if artist['id'] not in artists:
                artists[artist['id']] = artist['name']
                queue.put(artist['id'])

    for id in artists:
        artists_db.append(Artist(id, artists[id]))

    return artists_db


def get_artist_tracks(spotify, artist):
    track_ids, track_names = [], []

    for item in spotify.artist_top_tracks(artist.spotify_id)['tracks'][:NUMBER_OF_TOP_TRACKS]:
        track_ids.append(item['id'])
        track_names.append(item['name'])

    result = []
    for (name, features) in zip(track_names, spotify.audio_features(tracks=track_ids)):
        result.append(Track(name, **features))

    return result
