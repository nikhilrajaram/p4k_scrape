from src.model.Model import Model


class Category(Model):
    def __init__(self, bio="", header="", category_id=None, mobile_header="", name="", url=""):
        self.bio = bio
        self.header = header
        self.id = category_id
        self.mobile_header = mobile_header
        self.name = name
        self.url = url

    @classmethod
    def from_json(cls, json):
        if json is None:
            return Category()

        return Category(json.get('bio'), json.get('header'), json.get('id'), json.get('mobile_header'),
                        json.get('name'), json.get('url'))
