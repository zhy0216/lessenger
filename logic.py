from typing import List, Dict, Union
from enum import Enum

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

    def __init__(self, ):
        pass

    def to_json(self) -> Dict:
        return {
            "type": self.type,
            "text": self.text
        }


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