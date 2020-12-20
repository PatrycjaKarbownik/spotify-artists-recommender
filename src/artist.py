import statistics
from random import shuffle

from src.track import Features

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

    def search_unrelated_artists(self, artists):
        artists_ids = list(artists)
        shuffle(artists_ids)
        for artist_id in artists_ids:
            if artist_id not in self.related_artists:
                self.unrelated_artists.append(artist_id)
                if len(self.unrelated_artists) == UNRELATED_ARTISTS:
                    break

    def calc_avg_track_features(self):
        track_features = [track.features for track in self.tracks]
        features_averages = {}

        for feature_name in Features.get_features_list():
            feature_values = [getattr(features, feature_name) for features in track_features]
            features_averages[feature_name] = statistics.mean(feature_values)

        self.avg_track_features = Features(**features_averages)
