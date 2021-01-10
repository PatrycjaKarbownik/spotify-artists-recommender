MAX_TEMPO_VALUE = 300
MAX_LOUDNESS_VALUE = 60


class Track:
    def __init__(self, name, **kwargs):
        self.id = kwargs['id']
        self.name = name
        self.features = Features(**kwargs)


class Features:
    def __init__(self, **kwargs):
        # for feature_name in Features.get_features_list():
        #     if feature_name not in kwargs:
        #         print("{0} not defined".format(feature_name))

        self.danceability = kwargs.get("danceability", 0)
        self.energy = kwargs.get("energy", 0)
        self.acousticness = kwargs.get("acousticness", 0)
        self.instrumentalness = kwargs.get("instrumentalness", 0)
        self.valence = kwargs.get("valence", 0)
        self.loudness = kwargs.get("loudness", 0) / MAX_LOUDNESS_VALUE
        self.mode = kwargs.get("mode", 0)

        temporary_tempo = kwargs.get("tempo", 0) / MAX_TEMPO_VALUE
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
