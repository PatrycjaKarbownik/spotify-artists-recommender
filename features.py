class Features:
    def __init__(self, **kwargs):
        self.danceability = kwargs['danceability']
        self.energy = kwargs['energy']
        self.acousticness = kwargs['acousticness']
        self.instrumentalness = kwargs['instrumentalness']
        self.valence = kwargs['valence']
