import pytest

from python_serverless.serverless_function import serverless_function
from python_serverless.serverless_http import HttpRequest, HttpResponse


@serverless_function()
def function_example(request: HttpRequest) -> HttpResponse:
    return HttpResponse(200, f"{request.body} received, looks good!")


def test_aws():
    event = {
        "resource": "/",
        "path": "/",
        "httpMethod": "GET",
        "body": "hello"
    }
    context = {
        "function_name": "name"
    }
    response = function_example(event, context)

    assert "hello received, looks good!" == response["body"]
    assert response["isBase64Encoded"]
    assert 200 == response["statusCode"]


def test_when_no_handler_supports_request_then_throw_exception():
    with pytest.raises(Exception, match="Not sure how to handle these kwargs"):
        function_example(a="b")
