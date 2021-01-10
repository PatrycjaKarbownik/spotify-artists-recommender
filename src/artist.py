import statistics
from random import sample

from src.track import Features

UNRELATED_ARTISTS = 20
MINIMUM_RELATED_ARTISTS = 10
SPOTIFY_ARTIST_LINK_TEMPLATE = 'https://open.spotify.com/artist/'


class Artist:
    def __init__(self, spotify_id, name, genres=None):
        self.spotify_id = spotify_id
        self.spotify_link = SPOTIFY_ARTIST_LINK_TEMPLATE + spotify_id
        self.name = name
        self.genres = genres
        self.tracks = []
        self.related_artists = []
        self.unrelated_artists = []
        self.avg_track_features = None

    def set_tracks(self, tracks):
        self.tracks = tracks

    def search_related_artists(self, spotify, artists_main_ids, artists_supp):
        related_artists = []
        for related in spotify.artist_related_artists(self.spotify_id)['artists']:
            related_artists.append(Artist(related['id'], related['name'], related['genres']))
        # related artists based on main db and spotify api query
        self.related_artists = list(set(artists_main_ids) & set([x.spotify_id for x in related_artists]))

        # if self.related_artists list is not enough long we should add more artists from spotify api query and
        # update supporting database
        if len(related_artists) < MINIMUM_RELATED_ARTISTS:
            return

        it = 0
        while len(self.related_artists) < MINIMUM_RELATED_ARTISTS:
            related_artist = related_artists[it]
            if related_artist.spotify_id not in self.related_artists:
                self.related_artists.append(related_artist.spotify_id)
                if related_artist.spotify_id not in artists_supp:
                    artists_supp[related_artist.spotify_id] = related_artist
            it += 1

    def search_unrelated_artists(self, artists):
        artists_ids = list(artists)
        index_list = sample(range(len(artists_ids)), len(self.related_artists) + UNRELATED_ARTISTS)

        for idx in index_list:
            artist_id = artists_ids[idx]
            if artist_id not in self.related_artists and artist_id != self.spotify_id:
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
