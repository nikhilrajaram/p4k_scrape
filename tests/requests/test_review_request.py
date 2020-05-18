import pytest
import datetime

from src.error.paginated_request_error import PaginatedRequestError
from src.request.review_request import ReviewRequest
from src.request.review_search_url_builder import ReviewSearchURLBuilder


class TestReviewRequest:
    def test_execute_from_1mo_ago(self):
        date_1mo_ago = (datetime.datetime.now()-datetime.timedelta(weeks=1)).strftime('%Y-%m-%d')
        rsb = ReviewSearchURLBuilder().add_from_query(date_1mo_ago)
        try:
            ReviewRequest(rsb).execute()
        except PaginatedRequestError:
            assert False

        assert True
