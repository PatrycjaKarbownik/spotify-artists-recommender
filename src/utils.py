import pickle


def save_databases(artists_databases, files_paths):
    for db_no in range(len(artists_databases)):
        with open(files_paths[db_no], 'wb') as f:
            pickle.dump(artists_databases[db_no], f)


def load_database(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)
