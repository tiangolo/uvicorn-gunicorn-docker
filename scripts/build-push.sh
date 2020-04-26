#!/usr/bin/env bash

set -e

use_tag="tiangolo/uvicorn-gunicorn:$NAME"
use_dated_tag="${use_tag}-$(date -I)"

DOCKERFILE=${DOCKERFILE-$NAME}

docker build -t "$use_tag" --file "./docker-images/${DOCKERFILE}.dockerfile" "./docker-images/"

docker tag "$use_tag" "$use_dated_tag"

docker push "$use_tag"
docker push "$use_dated_tag"
