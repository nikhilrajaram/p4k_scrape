from src.model.Model import Model
from src.model.review.category import Category
from src.model.review.review import Review


class ReviewResults(Model):
    def __init__(self, category=None, reviews=[]):
        self.category = category
        self.reviews = reviews

    @classmethod
    def from_json(cls, json):
        if json is None:
            return ReviewResults()

        reviews = [Review.from_json(review) for review in json.get('list')]
        return ReviewResults(Category.from_json(json.get('category')), reviews)
