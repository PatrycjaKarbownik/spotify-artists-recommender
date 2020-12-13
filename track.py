from features import Features


class Track:
    def __init__(self, name, **kwargs):
        self.id = kwargs['id']
        self.name = name
        self.features = Features(**kwargs)
