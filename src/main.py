import os
from src.utils import load_database, save_database, calc_avg_track_features
from src.recommender import predict_recommendations
from src.similarities import get_relevant_features
from src.spotify import connect_to_spotify, get_artists_id_list, add_tracks, add_related_and_unrelated_artists

ARTISTS_DB_PATH_MAIN, ARTISTS_DB_PATH_SUPP = "artists_db/db_main", "artists_db/db_supp"

if __name__ == '__main__':
    spotify = connect_to_spotify()

    if os.path.exists(ARTISTS_DB_PATH_MAIN) and os.path.exists(ARTISTS_DB_PATH_SUPP):
        artists_database_main = load_database(ARTISTS_DB_PATH_MAIN)
        artists_database_supp = load_database(ARTISTS_DB_PATH_SUPP)
    else:
        artists_database_main = get_artists_id_list(spotify, seed="Kult")
        artists_database_supp = add_related_and_unrelated_artists(spotify, artists_database_main)

        add_tracks(spotify, [artists_database_main, artists_database_supp])
        calc_avg_track_features([artists_database_main, artists_database_supp])

        save_database(artists_database_main, ARTISTS_DB_PATH_MAIN)
        save_database(artists_database_supp, ARTISTS_DB_PATH_SUPP)

    relevant_features = get_relevant_features(artists_database_main, artists_database_supp)

    db_all_artists = dict(**artists_database_main, **artists_database_supp)

    while True:
        artist_name = input('Enter artist name (or press Enter to exit): ')
        if artist_name:
            recommendations = predict_recommendations(spotify, artist_name, db_all_artists, relevant_features)
            for recommendation in recommendations:
                print(recommendation)
        else:
            break
