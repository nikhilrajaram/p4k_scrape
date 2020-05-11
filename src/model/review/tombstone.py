from src.model.Model import Model
from src.model.review.albums import Albums


class Tombstone(Model):
    def __init__(self, albums=[], bnm=None, bnr=None):
        self.albums = albums
        self.bnm = bnm
        self.bnr = bnr

    @classmethod
    def from_json(cls, json):
        if json is None:
            return Tombstone()

        albums = [Albums.from_json(album) for album in json.get('albums')]
        return Tombstone(albums, json.get('bnm'), json.get('bnr'))
