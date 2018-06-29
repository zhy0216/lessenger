from collections import namedtuple
from enum import Enum
from typing import List, Dict, Union, Tuple

import aiohttp

import setting

class Action(Enum):
    JOIN = 'join'
    MESSAGE = 'message'


class Message:
    type = None

    def to_json(self) -> Dict:
        raise NotImplementedError


class PureMessage(Message):
    type = 'text'

    def __init__(self, text=None):
        self.text = text

    def to_json(self) -> Dict:
        return {
            "type": self.type,
            "text": self.text
        }


class RichMessage(Message):
    type = 'rich'

    def __init__(self):
        pass

    def to_json(self) -> Dict:
        pass


Weather = namedtuple("Weather", ['temperature', 'summary'])
LatLng = namedtuple("LatLong", ['lat', 'lng'])

class Fetcher:
    GMAP_API_URL = "https://maps.googleapis.com/maps/api/geocode"
    DARK_SKY_API_URL = "https://api.darksky.net"

    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    async def fetch_latlng_by_address(self, address) -> LatLng:
        url = f"{self.GMAP_API_URL}/json?address={address}&key={setting.GMAP_API_KEY}"
        async with self.session.get(url) as r:
            r.raise_for_status()
            json = await r.json()
            location_json = json["results"][0]["geometry"]["location"]
            return LatLng(location_json["lat"], location_json["lng"])

    async def fetch_latlng_by_postcode(self, postcode) -> LatLng:
        url = f"{self.GMAP_API_URL}/json?components=postal_code:{postcode}&key={setting.GMAP_API_KEY}"
        async with self.session.get(url) as r:
            r.raise_for_status()
            json = await r.json()
            location_json = json["results"][0]["geometry"]["location"]
            return LatLng(location_json["lat"], location_json["lng"])

    async def fetch_current_weather_by_latlng(self, latlng: LatLng) -> Weather:
        latlng_str = ','.join(map(str, latlng))
        url = f"{self.DARK_SKY_API_URL}/forecast/{setting.DARK_SKY_API_KEY}/{latlng_str}?exclude=minutely,hourly,daily,alerts,flags"
        async with self.session.get(url) as r:
            r.raise_for_status()
            json = await r.json()
            return Weather(json["currently"]["temperature"], json["currently"]["summary"])

class ActionHandler:
    def __init__(self):
        pass

    async def response(self) -> List[Message]:
        raise NotImplementedError


class JoinActionHanlder(ActionHandler):
    def __init__(self, user_id=None, name=None):
        self.user_id = user_id
        self.name = name

    async def response(self) -> List[PureMessage]:
        return [PureMessage(text=f"Hello, {self.name}!")]


class MessageActionHanlder(ActionHandler):
    def __init__(self):
        pass

    async def response(self) -> List[PureMessage]:
        pass