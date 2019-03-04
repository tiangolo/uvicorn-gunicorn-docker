#!/usr/bin/env bash

set -e
set -x

bash scripts/build-push.sh

bash scripts/trigger-children.sh
