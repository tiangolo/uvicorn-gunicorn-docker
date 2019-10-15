#!/usr/bin/env bash

set -e
set -x

bash scripts/build-push-all.sh

bash scripts/trigger-children.sh
