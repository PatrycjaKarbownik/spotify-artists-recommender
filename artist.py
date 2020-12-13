import statistics

from track import Features


class Artist:
    def __init__(self, spotify_id, name):
        self.spotify_id = spotify_id
        self.name = name
        self.tracks = []
        self.avg_track_features = None

    def set_tracks(self, tracks):
        self.tracks = tracks

    def get_tracks(self):
        return self.tracks

    def search_related_artists(self, spotify, artists_db):
        # todo search intersection (spotify.artist_related_artists & artists_db)
        # result = map(lambda artist: artist['id'], spotify.artist_related_artists(self.spotify_id)['artists'])
        pass

    def search_unrelated_artists(self, spotify, artists_db):
        pass

    def calc_avg_track_features(self):
        features = list(map(lambda track: track.features, self.tracks))
        danceabilities = list(map(lambda feature: feature.danceability, features))
        energies = list(map(lambda feature: feature.energy, features))
        acousticnesses = list(map(lambda feature: feature.acousticness, features))
        instrumentalnesses = list(map(lambda feature: feature.instrumentalness, features))
        valences = list(map(lambda feature: feature.valence, features))
        loudnesses = list(map(lambda feature: feature.loudness, features))
        modes = list(map(lambda feature: feature.mode, features))
        tempos = list(map(lambda feature: feature.tempo, features))
        time_signatures = list(map(lambda feature: feature.time_signature, features))

        dictionary = {
            "danceability": statistics.mean(danceabilities),
            "energy": statistics.mean(energies),
            "acousticness": statistics.mean(acousticnesses),
            "instrumentalness": statistics.mean(instrumentalnesses),
            "valence": statistics.mean(valences),
            "loudness": statistics.mean(loudnesses),
            "mode": statistics.mean(modes),
            "tempo": statistics.mean(tempos),
            "time_signature": statistics.mean(time_signatures)
        }

        self.avg_track_features = Features(**dictionary)
