

from sanic import Sanic
from sanic.response import json
from sanic_cors import CORS

app = Sanic(__name__)
CORS(app)


@app.route("/chat/messages", methods=['POST'])
async def hello_world(request):
    return json({
        "messages": [
            {
                "type": "text",
                "text": "Sorry, I don't have any sandwiches, but have a picture instead:"
            },
            {
                "type": "rich",
                "html": "<img src='http://i.imgur.com/J9DLQ.png'>"
            }
        ]
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)