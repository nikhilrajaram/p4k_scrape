from src.model.Model import Model


class Sizes(Model):
    def __init__(self, homepage_large="", homepage_small="", list="", standard=""):
        self.homepage_large = homepage_large
        self.homepage_small = homepage_small
        self.list = list
        self.standard = standard

    @classmethod
    def from_json(cls, json):
        if json is None:
            return Sizes()

        return Sizes(json.get('homepageLarge'), json.get('homepageSmall'), json.get('list'), json.get('standard'))
