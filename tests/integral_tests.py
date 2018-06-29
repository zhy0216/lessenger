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
    async with aiohttp.ClientSession() as session:
        fetcher = Fetcher(session)
        latlng = await fetcher.fetch_latlng_by_postcode(94103)
        assert float_equal(latlng.lat, 37.7726402)
        assert float_equal(latlng.lng, -122.4099154)


@pytest.mark.asyncio
async def test_fetcher_fetch_current_weather_by_latlng():
    # weather is changing so, we have to mock it.
    async with aiohttp.ClientSession() as session:
        fetcher = Fetcher(session)
        latlng = await fetcher.fetch_latlng_by_address("sf")
        weather = await fetcher.fetch_current_weather_by_latlng(latlng)
        # assert weather.summary == "Mostly Cloudy"
        # assert float_equal(weather.temperature, 70.36)

