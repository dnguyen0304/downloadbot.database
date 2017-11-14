#!/usr/bin/env bash

set -eu

PACKAGE_NAME=$(./scripts/get-package-name.sh)
TAG=$(./scripts/get-package-version.sh)

docker build \
    --file docker/buildtime/base/Dockerfile \
    --tag dnguyen0304/${PACKAGE_NAME}-buildtime-base:${TAG} \
    --build-arg SHARED_VOLUME="/tmp/build" \
    .
