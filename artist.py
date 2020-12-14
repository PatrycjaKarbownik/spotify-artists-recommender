import statistics
from random import shuffle

from track import Features

UNRELATED_ARTISTS = 20


class Artist:
    def __init__(self, spotify_id, name):
        self.spotify_id = spotify_id
        self.name = name
        self.tracks = []
        self.related_artists = []
        self.unrelated_artists = []
        self.avg_track_features = None

    def set_tracks(self, tracks):
        self.tracks = tracks

    def get_tracks(self):
        return self.tracks

    def search_related_artists(self, spotify, artists_ids):
        related_artists = []
        for related in spotify.artist_related_artists(self.spotify_id)['artists']:
            related_artists.append(related['id'])
        self.related_artists = list(set(artists_ids) & set(related_artists))

    def search_unrelated_artists(self, artists_ids):
        shuffle(artists_ids)
        for artist_id in artists_ids:
            if artist_id not in self.related_artists:
                self.unrelated_artists.append(artist_id)
                if len(self.unrelated_artists) == UNRELATED_ARTISTS:
                    break

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
