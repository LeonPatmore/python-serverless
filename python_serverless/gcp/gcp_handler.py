import os

from ..serverless_http import ProviderHttpHandler, HttpRequest, HttpResponse


class GcpHandler(ProviderHttpHandler):

    def generate_request(self, *args, **kwargs) -> HttpRequest:
        event = args[0]
        return HttpRequest(event.data.decode("utf-8"))

    def convert_to_response(self, response: HttpResponse):
        return response.body, response.status, {}

    def supports(self, *args, **kwargs) -> bool:
        return "K_SERVICE" in os.environ.keys()
