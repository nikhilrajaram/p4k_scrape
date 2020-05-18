import requests
import numpy as np
import asyncio
import aiohttp

from src.error.paginated_request_error import PaginatedRequestError
from src.model.review.review_response import ReviewResponse


class ReviewRequest:
    """
    Serialize a (potentially) paginated response from Pitchfork's API
    Query specified by a ReviewSearchURLBuilder instance
    """
    DEFAULT_REQUEST_LEN = 200

    def __init__(self, rsb, request_len=DEFAULT_REQUEST_LEN):
        """
        Initialize ReviewRequest
        :param rsb: ReviewSearchURLBuilder which specifies query
        :param request_len: size parameter of requests
        """
        rsb.add_size_query(request_len)
        self.rsb = rsb
        self.request_len = request_len
        self.review_resp = None
        self._sync_session = requests.Session()
        self._async_session = None

    async def _async_session_init(self):
        """
        Instantiate asynchronous connection pool
        :return: None
        """
        self._async_session = aiohttp.ClientSession()

    def _execute_sync(self, url):
        """
        Execute a synchronous request to the Pitchfork API
        :param url: url to request
        :return: json-like response body as a dict
        """
        r = self._sync_session.get(url)
        if r.status_code != 200:
            raise PaginatedRequestError(url, "status code: {}".format(r.status_code))

        return r.json()

    async def _execute_async(self, url):
        """
        Create a coroutine for a single request to the Pitchfork API
        :param url: url to request
        :return: request coroutine
        """
        async with self._async_session.get(url) as r:
            if r.status != 200:
                raise PaginatedRequestError(url, "status code: {}".format(r.status))

            return await r.json()

    async def _batch_execute_async(self, urls):
        """
        Asynchronously perform requests to Pitchfork API to list of urls
        :param urls: list of urls to request
        :return: list of responses
        """
        tasks = [self._execute_async(url) for url in urls]
        resps = await asyncio.gather(self._async_session_init(), *tasks, return_exceptions=False)
        await self._async_session.close()
        return resps

    def execute(self):
        """
        Execute request specified by input ReviewSearchURLBuilder
        If request is paginated, make requests asynchronously
        Serialize response and return
        :return: Serialized response
        """
        page = 0
        self.review_resp = ReviewResponse.from_json(self._execute_sync(self.rsb.copy().add_start_query(0).build()))
        urls = []
        for i in range(1, np.ceil(self.review_resp.count/len(self.review_resp.results.reviews)).astype(int)):
            page += 1
            urls.append(self.rsb.copy().add_start_query(page*self.request_len).build())

        if urls:
            responses = asyncio.run(self._batch_execute_async(urls), debug=True)
            for resp in responses:
                if resp is None:
                    continue

                review_resp = ReviewResponse.from_json(resp)
                self.review_resp.results.reviews.extend(review_resp.results.reviews)

        return self.review_resp
