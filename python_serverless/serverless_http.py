from enum import Enum


class HttpMethod(Enum):

    GET = "get"
    POST = "post"


class HttpRequest:

    def __init__(self, body: str, method: HttpMethod or str):
        self.body = body
        self.method = self.get_method_as_enum(method)

    @staticmethod
    def get_method_as_enum(method: HttpMethod or str) -> HttpMethod:
        if isinstance(method, str):
            return HttpMethod(method.lower())
        return method


class HttpResponse:

    def __init__(self, status: int, body: str):
        self.status = status
        self.body = body


class ProviderHttpHandler:

    def supports(self, *args, **kwargs) -> bool:
        raise NotImplementedError

    def generate_request(self, *args, **kwargs) -> HttpRequest:
        raise NotImplementedError

    def convert_to_response(self, response: HttpResponse):
        raise NotImplementedError
