import aiohttp
import pytest
from logic import Fetcher
from tests import float_equal


@pytest.mark.asyncio
async def test_fetcher_fetch_latlng_by_address():
    async with aiohttp.ClientSession() as session:
        fetcher = Fetcher(session)
        latlng = await fetcher.fetch_latlng_by_address("sf")
        assert float_equal(latlng.lat, 37.7749295)
        assert float_equal(latlng.lng, -122.4194155)


@pytest.mark.asyncio
async def test_fetcher_fetch_latlng_by_postcode():
    async with aiohttp.ClientSession() as session:
        fetcher = Fetcher(session)
        latlng = await fetcher.fetch_latlng_by_postcode(94103)
        assert float_equal(latlng.lat, 37.7726402)
        assert float_equal(latlng.lng, -122.4099154)

