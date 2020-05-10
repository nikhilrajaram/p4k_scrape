class ReviewResponse:
    def __init__(self, count=None, resp_next=None, previous=None, results=None):
        self.count = count
        self.next = resp_next
        self.previous = previous
        self.results = results
