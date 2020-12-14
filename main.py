from spotify import connect_to_spotify, get_artist_tracks, get_artists_id_list


def add_tracks(spotify, artists):
    for artist in artists:
        tracks = get_artist_tracks(spotify, artist)
        artist.set_tracks(tracks)
        artist.calc_avg_track_features()


def add_related_and_unrelated_artists(spotify, artists_db, artists_ids):
    for artist in artists_db:
        artist.search_related_artists(spotify, artists_ids)
        artist.search_unrelated_artists(artists_ids)


def find_correlation(artists):
    # todo return list of track features which correlated between related artists (based on users history)
    return []


def predict_recommendations(artist_name, artists, features):
    # todo prediction should based on correlated features
    return []


if __name__ == '__main__':
    spotify = connect_to_spotify()

    artists_database, artists_ids = get_artists_id_list(spotify, seed="Kult")
    add_tracks(spotify, artists_database)
    add_related_and_unrelated_artists(spotify, artists_database, artists_ids)
    # features = find_correlation(artists_database)

    # for i in range(5):
    #     artist_name = input('Enter artist name: ')
    #     recommendations = predict_recommendations(artist_name, artists, features)
    #     for recommendation in recommendations:
    #         print(recommendation)
