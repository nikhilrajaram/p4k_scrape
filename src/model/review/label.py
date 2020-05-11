from src.model.Model import Model


class Label(Model):
    def __init__(self, display_name="", label_id=None, name=""):
        self.display_name = display_name
        self.id = label_id
        self.name = name

    @classmethod
    def from_json(cls, json):
        if json is None:
            return Label()

        return Label(json.get('display_name'), json.get('id'), json.get('name'))
