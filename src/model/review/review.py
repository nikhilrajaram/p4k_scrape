from src.model.Model import Model
from src.model.review.artist import Artist
from src.model.review.author import Author
from src.model.review.genre import Genre
from src.model.review.tombstone import Tombstone


class Review(Model):
    def __init__(self, artists=[], authors=[], channel="", content_type="", dek="", genres=[], review_id=None,
                 modified_at=None, position=None, private_tags=[], promo_description="", promo_title="",
                 pub_date=None, seo_description="", seo_title="", social_description="", social_title="",
                 sub_channel="", tags=[], timestamp=None, title="", tombstone=None, url=""):
        self.artists = artists
        self.authors = authors
        self.channel = channel
        self.content_type = content_type
        self.dek = dek
        self.genres = genres
        self.id = review_id
        self.modified_at = modified_at
        self.position = position
        self.private_tags = private_tags
        self.promo_description = promo_description
        self.promo_title = promo_title
        self.pub_date = pub_date
        self.seo_description = seo_description
        self.seo_title = seo_title
        self.social_description = social_description
        self.social_title = social_title
        self.sub_channel = sub_channel
        self.tags = tags
        self.timestamp = timestamp
        self.title = title
        self.tombstone = tombstone
        self.url = url

    @classmethod
    def from_json(cls, json):
        if json is None:
            return Review()

        try:
            artists = [Artist.from_json(artist) for artist in json.get('artists')]
        except TypeError:
            artists = []

        try:
            authors = [Author.from_json(author) for author in json.get('authors')]
        except TypeError:
            authors = []

        try:
            genres = [Genre.from_json(genre) for genre in json.get('genres')]
        except TypeError:
            genres = []

        return Review(artists, authors, json.get('channel'), json.get('contentType'), json.get('dek'), genres,
                      json.get('id'), json.get('modifiedAt'), json.get('position'), json.get('privateTags'),
                      json.get('promoDescription'), json.get('promoTitle'), json.get('pubDate'),
                      json.get('seoDescription'), json.get('seoTitle'), json.get('socialDescription'),
                      json.get('socialTitle'), json.get('subChannel'), json.get('tags'), json.get('timestamp'),
                      json.get('title'), Tombstone.from_json(json.get('tombstone')), json.get('url'))
