from math import sqrt
from random import shuffle
from track import Features

FEATURES_THRESHOLD = -0.2
ARTISTS_THRESHOLD = 0.7


def get_relevant_features(artists_db):
    features_relevance = Features()
    artists_ids = list(artists_db.keys())
    shuffle(artists_ids)

    for artist_id in artists_ids[:int(sqrt(len(artists_db)))]:
        artist = artists_db[artist_id]
        related_artists = [artists_db[spotify_id] for spotify_id in artist.related_artists]
        unrelated_artists = [artists_db[spotify_id] for spotify_id in artist.unrelated_artists]

        related_artists_features = calculate_features_deviations(artist, related_artists)
        unrelated_artists_features = calculate_features_deviations(artist, unrelated_artists)

        for feature_name in Features.get_features_list():
            related_artists_deviation = getattr(related_artists_features, feature_name)
            unrelated_artists_deviation = getattr(unrelated_artists_features, feature_name)
            if related_artists_deviation - unrelated_artists_deviation < FEATURES_THRESHOLD:
                features_relevance.increment(feature_name)

    result = []
    for feature_name in Features.get_features_list():
        if getattr(features_relevance, feature_name) > len(artists_db) * ARTISTS_THRESHOLD:
            result.append(feature_name)

    return result


def calculate_features_deviations(artist, other_artists):
    artists_features_averages = [artist.avg_track_features for artist in other_artists]
    dictionary = {}
    for feature_name in Features.get_features_list():
        main_artist_feature_avg = getattr(artist.avg_track_features, feature_name)
        feature_averages = [getattr(features_averages, feature_name) for features_averages in artists_features_averages]
        deviation_list = [calculate_deviation(main_artist_feature_avg, value) for value in feature_averages]
        dictionary[feature_name] = sum(deviation_list)

    return Features(**dictionary)


def calculate_deviation(minuend, subtrahend):
    return (minuend - subtrahend) ** 2


def calc_sim(artist_1, artist_2, features):
    pass
