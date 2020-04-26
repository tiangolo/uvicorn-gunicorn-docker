#!/usr/bin/env bash
set -e

use_tag="tiangolo/uvicorn-gunicorn:$NAME"

DOCKERFILE=${DOCKERFILE-$NAME}

docker build -t "$use_tag" --file "./docker-images/${DOCKERFILE}.dockerfile" "./docker-images/"
pytest tests
