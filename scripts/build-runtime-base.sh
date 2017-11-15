#!/usr/bin/env bash

set -eu

PACKAGE_NAME=$(./scripts/get-package-name.sh)
TAG=$(./scripts/get-package-version.sh)
CONFIGURATION_DIRECTORY_NAME=$(./scripts/get-configuration-directory-name.sh)
CONFIGURATION_FILE_NAME=$(./scripts/get-configuration-file-name.sh)

docker build \
    --file docker/runtime/base/Dockerfile \
    --tag dnguyen0304/${PACKAGE_NAME}-runtime-base:${TAG} \
    --build-arg PACKAGE_NAME=${PACKAGE_NAME} \
    --build-arg CONFIGURATION_DIRECTORY_NAME=${CONFIGURATION_DIRECTORY_NAME} \
    --build-arg CONFIGURATION_FILE_NAME=${CONFIGURATION_FILE_NAME} \
    .
