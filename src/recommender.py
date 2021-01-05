from src.similarities import calculate_deviation_between_two_artists
from src.spotify import prepare_artist_profile

REC_LIST_SIZE = 10


def predict_recommendations(spotify, artist_name, artists_db, relevant_features):
    rec_artist_id = spotify.search(q=artist_name, type='artist')['artists']['items'][0]['id']
    if rec_artist_id in artists_db.keys():
        rec_artist = artists_db[rec_artist_id]
    else:
        rec_artist = prepare_artist_profile(spotify, rec_artist_id, artist_name)

    artists_similarities, rec = [], []
    for artist in artists_db.values():
        if artist.spotify_id != rec_artist_id:
            deviation = calculate_deviation_between_two_artists(artist, rec_artist, relevant_features)
            artists_similarities.append((deviation, artist))

    artists_similarities.sort(key=lambda tup: tup[0])

    for artist in artists_similarities[:REC_LIST_SIZE]:
        rec.append(artist[1].name)

    return rec
