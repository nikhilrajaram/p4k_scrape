import pytest
import urllib

from src.request.review_search_builder import ReviewSearchURLBuilder


class TestReviewSearchBuilder:
    SCHEME = 'https'
    NETLOC = 'pitchfork.com'
    PATH = '/api/v2/search/'

    @staticmethod
    def assert_base(parsed):
        assert parsed.scheme == TestReviewSearchBuilder.SCHEME
        assert parsed.netloc == TestReviewSearchBuilder.NETLOC
        assert parsed.path == TestReviewSearchBuilder.PATH

    def test_add_types_query(self):
        rsb = ReviewSearchURLBuilder()\
            .add_types_query(['a', 'b', 'c'])
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'types=a%2Fb%2Fc'

    def test_add_multiple_types_query(self):
        rsb = ReviewSearchURLBuilder()\
            .add_types_query(['a', 'b', 'c'])\
            .add_types_query(['d', 'e', 'f'])
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'types=a%2Fb%2Fc%2Cd%2Fe%2Ff'

    def test_add_hierarchy_query(self):
        rsb = ReviewSearchURLBuilder()\
            .add_hierarchy_query(['a', 'b', 'c'])
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'hierarchy=a%2Fb%2Fc'

    def test_add_multiple_hierarchy_query(self):
        rsb = ReviewSearchURLBuilder()\
            .add_hierarchy_query(['a', 'b', 'c'])\
            .add_hierarchy_query(['d', 'e', 'f'])
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'hierarchy=a%2Fb%2Fc%2Cd%2Fe%2Ff'

    def test_add_sort_query(self):
        rsb = ReviewSearchURLBuilder()\
            .add_sort_query('a', 'b')
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'sort=a%20b'

    def test_add_multiple_sort_query(self):
        rsb = ReviewSearchURLBuilder()\
            .add_sort_query('a', 'b')\
            .add_sort_query('c', 'd')
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'sort=a%20b%2Cc%20d'

    def test_add_size_query(self):
        rsb = ReviewSearchURLBuilder()\
            .add_size_query(1)
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'size=1'

    def test_add_size_query_str_error(self):
        rsb = ReviewSearchURLBuilder()
        try:
            rsb.add_size_query("a")
        except ValueError:
            assert True
            return
        assert False

    def test_add_multiple_size_query(self):
        rsb = ReviewSearchURLBuilder()\
            .add_size_query(1)\
            .add_size_query(2)
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'size=2'

    def test_add_start_query(self):
        rsb = ReviewSearchURLBuilder()\
            .add_start_query(1)
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'start=1'

    def test_add_start_query_str_error(self):
        rsb = ReviewSearchURLBuilder()
        try:
            rsb.add_start_query("a")
        except ValueError:
            assert True
            return
        assert False

    def test_add_multiple_start_query(self):
        rsb = ReviewSearchURLBuilder()\
            .add_start_query(1)\
            .add_start_query(2)
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'start=2'

    def test_add_from_query(self):
        date = "2011-01-01"
        rsb = ReviewSearchURLBuilder()\
            .add_from_query(date)
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'from={}'.format(date)

    def test_add_from_query_date_error(self):
        date = "2011-13-01"   # incorrect month
        rsb = ReviewSearchURLBuilder()
        try:
            rsb.add_from_query(date)
        except ValueError:
            assert True
            return
        assert False

    def test_add_multiple_from_query(self):
        date1 = "2011-01-01"
        date2 = "2012-01-01"
        rsb = ReviewSearchURLBuilder()\
            .add_from_query(date1)\
            .add_from_query(date2)
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'from={}'.format(date2)

    def test_add_to_query(self):
        date = "2011-01-01"
        rsb = ReviewSearchURLBuilder()\
            .add_to_query(date)
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'to={}'.format(date)

    def test_add_to_query_date_error(self):
        date = "2011-13-01"   # incorrect month
        rsb = ReviewSearchURLBuilder()
        try:
            rsb.add_to_query(date)
        except ValueError:
            assert True
            return
        assert False

    def test_add_multiple_to_query(self):
        date1 = "2011-01-01"
        date2 = "2012-01-01"
        rsb = ReviewSearchURLBuilder()\
            .add_to_query(date1)\
            .add_to_query(date2)
        url = rsb.build()
        parsed = urllib.parse.urlparse(url)
        TestReviewSearchBuilder.assert_base(parsed)
        assert parsed.query == 'to={}'.format(date2)
