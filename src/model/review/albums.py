from src.model.Model import Model
from src.model.review.album import Album


class Albums(Model):
    def __init__(self, album=None, album_id=None, labels_and_years=[], rating=None):
        self.album = album
        self.album_id = album_id
        self.labels_and_years = labels_and_years
        self.rating = rating

    @classmethod
    def from_json(cls, json):
        if json is None:
            return Albums()

        return Albums(Album.from_json(json.get('album')), json.get('id'), json.get('labels_and_years'),
                      json.get('rating'))
