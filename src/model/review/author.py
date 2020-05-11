from src.model.Model import Model


class Author(Model):
    def __init__(self, author_id=None, name="", slug="", title="", url=""):
        self.id = author_id
        self.name = name
        self.slug = slug
        self.title = title
        self.url = url

    @classmethod
    def from_json(cls, json):
        if json is None:
            return Author()

        return Author(json.get('id'), json.get('name'), json.get('slug'), json.get('title'), json.get('url'))
