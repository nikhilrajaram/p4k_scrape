from src.model.Model import Model
from src.model.review.artist import Artist
from src.model.review.label import Label
from src.model.review.photos import Photos


class Album(Model):
    def __init__(self, artists=[], display_name="", labels=[], photos=None, release_year=None):
        self.artists = artists
        self.display_name = display_name
        self.labels = labels
        self.photos = photos
        self.release_year = release_year

    @classmethod
    def from_json(cls, json):
        if json is None:
            return Album()

        artists = [Artist.from_json(artist) for artist in json.get('artists')]
        labels = [Label.from_json(label) for label in json.get('labels')]
        return Album(artists, json.get('display_name'), labels, Photos.from_json(json.get('photos')),
                     json.get('release_year'))
