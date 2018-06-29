import pytest


def float_equal(x, y) -> bool:
    return abs(x - y) < 0.000001


@pytest.yield_fixture
def app():
    from web import app
    yield app


@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app))
