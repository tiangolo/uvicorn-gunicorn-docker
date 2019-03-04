#!/usr/bin/env bash

set -e
set -x

body='{
"request": {
"branch":"master"
}}'

for child in tiangolo%2Fuvicorn-gunicorn-fastapi-docker tiangolo%2Fuvicorn-gunicorn-starlette-docker; do
   curl -s -X POST \
      -H "Content-Type: application/json" \
      -H "Accept: application/json" \
      -H "Travis-API-Version: 3" \
      -H "Authorization: token $TRAVIS_TOKEN" \
      -d "$body" \
      https://api.travis-ci.org/repo/$child/requests
done
