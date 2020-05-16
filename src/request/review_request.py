import requests

from src.error.paginated_request_error import PaginatedRequestError
from src.model.review.review_response import ReviewResponse


class ReviewRequest:
    DEFAULT_REQUEST_LEN = 23

    def __init__(self, rsb, request_len=DEFAULT_REQUEST_LEN):
        rsb.add_size_query(request_len)
        self.rsb = rsb
        self.request_len = request_len
        self.review_resp = None

    @staticmethod
    def _serialize(r):
        return ReviewResponse.from_json(r.json())

    @staticmethod
    def _execute(url):
        r = requests.get(url)
        if r.status_code != 200:
            raise PaginatedRequestError(url, "status code: {}".format(r.status_code))

        return ReviewRequest._serialize(requests.get(url))

    def execute(self):
        page = 0
        url = self.rsb.copy().add_start_query(0).build()
        self.review_resp = self._execute(url)
        count = self.review_resp.count
        n = len(self.review_resp.results.reviews)

        while n < count:
            page += 1
            url = self.rsb.copy().add_start_query(page*self.request_len).build()
            temp_resp = self._execute(url)
            self.review_resp.results.reviews.extend(temp_resp.results.reviews)
            n += len(temp_resp.results.reviews)

        return self.review_resp
