from src.model.Model import Model


class Genre(Model):
    def __init__(self, display_name="", slug=""):
        self.display_name = display_name
        self.slug = slug

    @classmethod
    def from_json(cls, json):
        if json is None:
            return Genre()

        return Genre(json.get('display_name'), json.get('slug'))
