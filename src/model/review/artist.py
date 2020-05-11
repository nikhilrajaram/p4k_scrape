from src.model.Model import Model
from src.model.review.genre import Genre


class Artist(Model):
    def __init__(self, display_name="", genres=[], artist_id=None, photos=None, slug=None, url=""):
        self.display_name = display_name
        self.genres = genres
        self.id = artist_id
        self.photos = photos
        self.slug = slug
        self.url = url

    @classmethod
    def from_json(cls, json):
        if json is None:
            return Artist()

        genres = [Genre.from_json(genre) for genre in json.get('genres')]
        return Artist(json.get('display_name'), genres, json.get('id'), json.get('photos'), json.get('slug'),
                      json.get('url'))
