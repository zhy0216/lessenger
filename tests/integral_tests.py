import aiohttp
import pytest
from logic import Fetcher


def float_equal(x, y) -> bool:
    return abs(x - y) < 0.000001


@pytest.mark.asyncio
async def test_fetcher_fetch_latlng_by_address():
    async with aiohttp.ClientSession() as session:
        fetcher = Fetcher(session)
        latlng = await fetcher.fetch_latlng_by_address("sf")
        assert float_equal(latlng.lat, 37.7749295)
        assert float_equal(latlng.lng, -122.4194155)


@pytest.mark.asyncio
async def test_fetcher_fetch_latlng_by_postcode():
    pass


@pytest.mark.asyncio
async def test_fetcher_fetch_latlng_by_postcode():
    pass
