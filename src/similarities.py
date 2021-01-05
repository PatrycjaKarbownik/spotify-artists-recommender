from src.track import Features

FEATURES_THRESHOLD = -0.2
ARTISTS_THRESHOLD = 0.7


def get_relevant_features(artists_db_main, artists_db_supp):
    features_relevance = Features()

    for artist in artists_db_main.values():
        related_artists = []
        for spotify_id in artist.related_artists:
            if spotify_id in artists_db_main:
                related_artists.append(artists_db_main[spotify_id])
            elif spotify_id in artists_db_supp:
                related_artists.append(artists_db_supp[spotify_id])
            else:
                print('Houston, we have a problem!')

        unrelated_artists = [artists_db_main[spotify_id] for spotify_id in artist.unrelated_artists]
        related_artists_features = calculate_features_deviations(artist, related_artists)
        unrelated_artists_features = calculate_features_deviations(artist, unrelated_artists)

        for feature_name in Features.get_features_list():
            related_artists_deviation = getattr(related_artists_features, feature_name)
            unrelated_artists_deviation = getattr(unrelated_artists_features, feature_name)
            if related_artists_deviation - unrelated_artists_deviation < FEATURES_THRESHOLD:
                features_relevance.increment(feature_name)

    result = []
    for feature_name in Features.get_features_list():
        relevance = getattr(features_relevance, feature_name)
        if relevance > ARTISTS_THRESHOLD:
            result.append((feature_name, relevance))

    return result


def calculate_features_deviations(artist, other_artists):
    artists_features_averages = [artist.avg_track_features for artist in other_artists]
    features_deviations = {}

    for feature_name in Features.get_features_list():
        main_artist_feature_avg = getattr(artist.avg_track_features, feature_name)
        feature_averages = [getattr(features_averages, feature_name) for features_averages in artists_features_averages]
        deviation_list = [calculate_deviation(main_artist_feature_avg, value) for value in feature_averages]
        features_deviations[feature_name] = sum(deviation_list)

    return Features(**features_deviations)


def calculate_deviation_between_two_artists(artist_1, artist_2, features):
    deviation_sum = 0

    for feature in features:
        artist_1_feat_value = getattr(artist_1.avg_track_features, feature[0])
        artist_2_feat_value = getattr(artist_2.avg_track_features, feature[0])
        deviation_sum += feature[1] * calculate_deviation(artist_1_feat_value, artist_2_feat_value)

    return deviation_sum


def calculate_deviation(value_1, value_2):
    return (value_1 - value_2) ** 2
