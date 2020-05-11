import urllib


class ReviewSearchBuilder:
    SEARCH_ENDPOINT = "https://pitchfork.com/api/v2/search/"
    ROOT_QUERY = "?"
    ROOT_HIERARCHY = "hierarchy="
    ROOT_TYPES = "types="
    ROOT_SORT = "sort="
    COMMA_URLENCODED = "%2C"

    def __init__(self):
        self.query_string = ReviewSearchBuilder.ROOT_QUERY
        self.query_types_string = ReviewSearchBuilder.ROOT_TYPES
        self.query_hierarchy_string = ReviewSearchBuilder.ROOT_HIERARCHY
        self.query_sort_string = ReviewSearchBuilder.ROOT_SORT
        self.query_size_string = None
        self.query_start_string = None
        self.query_from_string = None
        self.query_to_string = None

    def add_types_query(self, types):
        if self.query_types_string != ReviewSearchBuilder.ROOT_TYPES:
            self.query_types_string += ReviewSearchBuilder.COMMA_URLENCODED

        self.query_types_string += urllib.parse.quote('/'.join(types))
        return self

    def add_hierarchy_query(self, hierarchy):
        if self.query_hierarchy_string != ReviewSearchBuilder.ROOT_HIERARCHY:
            self.query_hierarchy_string += ReviewSearchBuilder.COMMA_URLENCODED

        self.query_hierarchy_string += urllib.parse.quote('/'.join(hierarchy))
        return self

    def add_sort_query(self, sort_field, sort_direction):
        if self.query_sort_string != ReviewSearchBuilder.ROOT_SORT:
            self.query_sort_string += ReviewSearchBuilder.COMMA_URLENCODED

        self.query_sort_string += urllib.parse.quote("{} {}".format(sort_field, sort_direction))
        return self

    def add_size_query(self, size):
        self.query_size_string = urllib.parse.urlencode({"size": size})
        return self

    def add_start_query(self, start):
        self.query_start_string = urllib.parse.urlencode({"start": start})
        return self

    def add_from_query(self, from_date):
        self.query_from_string = urllib.parse.urlencode({"from": from_date})
        return self

    def add_to_query(self, to_date):
        self.query_to_string = urllib.parse.urlencode({"to": to_date})
        return self

    def add_query(self, query):
        if self.query_string[-1] != '?':
            self.query_string += '&'

        self.query_string += query

    def copy(self):
        new_rsb = ReviewSearchBuilder()
        new_rsb.query_string = ReviewSearchBuilder.ROOT_QUERY
        new_rsb.query_types_string = self.query_types_string
        new_rsb.query_hierarchy_string = self.query_hierarchy_string
        new_rsb.query_sort_string = self.query_sort_string
        new_rsb.query_size_string = self.query_size_string
        new_rsb.query_start_string = self.query_start_string
        new_rsb.query_from_string = self.query_from_string
        new_rsb.query_to_string = self.query_to_string
        return new_rsb

    def build(self):
        if self.query_types_string != ReviewSearchBuilder.ROOT_TYPES:
            self.add_query(self.query_types_string)

        if self.query_hierarchy_string != ReviewSearchBuilder.ROOT_HIERARCHY:
            self.add_query(self.query_hierarchy_string)

        if self.query_sort_string != ReviewSearchBuilder.ROOT_SORT:
            self.add_query(self.query_sort_string)

        if self.query_size_string is not None:
            self.add_query(self.query_size_string)

        if self.query_start_string is not None:
            self.add_query(self.query_start_string)

        if self.query_from_string is not None:
            self.add_query(self.query_from_string)

        if self.query_to_string is not None:
            self.add_query(self.query_to_string)

        url = ReviewSearchBuilder.SEARCH_ENDPOINT + self.query_string
        self.query_string = ReviewSearchBuilder.ROOT_QUERY
        return url
