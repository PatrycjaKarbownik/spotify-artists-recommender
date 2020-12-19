from queue import Queue

import spotipy
from spotipy import SpotifyClientCredentials

import config
from src.artist import Artist
from src.track import Track

NUMBER_OF_TOP_TRACKS = 2
DATABASE_SIZE = 30


def connect_to_spotify():
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(config.client_id, config.client_secret))


def get_artists_id_list(spotify, seed):
    seed_id = spotify.search(q=seed, type='artist')['artists']['items'][0]['id']
    artists_db, queue = dict(), Queue()

    queue.put(seed_id)
    while queue.not_empty and len(artists_db) < DATABASE_SIZE:
        artist = queue.get()
        related_artists = spotify.artist_related_artists(artist)['artists']
        for artist in related_artists:
            if artist['id'] not in artists_db:
                artists_db[artist['id']] = Artist(artist['id'], artist['name'])
                queue.put(artist['id'])

    return artists_db


def get_artist_tracks(spotify, artist):
    track_ids, track_names, result = [], [], []

    for item in spotify.artist_top_tracks(artist.spotify_id)['tracks'][:NUMBER_OF_TOP_TRACKS]:
        track_ids.append(item['id'])
        track_names.append(item['name'])

    for (name, features) in zip(track_names, spotify.audio_features(tracks=track_ids)):
        result.append(Track(name, **features))

    return result


def add_tracks(spotify, artists_db):
    for artist in artists_db.values():
        tracks = get_artist_tracks(spotify, artist)
        artist.set_tracks(tracks)
        artist.calc_avg_track_features()


def add_related_and_unrelated_artists(spotify, artists_db):
    for artist in artists_db.values():
        artist.search_related_artists(spotify, artists_db.keys())
        artist.search_unrelated_artists(artists_db.keys())
