from ..serverless_http import ProviderHttpHandler, HttpRequest, HttpResponse


class AwsHandler(ProviderHttpHandler):

    def generate_request(self, *args, **kwargs) -> HttpRequest:
        event = args[0]
        return HttpRequest(event["body"])

    def convert_to_response(self, response: HttpResponse):
        return {
            "isBase64Encoded": True,
            "statusCode": response.status,
            "body": response.body
        }

    def supports(self, *args, **kwargs) -> bool:
        return len(args) == 2
