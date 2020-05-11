import requests

from src.model.review.review_response import ReviewResponse


class ReviewRequest:
    def __init__(self, url):
        self.url = url
        self.r = None
        self.json = None
        self.review = None

    def execute(self):
        if self.r is not None:
            return self.review

        return self.serialize(requests.get(self.url))

    def serialize(self, r):
        self.r = r
        self.json = r.json()

        try:
            self.review = ReviewResponse.from_json(self.json)
        except ValueError as ex:
            print(ex)

        return self.review
