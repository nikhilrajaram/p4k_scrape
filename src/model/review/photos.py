from src.model.Model import Model
from src.model.review.tout import Tout


class Photos(Model):
    def __init__(self, lede=None, social=None, tout=None):
        self.lede = lede
        self.social = social
        self.tout = tout

    @classmethod
    def from_json(cls, json):
        if json is None:
            return Photos()

        return Photos(json.get('lede'), json.get('social'), Tout.from_json(json.get('tout')))
