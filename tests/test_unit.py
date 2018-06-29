import pytest

from logic import Fetcher, LatLng
from web import app
from tests import float_equal


async def test_join_action(test_cli):
    response = await test_cli.post('/chat/messages', data={
        "action": "join",
        "user_id": 123456,
        "name": "John"
    })
    assert response.status == 200
    assert (await response.json())["messages"][0]["text"] == "Hello, John!"
