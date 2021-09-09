FILE=config

define \n


endef

CONFIG := $(file <${FILE})
CONFIG_AS_LIST := $(subst ${\n}, ,${CONFIG})
DOMAIN := $(word 1,${CONFIG_AS_LIST})
REPO := $(word 2,${CONFIG_AS_LIST})

get:
	@echo "Domain is ${DOMAIN}"
	@echo "Repo is ${REPO}"

init:
	@read -p "Please enter your domain:" DOMAIN; \
	read -p "Please enter your repo:" REPO; \
	echo -e "$${DOMAIN}\n$${REPO}" > ${FILE}

push:
	pip install awscli twine && \
	aws codeartifact login --tool twine --domain rare --repository coding
