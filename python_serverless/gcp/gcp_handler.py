from ..serverless_http import ProviderHttpHandler, HttpRequest, HttpResponse


class GcpHandler(ProviderHttpHandler):

    def generate_request(self, *args, **kwargs) -> HttpRequest:
        event = kwargs["request"]
        return HttpRequest(event.data)

    def convert_to_response(self, response: HttpResponse):
        return response.body, response.status, {}

    def supports(self, *args, **kwargs) -> bool:
        return "request" in kwargs
