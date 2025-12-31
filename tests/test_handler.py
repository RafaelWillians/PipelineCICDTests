from lambdas.hello_world.handler import handler

def test_handler_response():
    result = handler({}, {})
    assert result["statusCode"] == 200
    assert result["body"] == "Hello World!"