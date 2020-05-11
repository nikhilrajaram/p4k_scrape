from src.model.Model import Model
from src.model.review.sizes import Sizes


class Tout(Model):
    def __init__(self, alt_text="", caption="", credit="", height=None, sizes=None, title="", width=None):
        self.alt_text = alt_text
        self.caption = caption
        self.credit = credit
        self.height = height
        self.sizes = sizes
        self.title = title
        self.width = width

    @classmethod
    def from_json(cls, json):
        if json is None:
            return Tout()

        return Tout(json.get('altText'), json.get('caption'), json.get('credit'), json.get('height'),
                    Sizes.from_json(json.get('sizes')), json.get('title'), json.get('width'))
