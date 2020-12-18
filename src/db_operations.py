import pickle


def save_database(artists_database, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(artists_database, f)


def load_database(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)
