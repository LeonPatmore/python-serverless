
FILE='config'

init:
	@read -p "Please enter your domain:" DOMAIN; \
	read -p "Please enter your repo:" REPO; \
	echo -e "$${DOMAIN}\n$${REPO}" > ${FILE}

push:
	pip install awscli twine && \
	aws codeartifact login --tool twine --domain rare --repository coding
