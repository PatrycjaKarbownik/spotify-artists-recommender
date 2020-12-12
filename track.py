class Track:
    def __init__(self, name, **kwargs):
        self.id = kwargs['id']
        self.name = name
        self.danceability = kwargs['danceability']
        self.energy = kwargs['energy']
        self.key = kwargs['key']
        self.loudness = kwargs['loudness']
        self.mode = kwargs['mode']
        self.speechiness = kwargs['speechiness']
        self.acousticness = kwargs['acousticness']
        self.instrumentalness = kwargs['instrumentalness']
        self.liveness = kwargs['liveness']
        self.valence = kwargs['valence']
        self.tempo = kwargs['tempo']
        self.duration_ms = kwargs['duration_ms']
        self.time_signature = kwargs['time_signature']
