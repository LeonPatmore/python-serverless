import os

from ..serverless_http import ProviderHttpHandler, HttpRequest, HttpResponse


class AwsHandler(ProviderHttpHandler):

    def generate_request(self, *args, **kwargs) -> HttpRequest:
        event = args[0]
        return HttpRequest(event["body"], event["httpMethod"])

    def convert_to_response(self, response: HttpResponse):
        return {
            "isBase64Encoded": True,
            "statusCode": response.status,
            "body": response.body
        }

    def supports(self, *args, **kwargs) -> bool:
        return "AWS_LAMBDA_FUNCTION_NAME" in os.environ.keys()
