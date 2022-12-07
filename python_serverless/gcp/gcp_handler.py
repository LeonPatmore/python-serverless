from ..serverless_http import ProviderHttpHandler, HttpRequest, HttpResponse


class GcpHandler(ProviderHttpHandler):

    def generate_request(self, **kwargs) -> HttpRequest:
        event = kwargs["request"]
        return HttpRequest(event.data)

    def convert_to_response(self, response: HttpResponse):
        return response.body, response.status, {}

    def supports(self, **kwargs) -> bool:
        return "request" in kwargs
