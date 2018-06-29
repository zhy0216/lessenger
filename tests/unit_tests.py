from web import app


def test_join_action():
    request, response = app.test_client.post('/chat/messages', data={
        "action": "join",
        "user_id": 123456,
        "name": "John"
    })
    assert response.status == 200
    assert response.json["messages"][0]["text"] == "Hello, John!"
