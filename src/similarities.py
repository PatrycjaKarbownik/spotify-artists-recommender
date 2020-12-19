from math import sqrt
from random import shuffle

FEATURES_THRESHOLD = -0.2
ARTISTS_THRESHOLD = 0.7


def analyse_features(artist_id, other_artists, artists_db):
    pass  # todo
    # return [feature_1_val, feature_2_val, feature3_val, ...]


def analyse_artists(artists_db):
    related_artists_features, unrelated_artists_features = [], []
    artists_ids = list(artists_db.keys())
    shuffle(artists_ids)

    for artist_id in artists_ids[:int(sqrt(len(artists_db)))]:
        artist = artists_db[artist_id]
        related_artists_features.append(analyse_features(artist, artist.related_artists, artists_db))
        unrelated_artists_features.append(analyse_features(artist, artist.unrelated_artists, artists_db))

    # for i in len(related_artists_features):
    #     for j in len(related_artists_features[i]):
    #         if related_artists_features[i][j] - unrelated_artists_features[i][j] < FEATURES_THRESHOLD:
    #             pass

    # for feature in features:
    #     if ... > len(artists_db) * ARTISTS_THRESHOLD:
    #         pass

    return []


def calc_sim(artist_1, artist_2, features):
    pass
