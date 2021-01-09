import pickle


def save_database(artists_database, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(artists_database, f)


def load_database(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)


def calc_avg_track_features(artists_dbs):
    for artists_db in artists_dbs:
        for artist in artists_db.values():
            if len(artist.tracks) > 0:
                artist.calc_avg_track_features()
