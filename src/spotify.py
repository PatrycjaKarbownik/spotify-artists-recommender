from datetime import datetime
from queue import Queue

import spotipy
from spotipy import SpotifyClientCredentials

import config
from artist import Artist
from track import Track

NUMBER_OF_TOP_TRACKS = 10
DATABASE_SIZE = 60


def connect_to_spotify():
    return spotipy.Spotify(auth_manager=SpotifyClientCredentials(config.client_id, config.client_secret))


def get_artists_id_list(spotify, seed):
    print('Preparing database ' + str(datetime.now()))
    seed_artist = spotify.search(q=seed, type='artist')['artists']['items'][0]
    artists_db, queue = dict(), Queue()
    artists_db[seed_artist['id']] = Artist(seed_artist['id'], seed_artist['name'], seed_artist['genres'])

    queue.put(seed_artist['id'])
    while queue.not_empty and len(artists_db) < DATABASE_SIZE:
        artist = queue.get()
        related_artists = spotify.artist_related_artists(artist)['artists']
        for artist in related_artists:
            if artist['id'] not in artists_db:
                artists_db[artist['id']] = Artist(artist['id'], artist['name'], artist['genres'])
                queue.put(artist['id'])

    return artists_db


def get_artist_tracks(spotify, artist):
    track_ids, track_names, result = [], [], []

    for item in spotify.artist_top_tracks(artist.spotify_id)['tracks'][:NUMBER_OF_TOP_TRACKS]:
        track_ids.append(item['id'])
        track_names.append(item['name'])

    for (name, features) in zip(track_names, spotify.audio_features(tracks=track_ids)):
        if features is None:
            continue
        result.append(Track(name, **features))

    return result


def add_tracks(spotify, artists_databases):
    print('Add tracks ' + str(datetime.now()))
    for artist_db in artists_databases:
        for artist in artist_db.values():
            tracks = get_artist_tracks(spotify, artist)
            artist.set_tracks(tracks)


def add_related_and_unrelated_artists(spotify, artists_db_main):
    print('Related & unrelated artists ' + str(datetime.now()))
    artists_db_supp = dict()
    for artist in artists_db_main.values():
        artist.search_related_artists(spotify, artists_db_main.keys(), artists_db_supp)
        artist.search_unrelated_artists(artists_db_main.keys())

    return artists_db_supp


def prepare_artist_profile(spotify, artist_id, artist_name):
    artist = Artist(artist_id, artist_name)
    artist.set_tracks(get_artist_tracks(spotify, artist))
    artist.calc_avg_track_features()

    return artist
