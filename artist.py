import statistics
from features import Features


class Artist:
    def __init__(self, name, spotify_id, spotify):
        self.name = name
        self.spotify_id = spotify_id
        self.tracks = []
        self.avg_track_features = None

        self.spotify_id_related_artists = self.search_for_related_artists(spotify)
        self.spotify_id_not_related_artists = self.search_for_unrelated_artists(spotify)

    def set_tracks(self, tracks):
        self.tracks = tracks

    def get_tracks(self):
        return self.tracks

    def search_for_related_artists(self, spotify):
        result = map(lambda artist: artist['id'], spotify.artist_related_artists(self.spotify_id)['artists'])
        return list(result)

    def search_for_unrelated_artists(self, spotify):
        # todo we are looking for unrelated artists idk how
        return []

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
