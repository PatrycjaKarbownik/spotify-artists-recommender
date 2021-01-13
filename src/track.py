MAX_TEMPO_VALUE = 300
MAX_LOUDNESS_VALUE = 60


class Track:
    def __init__(self, name, **kwargs):
        self.id = kwargs['id']
        self.name = name
        self.features = Features(**kwargs)


class Features:
    def __init__(self, **kwargs):
        self.danceability = kwargs.get("danceability")
        self.energy = kwargs.get("energy")
        self.acousticness = kwargs.get("acousticness")
        self.instrumentalness = kwargs.get("instrumentalness")
        self.valence = kwargs.get("valence")
        self.mode = kwargs.get("mode")
        self.loudness = kwargs.get("loudness")

        temporary_tempo = kwargs.get("tempo")

        if self.loudness is not None:
            self.loudness = self.loudness / MAX_LOUDNESS_VALUE
        if temporary_tempo is not None:
            temporary_tempo = temporary_tempo / MAX_TEMPO_VALUE
            self.tempo = 1 if temporary_tempo > 1 else temporary_tempo

    def increment(self, name):
        """Increments a counter specified by the 'name' argument."""
        self.__dict__[name] += 1

    def add(self, name, value):
        """Add value to argument specified by the 'name' ."""
        self.__dict__[name] += value

    @staticmethod
    def get_features_list():
        return [
            "danceability", "energy", "acousticness", "instrumentalness", "valence", "loudness", "mode", "tempo"
        ]

    @staticmethod
    def get_zeros_features():
        f = Features()
        for feature_name in Features.get_features_list():
            setattr(f, feature_name, 0)
        return f
