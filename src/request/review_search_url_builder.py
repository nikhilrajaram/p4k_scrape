import urllib.parse
import datetime


class ReviewSearchURLBuilder:
    """
    URL builder for search queries for Pitchfork reviews
    """
    SEARCH_ENDPOINT = "https://pitchfork.com/api/v2/search/"
    ROOT_QUERY = "?"
    ROOT_HIERARCHY = "hierarchy="
    ROOT_TYPES = "types="
    ROOT_SORT = "sort="
    COMMA_URLENCODED = "%2C"
    DATE_STRING = "%Y-%m-%d"

    def __init__(self):
        self.query_string = ReviewSearchURLBuilder.ROOT_QUERY
        self.query_types_string = ReviewSearchURLBuilder.ROOT_TYPES
        self.query_hierarchy_string = ReviewSearchURLBuilder.ROOT_HIERARCHY
        self.query_sort_string = ReviewSearchURLBuilder.ROOT_SORT
        self.query_size_string = None
        self.query_start_string = None
        self.query_from_string = None
        self.query_to_string = None

    @staticmethod
    def validate_int(n):
        """
        Validate if input is of type integer, if not raise ValueError
        :param n: object to validate
        :return: None
        """
        if type(n) is not int:
            raise ValueError("size argument must be of type int")

    @staticmethod
    def validate_date(date):
        """
        Validate if input is a date string matching the format 'yyyy-mm-dd'
        :param date: object to validate
        :return: None
        """
        try:
            datetime.datetime.strptime(date, ReviewSearchURLBuilder.DATE_STRING)
        except ValueError:
            raise ValueError("date format must match 'yyyy-mm-dd")

    def add_types_query(self, types):
        """
        Add an article type restriction to the query string
        :param types: list of types of article ordered by precedence
        :return: class instance
        """
        if self.query_types_string != ReviewSearchURLBuilder.ROOT_TYPES:
            self.query_types_string += ReviewSearchURLBuilder.COMMA_URLENCODED

        self.query_types_string += urllib.parse.quote_plus('/'.join(types))
        return self

    def add_hierarchy_query(self, hierarchy):
        """
        Add a hierarchy specification to the query string
        :param hierarchy: list of media ordered by precedence
        :return: class instance
        """
        if self.query_hierarchy_string != ReviewSearchURLBuilder.ROOT_HIERARCHY:
            self.query_hierarchy_string += ReviewSearchURLBuilder.COMMA_URLENCODED

        self.query_hierarchy_string += urllib.parse.quote_plus('/'.join(hierarchy))
        return self

    def add_sort_query(self, sort_field, sort_direction):
        """
        Add a sort specification to the query string
        :param sort_field: field to sort on
        :param sort_direction: asc/desc, which way to order query
        :return: class instance
        """
        if self.query_sort_string != ReviewSearchURLBuilder.ROOT_SORT:
            self.query_sort_string += ReviewSearchURLBuilder.COMMA_URLENCODED

        self.query_sort_string += urllib.parse.quote("{} {}".format(sort_field, sort_direction))
        return self

    def add_size_query(self, size):
        """
        Add a query for the number of results to return in one response to the query string
        :param size: number of results to return, integer > 0
        :return: class instance
        """
        ReviewSearchURLBuilder.validate_int(size)
        self.query_size_string = urllib.parse.urlencode({"size": size})
        return self

    def add_start_query(self, start):
        """
        Add a query for the index at which to start returning articles
        Intended for pagination purposes
        :param start: integer >= 0
        :return: class instance
        """
        ReviewSearchURLBuilder.validate_int(start)
        self.query_start_string = urllib.parse.urlencode({"start": start})
        return self

    def add_from_query(self, from_date):
        """
        Add a query to specify what date to return articles from (lower bound on date)
        :param from_date: ReviewSearchURLBuilder.DATESTRING formatted date string
        :return: class instance
        """
        ReviewSearchURLBuilder.validate_date(from_date)
        self.query_from_string = urllib.parse.urlencode({"from": from_date})
        return self

    def add_to_query(self, to_date):
        """
        Add a query to specify what date to return articles to (upper bound on date)
        :param to_date: ReviewSearchURLBuilder.DATESTRING formatted date string
        :return: class instance
        """
        ReviewSearchURLBuilder.validate_date(to_date)
        self.query_to_string = urllib.parse.urlencode({"to": to_date})
        return self

    def add_query(self, query):
        """
        Add a generic query string snippet to instance's query string
        :param query: query string snippet to add
        :return: None
        """
        if self.query_string[-1] != '?':
            self.query_string += '&'

        self.query_string += query

    def copy(self):
        """
        Copy and return a builder instance
        :return: instance copy
        """
        new_rsb = ReviewSearchURLBuilder()
        new_rsb.query_string = ReviewSearchURLBuilder.ROOT_QUERY
        new_rsb.query_types_string = self.query_types_string
        new_rsb.query_hierarchy_string = self.query_hierarchy_string
        new_rsb.query_sort_string = self.query_sort_string
        new_rsb.query_size_string = self.query_size_string
        new_rsb.query_start_string = self.query_start_string
        new_rsb.query_from_string = self.query_from_string
        new_rsb.query_to_string = self.query_to_string
        return new_rsb

    def build(self):
        """
        Build query URL to request
        :return: url with according query string
        """
        if self.query_types_string != ReviewSearchURLBuilder.ROOT_TYPES:
            self.add_query(self.query_types_string)

        if self.query_hierarchy_string != ReviewSearchURLBuilder.ROOT_HIERARCHY:
            self.add_query(self.query_hierarchy_string)

        if self.query_sort_string != ReviewSearchURLBuilder.ROOT_SORT:
            self.add_query(self.query_sort_string)

        if self.query_size_string is not None:
            self.add_query(self.query_size_string)

        if self.query_start_string is not None:
            self.add_query(self.query_start_string)

        if self.query_from_string is not None:
            self.add_query(self.query_from_string)

        if self.query_to_string is not None:
            self.add_query(self.query_to_string)

        url = ReviewSearchURLBuilder.SEARCH_ENDPOINT + self.query_string
        self.query_string = ReviewSearchURLBuilder.ROOT_QUERY
        return url
