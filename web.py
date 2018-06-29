from typing import List

from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS
from logic import Action, JoinActionHanlder, MessageActionHanlder, Message, MessageActionDispatcher

app = Sanic(__name__)
CORS(app)


@app.exception(Exception)
async def error_handler(request, exception):
    return json({"messsages": dict(type="error", text="error:" + str(exception))})


@app.route("/chat/messages", methods=['POST'])
async def hello_world(request):
    action = Action(request.form.get('action'))
    if action == Action.JOIN:
        user_id = request.form.get('user_id')
        name = request.form.get('name')
        handler = JoinActionHanlder(user_id=user_id, name=name)
    elif action == Action.MESSAGE:
        user_id = request.form.get('user_id')
        text = request.form.get('text')
        dispatcher = MessageActionDispatcher(user_id=user_id, text=text)
        handler = await dispatcher.parse_text()

    messages: List[Message] = await handler.response()
    return json({
        "messages": [m.to_json() for m in messages]
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)