from spotify import connect_to_spotify, get_artist_tracks, get_artists_id_list


def analyse_features(artist_id, other_artists, artists_db):
    pass  # todo


def add_tracks(spotify, artists_db):
    for artist in artists_db.values():
        tracks = get_artist_tracks(spotify, artist)
        artist.set_tracks(tracks)
        artist.calc_avg_track_features()


def add_related_and_unrelated_artists(spotify, artists_db):
    for artist in artists_db.values():
        artist.search_related_artists(spotify, artists_db.keys())
        artist.search_unrelated_artists(artists_db.keys())


def find_correlation(artists_db):
    related_artists_features, unrelated_artists_features = [], []
    for artist in artists_db.values():
        related_artists_features.append(analyse_features(artist, artist.related_artists, artists_db))
        unrelated_artists_features.append(analyse_features(artist, artist.unrelated_artists, artists_db))
    # todo continue here
    return []


def predict_recommendations(artist_name, artists, features):
    # todo prediction should based on correlated features
    return []


if __name__ == '__main__':
    spotify = connect_to_spotify()

    artists_database = get_artists_id_list(spotify, seed="Kult")
    add_tracks(spotify, artists_database)
    add_related_and_unrelated_artists(spotify, artists_database)
    features = find_correlation(artists_database)

    # for i in range(5):
    #     artist_name = input('Enter artist name: ')
    #     recommendations = predict_recommendations(artist_name, artists, features)
    #     for recommendation in recommendations:
    #         print(recommendation)
