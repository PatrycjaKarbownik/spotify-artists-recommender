class Track:
    def __init__(self, name, **kwargs):
        self.id = kwargs['id']
        self.name = name
        self.features = Features(**kwargs)


class Features:
    def __init__(self, **kwargs):
        self.danceability = kwargs['danceability']
        self.energy = kwargs['energy']
        self.acousticness = kwargs['acousticness']
        self.instrumentalness = kwargs['instrumentalness']
        self.valence = kwargs['valence']
        self.loudness = kwargs['loudness']
        self.mode = kwargs['mode']
        # self.liveness = kwargs['liveness']  # to tracks filtering
        self.tempo = kwargs['tempo']
        self.time_signature = kwargs['time_signature']
