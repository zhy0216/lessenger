from typing import List, Dict, Union
from enum import Enum

class Action(Enum):
    JOIN = 'join'
    MESSAGE = 'message'


class Message:
    pass


class PureMessage(Message):
    pass


class RichMessage(Message):
    pass


class ActionHandler:
    def __init__(self):
        pass

    async def response(self) -> List[Message]:
        raise NotImplementedError

    def get_handler_cls(self, action: Action):
        if action == Action.JOIN:
            return JoinActionHanlder
        elif action == Action.MESSAGE:
            return MessageActionHanlder
        else:
            raise ValueError(f'no such value {action}')


class JoinActionHanlder(ActionHandler):
    def __init__(self):
        pass

    async def response(self) -> List[PureMessage]:
        pass

class MessageActionHanlder(ActionHandler):
    def __init__(self):
        pass

    async def response(self) -> List[PureMessage]:
        pass