import aiohttp
import pytest
from logic import Fetcher

from web import app
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


@pytest.mark.asyncio
async def test_fetcher_fetch_current_weather_by_latlng():
    async with aiohttp.ClientSession() as session:
        fetcher = Fetcher(session)
        latlng = await fetcher.fetch_latlng_by_postcode(94103)
        weather = await fetcher.fetch_current_weather_by_latlng(latlng)
        assert weather.summary
        assert weather.temperature


def weatehr_check(ask_weather):
    request, response = app.test_client.post('/chat/messages', data={
        "action": "message",
        "user_id": 123456,
        "text": ask_weather
    })
    assert response.status == 200
    assert response.json["messages"][0]["text"].startswith("Currently")


def test_weather_check():
    for ask_weather in ("weather in 94103",
                        "94103 weather",
                        "sf weather",
                        "what's the weather in sf"):
        weatehr_check(ask_weather)

