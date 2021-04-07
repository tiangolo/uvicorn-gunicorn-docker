AWS_ACCOUNT=$(shell aws sts get-caller-identity | jq -r '.Account')
REGISTRY="${AWS_ACCOUNT}.dkr.ecr.us-east-2.amazonaws.com"
IMAGE=${AWS_ACCOUNT}.dkr.ecr.us-east-2.amazonaws.com/mandolin/data-api:base-v0.1

.PHONY: help
help:
	:  # noop

# -- api (docker) --

.PHONY: build
build:
	docker build --platform linux/amd64 -t ${IMAGE} -f docker-images/python3.8-ubuntu.dockerfile ./docker-images

.PHONY: push
push:
	aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin $(REGISTRY) && \
	docker push ${IMAGE}

docker-login:
	aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin $(REGISTRY)
