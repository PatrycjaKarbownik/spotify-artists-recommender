from spotify import connect_to_spotify, get_artist_tracks, get_artist_list


def add_tracks(spotify, artists):
    for artist in artists:
        tracks = get_artist_tracks(spotify, artist)
        artist.set_tracks(tracks)
        artist.calc_avg_track_features()


def find_correlation(artists):
    # todo return list of track features which correlated between related artists (based on users history)
    return []


def predict_recommendations(artist_name, artists, features):
    # todo prediction should based on correlated features
    return []


if __name__ == '__main__':
    spotify = connect_to_spotify()

    artists = get_artist_list(spotify)
    add_tracks(spotify, artists)
    features = find_correlation(artists)

    for i in range(5):
        artist_name = input('Enter artist name: ')
        recommendations = predict_recommendations(artist_name, artists, features)
        for recomendation in recommendations:
            print(recomendation)
