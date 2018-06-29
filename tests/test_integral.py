import asyncio
import aiohttp
import pytest
from logic import Fetcher

from web import app
from tests import float_equal


async def test_fetcher_fetch_latlng_by_address():
    async with aiohttp.ClientSession() as session:
        fetcher = Fetcher(session)
        latlng = await fetcher.fetch_latlng_by_address("sf")
        assert float_equal(latlng.lat, 37.7749295)
        assert float_equal(latlng.lng, -122.4194155)


async def test_fetcher_fetch_latlng_by_postcode():
    async with aiohttp.ClientSession() as session:
        fetcher = Fetcher(session)
        latlng = await fetcher.fetch_latlng_by_postcode(94103)
        assert float_equal(latlng.lat, 37.7726402)
        assert float_equal(latlng.lng, -122.4099154)


async def test_fetcher_fetch_current_weather_by_latlng():
    async with aiohttp.ClientSession() as session:
        fetcher = Fetcher(session)
        latlng = await fetcher.fetch_latlng_by_postcode(94103)
        weather = await fetcher.fetch_current_weather_by_latlng(latlng)
        assert weather.summary
        assert weather.temperature


async def weatehr_check(test_cli, ask_weather):
    response = await test_cli.post('/chat/messages', data={
        "action": "message",
        "user_id": 123456,
        "text": ask_weather
    })
    assert response.status == 200
    assert (await response.json())["messages"][0]["text"].startswith("Currently")


async def test_weather_check1(test_cli):
    await asyncio.gather(weatehr_check(test_cli, "weather in 94103"),
                         weatehr_check(test_cli, "94103 weather"),
                         weatehr_check(test_cli, "sf weather"),
                         weatehr_check(test_cli, "what's the weather in sf"))
