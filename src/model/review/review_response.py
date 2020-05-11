from src.model.Model import Model
from src.model.review.review_results import ReviewResults


class ReviewResponse(Model):
    def __init__(self, count=None, resp_next=None, previous=None, results=None):
        self.count = count
        self.next = resp_next
        self.previous = previous
        self.results = results

    @classmethod
    def from_json(cls, json):
        return ReviewResponse(json.get('count'), json.get('next'), json.get('previous'),
                              ReviewResults.from_json(json.get('results')))
