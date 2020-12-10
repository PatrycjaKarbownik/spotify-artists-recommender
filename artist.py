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
        # todo maybe this way -> spotify.artist_related_artists(self.spotify_id)
        return []

    def search_for_unrelated_artists(self, spotify):
        # todo we are looking for unrelated artists idk how
        return []
    def calc_avg_track_features(self):
        # todo self.avg_track_features = ...
        pass