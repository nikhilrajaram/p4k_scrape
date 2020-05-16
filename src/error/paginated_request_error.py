from src.error.request_error import RequestError


class PaginatedRequestError(RequestError):
    """Exception raised when one request in a paginated request is not successful
    Attributes:
        url -- url to which request failed
        message -- explanation of the error
    """
    def __init__(self, url, message):
        self.url = url
        self.message = message
