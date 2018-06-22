import asyncio

import aiohttp
from async_timeout import timeout
from yarl import URL


__version__ = '0.1.0'


class GA:

    base_url = URL('https://www.google-analytics.com/')
    collect_path = 'collect'

    def __init__(
        self,
        tracking_id,
        version=1,
        timeout=60,
        session=None,
    ):
        self.tracking_id = tracking_id
        self.version = version
        self.timeout = timeout

        if session is None:
            session = aiohttp.ClientSession(
                connector=aiohttp.TCPConnector(
                    use_dns_cache=False,
                ),
            )

        self.session = session

        self.futs = set()

    def _prepare_params(self, request_type, cid, **kwargs):
        params = {
            'v': self.version,
            'tid': self.tracking_id,
            'cid': cid,
            't': request_type,
        }

        params.update(**kwargs)

        return params

    async def __request(self, request_type, cid, **kwargs):
        params = self._prepare_params(request_type, cid, **kwargs)

        response = None

        try:
            async with timeout(self.timeout):
                response = await self.session.post(
                    self.base_url / self.collect_path,
                    data=params,
                    headers={
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    timeout=None,
                )

            response.raise_for_status()

            return response
        finally:
            if response is not None:
                await response.release()

    def _request(self, *args, **kwargs):
        coro = self.__request(*args, **kwargs)
        fut = asyncio.ensure_future(coro)

        self.futs.add(fut)
        fut.add_done_callback(self.futs.remove)

        return fut

    def pageview(self, cid, **kwargs):
        return self._request('pageview', cid, **kwargs)

    def screenview(self, cid, **kwargs):
        return self._request('screenview', cid, **kwargs)

    def event(self, cid, **kwargs):
        return self._request('event', cid, **kwargs)

    def transaction(self, cid, **kwargs):
        return self._request('transaction', cid, **kwargs)

    def item(self, cid, **kwargs):
        return self._request('item', cid, **kwargs)

    def social(self, cid, **kwargs):
        return self._request('social', cid, **kwargs)

    def exception(self, cid, **kwargs):
        return self._request('exception', cid, **kwargs)

    def timing(self, cid, **kwargs):
        return self._request('timing', cid, **kwargs)

    async def close(self):
        if self.futs:
            await asyncio.gather(*self.futs)

        await self.session.close()

    async def __aenter__(self):  # noqa
        return self

    async def __aexit__(self, *exc_info):  # noqa
        await self.close()
