# Python Serverless

Python serverless is a small Python module which allows you to write cloud-agnostic serverless functions!

## Supported Cloud Providers

- AWS
- GCP

## Usage Example

```python
from python_serverless.serverless_function import serverless_function
from python_serverless.serverless_http import HttpRequest, HttpResponse

@serverless_function()
def handler(request: HttpRequest) -> HttpResponse:
    return HttpResponse(200, f"{request.body} received, looks good!")
```
