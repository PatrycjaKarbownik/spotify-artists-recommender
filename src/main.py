import os
from random import random

from src.db_operations import load_database, save_database
from src.similarities import calculate_deviation_between_two_artists, get_relevant_features
from src.spotify import connect_to_spotify, get_artists_id_list, add_tracks, add_related_and_unrelated_artists

ARTISTS_DB_PATH = "artists_db/db"
REC_LIST_SIZE = 10
MAIN_LOOP = 5


def predict_recommendations(spotify, artist_name, artists_db, relevant_features):
    rec_artist_id = spotify.search(q=artist_name, type='artist')['artists']['items'][0]['id']
    if rec_artist_id in artists_db.keys():
        rec_artist = artists_db[rec_artist_id]
    else:
        # rec_artist = spotify ...
        # rec_artist = calc_artist_profile()
        pass

    artists_similarities, rec = [], []
    for artist in artists_db.values():
        if artist.spotify_id != rec_artist_id:
            deviation = calculate_deviation_between_two_artists(artist, rec_artist, relevant_features)
            artists_similarities.append((deviation, artist))

    artists_similarities.sort(key=lambda tup: tup[0])

    for artist in artists_similarities[:REC_LIST_SIZE]:
        rec.append(artist[1].name)

    return rec


if __name__ == '__main__':
    spotify = connect_to_spotify()

    if os.path.exists(ARTISTS_DB_PATH):
        artists_database = load_database(ARTISTS_DB_PATH)
    else:
        artists_database = get_artists_id_list(spotify, seed="Kult")
        add_tracks(spotify, artists_database)
        add_related_and_unrelated_artists(spotify, artists_database)
        save_database(artists_database, ARTISTS_DB_PATH)

    relevant_features = get_relevant_features(artists_database)

    for _ in range(MAIN_LOOP):
        print()
        artist_name = input('Enter artist name: ')
        recommendations = predict_recommendations(spotify, artist_name, artists_database, relevant_features)
        for recommendation in recommendations:
            print(recommendation)
