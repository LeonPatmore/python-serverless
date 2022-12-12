import flask
import pytest

from python_serverless.serverless_function import serverless_function
from python_serverless.serverless_http import HttpRequest, HttpResponse


@serverless_function()
def function_example(request: HttpRequest) -> HttpResponse:
    return HttpResponse(200, f"{request.body} received, looks good with method {request.method.name}!")


def test_aws(monkeypatch):
    monkeypatch.setenv("AWS_LAMBDA_FUNCTION_NAME", "myFunction")
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

    assert "hello received, looks good with method GET!" == response["body"]
    assert response["isBase64Encoded"]
    assert 200 == response["statusCode"]


@pytest.fixture()
def flask_setup():
    app = flask.Flask(__name__)
    return app


def test_gcp(monkeypatch, flask_setup):
    with flask_setup.test_request_context('/?name=Peter', data="hello"):
        monkeypatch.setenv("K_SERVICE", "myFunction")

        response = function_example(flask.request)

        assert ("hello received, looks good with method GET!", 200, {}) == response


def test_gcp_post(monkeypatch, flask_setup):
    with flask_setup.test_request_context('/?name=Peter', data="hello", method="POST"):
        monkeypatch.setenv("K_SERVICE", "myFunction")

        response = function_example(flask.request)

        assert ("hello received, looks good with method POST!", 200, {}) == response


def test_invalid_method(monkeypatch, flask_setup):
    monkeypatch.setenv("AWS_LAMBDA_FUNCTION_NAME", "myFunction")
    event = {
        "resource": "/",
        "path": "/",
        "httpMethod": "asd",
        "body": "hello"
    }
    context = {
        "function_name": "name"
    }
    with pytest.raises(Exception, match="'asd' is not a valid HttpMethod"):
        function_example(event, context)


def test_when_no_handler_supports_request_then_throw_exception():
    with pytest.raises(Exception, match="Not sure how to handle these kwargs"):
        function_example(a="b")
