from typing import List

from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS
from logic import Action, JoinActionHanlder, MessageActionHanlder, Message

app = Sanic(__name__)
CORS(app)


@app.route("/chat/messages", methods=['POST'])
async def hello_world(request):
    action = Action(request.form.get('action'))
    if action == Action.JOIN:
        user_id = request.form.get('user_id')
        name = request.form.get('name')
        handler = JoinActionHanlder(user_id=user_id, name=name)
    elif action == Action.MESSAGE:
        handler = MessageActionHanlder()

    messages: List[Message] = await handler.response()
    return json({
        "messages": [m.to_json() for m in messages]
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)