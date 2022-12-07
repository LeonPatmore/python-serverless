# Python Library Template

## How to Use

1. Setup your CodeArtifact project.
2. Run `make init` and pass your domain and repo.
3. Ensure that your `setup.py` has been configured correctly.
4. Run `make build`.
5. Run `make push`.

## Defining as Dependency

Add this to your pipfile:

```
[[source]]
url = "https://aws:$CODEARTIFACT_AUTH_TOKEN@my_domain-111122223333.d.codeartifact.eu-west-1.amazonaws.com/pypi/repo/simple/"
verify_ssl = true
name = "aws"
```

Make sure you export the auth token before you install or lock:

```shell
CODEARTIFACT_AUTH_TOKEN=`aws codeartifact get-authorization-token --domain my_domain --domain-owner 111122223333 --query authorizationToken --output text`
```
